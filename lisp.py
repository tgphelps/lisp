#!/usr/bin/env python


from typing import Optional
from globals import g
from classes import Obj, C


def main() -> None:
    g.nil = make_special(C.TNIL)
    g.dot = make_special(C.TDOT)
    g.cparen = make_special(C.TCPAREN)
    g.true = make_special(C.TTRUE)
    g.symbols = g.nil

    env: Obj = make_env(g.nil, None)
    define_constants(env)
    define_primitivess(env)


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


if __name__ == '__main__':
    main()
