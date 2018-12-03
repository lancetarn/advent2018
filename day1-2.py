#!/usr/bin/env python3
import sys
import itertools


def main():
    seen = {}
    freq = 0
    for l in itertools.cycle(sys.stdin):
        freq += int(l)
        seen.setdefault(freq, 0)
        seen[freq] += 1
        if seen[freq] > 1:
            print(freq)
            return


if __name__ == '__main__':
    main()
