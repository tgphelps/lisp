#!/usr/bin/env python

from classes import Obj
from globals import g


def main() -> None:
    # XXX temp code
    g.nil = Obj(1)
    print('g.nil =', g.nil)


if __name__ == '__main__':
    main()
