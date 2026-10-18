#!/usr/bin/env python3
"""BoardBook crawler for PPS (organization 915): Python port of tools/browser/boardbook_crawl.js.

Use it on any machine that can reach meetings.boardbook.org (needs beautifulsoup4):

  python3 boardbook_crawl.py OUT_DIR --index OLD_INDEX.json [--since 2025-01-01] [--only ID ID ...] [--refresh-items ID ...]

- Reads the org meeting table once and writes OUT_DIR/boardbook/boardbook_index_2025_2026.json. Agenda attachment
  lists ("items") are kept from OLD_INDEX for meetings not named in --only/--refresh-items, and re-read for those named
  (and for meetings OLD_INDEX doesn't have).
- Downloads each --only meeting exactly as the JS version does: agenda/minutes/public_notice/supplementals HTML,
  the minutes and notice PDFs, and every agenda attachment as PDF, into
  OUT_DIR/boardbook/meetings/<date>_<id>_<slug>/..., plus OUT_DIR/boardbook/_manifests/_manifest_bb_<id>.json
  (url, final_url, status, content_type, bytes, fetched_at) for provenance.
Then copy OUT_DIR/boardbook into sources/ and run the processing steps in RUNBOOK.md section 1a.5.
"""
import argparse, json, re, sys, time, datetime, pathlib, urllib.request
from bs4 import BeautifulSoup

BASE = 'https://meetings.boardbook.org'
ORG = '/public/Organization/915'
MON = {m: i for i, m in enumerate(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                     'September', 'October', 'November', 'December'], 1)}
DRE = re.compile(r'(January|February|March|April|May|June|July|August|September|October|November|December) (\d+), (20\d\d)')
UA = {'User-Agent': 'Mozilla/5.0 (archive refresh; PPS research)'}


def get(path):
    url = path if path.startswith('http') else BASE + path
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.status, r.geturl(), r.headers.get('Content-Type', '').split(';')[0], r.read()


def date_of(head):
    x = DRE.search(head)
    return f"{x[3]}-{MON[x[1]]:02d}-{int(x[2]):02d}" if x else ''


def bb_dir(head, mid):
    d = date_of(head) or 'unknown'
    s = re.sub(r'^Cancelled ', '', head)
    s = ' '.join(s.split(' - ')[1:])
    s = re.sub(r'Cancelled$', '', s).strip().lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:50]
    return f"{d}_{mid}_{s}"


def safe(s):
    s = re.sub(r'[\\/:*?"<>|]+', '', s)
    return re.sub(r'\s+', '_', s)[:120]


def text(el):
    return re.sub(r'\s+', ' ', el.get_text(' ')).strip() if el else ''


def org_meetings(since):
    soup = BeautifulSoup(get(ORG)[3], 'html.parser')
    out = []
    for tr in soup.select('#PublicMeetingsTable tbody tr'):
        tds = tr.find_all('td')
        if len(tds) < 3:
            continue
        m = re.search(r'meeting=(\d+)', str(tr))
        div = tds[0].find('div')
        head = text(div)
        t = re.search(r'Meeting Type:\s*(.+)', tds[0].get_text('\n'))
        loc = tds[1].select_one('span[id$=description]')
        vids = [a.get('href') for a in tds[1].find_all('a') if re.search(r'watch\?v=|youtu\.be/', a.get('href') or '')]
        det = [{'t': text(a), 'h': a.get('href')} for a in tds[2].find_all('a')]
        if m and date_of(head) >= since:
            out.append({'id': m[1], 'head': head, 'type': t[1].strip() if t else None,
                        'loc': loc.get_text().strip() if loc else None, 'vids': vids, 'det': det})
    return out


def agenda_items(mid):
    soup = BeautifulSoup(get('/Public/Agenda/915?meeting=' + mid)[3], 'html.parser')
    items = []
    for a in soup.select('a[data-documentid], a[href*="FileViewerOrPublic"]'):
        f = a.get('data-documentid') or (re.search(r'file=(\d+)', a.get('href') or '') or [None, None])[1]
        if not f:
            continue
        row = a.find_parent('tr')
        chk = row.select_one('.form-check') if row else None
        items.append({'file': f, 'name': a.get_text().strip(), 'item': text(chk)[:200]})
    return items


def fetch_meeting(m, out):
    d = 'boardbook/meetings/' + bb_dir(m['head'], m['id']) + '/'
    todo = [('/Public/Agenda/915?meeting=' + m['id'], d + 'agenda.html', 'agenda', None)]
    for kind, path in (('minutes', '/Public/Minutes/915?meeting='), ('public_notice', '/Public/PublicNotice/915?meeting='),
                       ('supplementals', '/Meeting/Supplementals/915?meeting=')):
        if not any(path.split('/')[2].lower() in (x['h'] or '').lower() for x in m['det']):
            continue
        h = get(path + m['id'])[3].decode('utf-8', 'replace')
        todo.append((path + m['id'], d + kind + '.html', kind, None))
        dm = re.search(r'id="NewDocumentViewerDocumentID" value="(\d+)"', h)
        if dm and kind != 'supplementals':
            todo.append((f'/Documents/DownloadPDF/{dm[1]}?org=915', f'{d}{kind}_{dm[1]}.pdf', kind + ' pdf', None))
        if kind == 'supplementals':
            for a in BeautifulSoup(h, 'html.parser').find_all('a', href=True):
                f = re.search(r'file=(\d+)', a['href']) or re.search(r'/Documents/\w+/(\d+)', a['href'])
                if f:
                    t = a.get_text().strip()
                    todo.append((f'/Documents/DownloadPDF/{f[1]}?org=915', f'{d}supplemental/{f[1]}_{safe(t or f[1])}.pdf', t, None))
    for it in m['items']:
        todo.append((f"/Documents/DownloadPDF/{it['file']}?org=915", f"{d}attachments/{it['file']}_{safe(it['name'])}.pdf",
                     it['name'], it['item']))
    man = []
    for url, path, title, found in todo:
        rec = {'path': path, 'url': url, 'final_url': '', 'status': 0, 'content_type': '', 'bytes': 0, 'error': '',
               'fetched_at': datetime.datetime.utcnow().isoformat(timespec='seconds') + 'Z', 'title': title}
        if found:
            rec['found_on'] = found
        try:
            st, fu, ct, body = get(url)
            p = out / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(body)
            rec.update(final_url=fu, status=st, content_type=ct, bytes=len(body))
        except Exception as e:
            rec['error'] = str(e)
        man.append(rec)
        print(rec['status'], rec['bytes'], path, rec['error'], flush=True)
        time.sleep(0.7)
    mp = out / 'boardbook/_manifests' / f"_manifest_bb_{m['id']}.json"
    mp.parent.mkdir(parents=True, exist_ok=True)
    mp.write_text(json.dumps(man, indent=1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('out')
    ap.add_argument('--index', required=True)
    ap.add_argument('--since', default='2025-01-01')
    ap.add_argument('--only', nargs='*', default=[])
    ap.add_argument('--refresh-items', nargs='*', default=[])
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    old = {m['id']: m for m in json.loads(pathlib.Path(a.index).read_text())['meetings']}
    ms = org_meetings(a.since)
    for m in ms:
        if m['id'] in a.only or m['id'] in a.refresh_items or m['id'] not in old:
            m['items'] = agenda_items(m['id'])
            time.sleep(0.5)
        else:
            m['items'] = old[m['id']].get('items', [])
    idx = {'generated': datetime.datetime.utcnow().isoformat(timespec='seconds') + 'Z', 'source': BASE + ORG, 'meetings': ms}
    ip = out / 'boardbook/boardbook_index_2025_2026.json'
    ip.parent.mkdir(parents=True, exist_ok=True)
    ip.write_text(json.dumps(idx, indent=1))
    new = [m['id'] for m in ms if m['id'] not in old]
    print('meetings', len(ms), 'new', new, flush=True)
    for m in ms:
        if m['id'] in a.only:
            fetch_meeting(m, out)


if __name__ == '__main__':
    main()
