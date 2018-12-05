#!/usr/bin/env python3
import sys
import typing
from collections import Counter


class Claim(typing.NamedTuple):
    ref: int
    anchor: tuple
    height: int
    width: int


def main():
    claimed = Counter()
    for line in sys.stdin:
        # print(line)
        claim = parse_claim(line.strip())
        claimed.update(get_points(claim))

    print(len([v for v in claimed.values() if v > 1]))


def parse_claim(line):
    ref, _, anchor, dimension = line.split()
    ref = int(ref.strip('#'))
    width, height = dimension.split('x')
    width, height = int(width), int(height)
    anchor = anchor.strip(':').split(',')
    anchor = (int(anchor[0]), int(anchor[1]))
    return Claim(ref, anchor, height, width)


def get_points(claim):
    x_, y_ = claim.anchor
    points = []
    for x in range(x_ + 1, x_ + claim.width + 1):
        for y in range(y_ + 1, y_ + claim.height + 1):
            points.append((x, y))
    # print(repr(claim))
    # print(points)
    # print(len(points))
    # sys.exit()

    return points


if __name__ == '__main__':
    main()
