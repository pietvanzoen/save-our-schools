#!/usr/bin/env python3
"""Copy a freshly fetched tree into sources/ without ever losing an earlier original.

  python3 tools/safe_copy.py STAGING_ROOT [--dest sources] [--date YYYY-MM-DD] [--dry-run]

STAGING_ROOT mirrors sources/ (e.g. OUT/ containing boardbook/meetings/...). For each file:
- new path                    -> copied in
- exists and identical        -> skipped
- exists and different        -> the existing file is moved to <dir>/_prior/<name>.<date-of-old-file><ext>
                                 (its last-modified date, or 'before-<date>'), then the new file is copied in.
Every replacement is logged to sources/_versions_log.csv (path, prior_copy, sha256_old, sha256_new, date).
Nothing is ever deleted. Use this instead of plain cp when refreshing sources/.
"""
import argparse, csv, datetime, hashlib, os, shutil, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('staging')
    ap.add_argument('--dest', default=str(ROOT / 'sources'))
    ap.add_argument('--date', default=datetime.date.today().isoformat())
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    src, dst = pathlib.Path(a.staging), pathlib.Path(a.dest)
    log = ROOT / 'sources/_versions_log.csv'
    rows, n_new, n_same, n_rep = [], 0, 0, 0
    for f in sorted(p for p in src.rglob('*') if p.is_file()):
        rel = f.relative_to(src)
        d = dst / rel
        if not d.exists():
            n_new += 1
            if not a.dry_run:
                d.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, d)
            continue
        old, new = sha(d), sha(f)
        if old == new:
            n_same += 1
            continue
        n_rep += 1
        prior_dir = d.parent / '_prior'
        stamp = datetime.date.fromtimestamp(d.stat().st_mtime).isoformat()
        if stamp >= a.date:
            stamp = f'before-{a.date}'
        prior = prior_dir / f'{d.stem}.{stamp}{d.suffix}'
        i = 2
        while prior.exists():
            prior = prior_dir / f'{d.stem}.{stamp}-{i}{d.suffix}'
            i += 1
        print('REPLACED', rel, '-> prior kept at', prior.relative_to(dst))
        rows.append([str(d.relative_to(ROOT)), str(prior.relative_to(ROOT)), old, new, a.date])
        if not a.dry_run:
            prior_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(d), prior)
            shutil.copy2(f, d)
    if rows and not a.dry_run:
        new_log = not log.exists()
        with open(log, 'a', newline='') as fh:
            w = csv.writer(fh)
            if new_log:
                w.writerow(['path', 'prior_copy', 'sha256_old', 'sha256_new', 'date'])
            w.writerows(rows)
    print(f'new {n_new}, identical {n_same}, replaced (prior kept) {n_rep}')


if __name__ == '__main__':
    main()
