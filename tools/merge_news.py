#!/usr/bin/env python3
"""Merge new news records (JSON array files) into sources/news/index.jsonl.

  python3 tools/merge_news.py records.json [more.json ...] [--outlet-slug oregonian] [--write]

- Matches existing records by normalized URL; a match is replaced in place and keeps its id.
- New records get ids NEWS-YYYYMMDD-<slug>-N (next free N).
- Checks CLAUDE.md rule 8: each short quote under 25 words; summary present; no long text fields.
Dry run by default.
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / 'sources/news/index.jsonl'
KEY_ORDER = ['id', 'date', 'outlet', 'title', 'url', 'author', 'topics', 'schools_mentioned', 'people_quoted',
             'summary', 'key_facts', 'short_quotes', 'retrieved', 'access', 'access_note', 'date_precision']


def norm(u):
    u = (u or '').strip().split('#')[0].split('?')[0]
    u = re.sub(r'^https?://(www\.)?', '', u).rstrip('/')
    return u.lower()


def check(r):
    problems = []
    for q in r.get('short_quotes', []):
        n = len(q.get('quote', '').split())
        if n >= 25:
            problems.append(f"quote {n} words: {q['quote'][:60]}")
    if not r.get('summary'):
        problems.append('no summary')
    if len(r.get('summary', '')) > 1500:
        problems.append(f"summary long ({len(r['summary'])} chars)")
    return problems


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    write = '--write' in sys.argv
    slug = 'oregonian'
    if '--outlet-slug' in sys.argv:
        slug = sys.argv[sys.argv.index('--outlet-slug') + 1]
        args.remove(slug)
    recs = [json.loads(l) for l in INDEX.open() if l.strip()]
    by_url = {norm(r.get('url')): i for i, r in enumerate(recs)}
    ids = {r['id'] for r in recs}

    def new_id(date):
        d = (date or '00000000').replace('-', '')[:8]
        n = 1
        while f'NEWS-{d}-{slug}-{n}' in ids:
            n += 1
        nid = f'NEWS-{d}-{slug}-{n}'
        ids.add(nid)
        return nid

    replaced = added = 0
    bad = 0
    for f in args:
        for r in json.load(open(f)):
            p = check(r)
            if p:
                bad += 1
                print('PROBLEM', r.get('url'), p)
                continue
            k = norm(r.get('url'))
            if k in by_url:
                i = by_url[k]
                old = recs[i]
                rid = old['id']  # always keep the existing id so citations keep resolving
                r = {'id': rid, **{x: y for x, y in r.items() if x != 'id'}}
                if old.get('access') != 'full':
                    r['access_note'] = (r.get('access_note', '') + f" Upgraded from a {old.get('access')} record (id kept so existing references still resolve).").strip()
                recs[i] = r
                replaced += 1
            else:
                r = {'id': new_id(r.get('date')), **{x: y for x, y in r.items() if x != 'id'}}
                recs.append(r)
                by_url[k] = len(recs) - 1
                added += 1
    print(f'replaced {replaced}, added {added}, problems {bad}, total {len(recs)}')
    if write and not bad:
        def ordered(r):
            out = {k: r[k] for k in KEY_ORDER if k in r}
            out.update({k: v for k, v in r.items() if k not in out})
            return out
        with INDEX.open('w') as fh:
            for r in recs:
                fh.write(json.dumps(ordered(r), ensure_ascii=False) + '\n')
        print('written', INDEX)
    elif write:
        print('not written: fix problems first')


if __name__ == '__main__':
    main()
