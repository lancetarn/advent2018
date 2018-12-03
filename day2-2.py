#!/usr/bin/env python3
import sys


def main():
    ids = []
    for l in sys.stdin:
        w = l.strip()
        check_ids(w, ids)
        ids.append(w)
    print("oh no")
    sys.exit(1)


def check_ids(new, ids):
    for i in ids:
        hits = []
        for check, ref in zip(new, i):
            if check == ref:
                hits.append(check)
        if len(hits) == len(new) - 1:
            print(f"New: {new}")
            print(f"Ref: {i}")
            print(f"Hits: {''.join(hits)}")
            sys.exit(0)


if __name__ == '__main__':
    main()
