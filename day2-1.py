#!/usr/bin/env python3
import sys
from collections import Counter


def main():
    twos, threes = 0, 0
    for l in sys.stdin:
        two, three = count_letters(l)
        twos += two
        threes += three
    print(twos * threes)


def count_letters(l):
    two, three = 0, 0
    c = Counter(l.strip())
    if 2 in c.values():
        two = 1
    if 3 in c.values():
        three = 1
    return two, three


if __name__ == '__main__':
    main()
