#!/usr/bin/env python


from typing import Optional
from globals import g
from classes import Obj, C
import util


def main() -> int:
    g.nil = make_special(C.TNIL)
    g.dot = make_special(C.TDOT)
    g.cparen = make_special(C.TCPAREN)
    g.true = make_special(C.TTRUE)
    g.symbols = g.nil

    env: Obj = make_env(g.nil, None)
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
        break  # XXX temp


def make_special(n: int) -> Obj:
    obj = Obj(C.TSPECIAL)
    obj.subtype = n
    return obj


def make_env(vars: Obj, up: Optional[Obj]) -> Obj:
    obj = Obj(C.TENV)
    obj.vars = vars
    obj.up = up
    return obj


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
