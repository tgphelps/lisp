#!/usr/bin/env python


from typing import Optional
from globals import g
from classes import Obj, C
import prims
import util


def main() -> int:
    g.nil = prims.make_special(C.TNIL)
    g.dot = prims.make_special(C.TDOT)
    g.cparen = prims.make_special(C.TCPAREN)
    g.true = prims.make_special(C.TTRUE)
    g.symbols = g.nil

    env: Obj = prims.make_env(g.nil, None)
    define_constants(env)
    define_primitivess(env)

    while True:
        expr = read()
        if not expr:
            return 0
        if expr == g.cparen:
            util.error("Stray close parenthesis")
        if expr == g.dot:
            util.error("Stray dot")
        print(eval(env, expr))
        print()
        return 0  # XXX temp


def define_constants(env: Obj) -> None:
    print('TODO: define_constants')


def define_primitivess(env: Obj) -> None:
    print('TODO: define_primitivess')


def read() -> Optional[Obj]:
    print('TODO: read')
    return g.nil


def eval(env: Obj, expr: Obj) -> Obj:
    print('TODO: eval')
    return g.nil


def pprint(Obj) -> None:
    print('TODO: pprint')


if __name__ == '__main__':
    main()
