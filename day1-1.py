#!/usr/bin/env python3
import sys
from functools import reduce
from operator import add


def main():
    in_ = sys.stdin.readlines()
    in_ = [int(l) for l in in_]
    print(reduce(add, in_, 0))


if __name__ == '__main__':
    main()
