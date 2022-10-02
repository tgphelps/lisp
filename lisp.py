#!/usr/bin/env python

from typing import Optional
from globals import g
from classes import Obj, C
import prims
import read
import util


Symbols: Optional[Obj] = None


def main() -> int:
    g.nil = prims.make_special(C.TNIL)
    g.dot = prims.make_special(C.TDOT)
    g.cparen = prims.make_special(C.TCPAREN)
    g.true = prims.make_special(C.TTRUE)
    g.symbols = g.nil

    env = prims.make_env(g.nil, None)
    define_constants(env)
    define_primitivess(env)

    while True:
        expr = read.read()
        if not expr:
            print('EOF')
            return 0
        if expr == g.cparen:
            util.error("Stray close parenthesis")
        if expr == g.dot:
            util.error("Stray dot")
        oprint(eval(env, expr))
        print()


def define_constants(env: Obj) -> None:
    sym = prims.intern("t")
    prims.add_variable(env, sym, g.true)


def define_primitivess(env: Obj) -> None:
    print('FIXME: define_primitivess')
    prims.add_primitive(env, "quote", prims.dummy_prim)
    prims.add_primitive(env, "list", prims.dummy_prim)
    prims.add_primitive(env, "setq", prims.dummy_prim)
    prims.add_primitive(env, "+", prims.dummy_prim)
    prims.add_primitive(env, "define", prims.dummy_prim)
    prims.add_primitive(env, "defun", prims.dummy_prim)
    prims.add_primitive(env, "defmacro", prims.dummy_prim)
    prims.add_primitive(env, "macroexpand", prims.dummy_prim)
    prims.add_primitive(env, "lambda", prims.dummy_prim)
    prims.add_primitive(env, "if", prims.dummy_prim)
    prims.add_primitive(env, "=", prims.dummy_prim)
    prims.add_primitive(env, "println", prims.dummy_prim)
    prims.add_primitive(env, "exit", prims.dummy_prim)


def eval(env: Obj, obj: Obj) -> Obj:
    if obj.typ in (C.TINT, C.TPRIMITIVE, C.TFUNCTION, C.TSPECIAL):
        return obj
    elif obj.typ == C.TSYMBOL:
        bind = prims.find(env, obj)
        if bind is None:
            util.error(f'undefined symbol: {obj.name}')
        return bind.cdr
    elif obj.typ == C.TCELL:
        util.error('eval cannot do functions yet')
    else:
        util.error('eval caanot get here')


def oprint(obj: Obj) -> None:
    if obj.typ == C.TINT:
        print(f'{obj.value}', end='')
    elif obj.typ == C.TSYMBOL:
        print(f'{obj.name}', end='')
    elif obj.typ == C.TPRIMITIVE:
        print('<primitive>', end='')
    elif obj.typ == C.TFUNCTION:
        print('<function>', end='')
    elif obj.typ == C.TMACRO:
        print('<macro>', end='')
    elif obj.typ == C.TCELL:
        print('ERR: cell', end='')
    elif obj.typ == C.TSPECIAL:
        if obj == g.nil:
            print('()', end='')
        elif obj == g.true:
            print('t', end='')
        else:
            print('ERR: bad special', end='')
    else:
        util.error('oprint cannot get here')


if __name__ == '__main__':
    main()
