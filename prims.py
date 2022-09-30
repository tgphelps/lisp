
# Various constructors

from typing import Optional, Callable
from classes import Obj, C


def make_special(n: int) -> Obj:
    obj = Obj(C.TSPECIAL)
    obj.subtype = n
    return obj


def make_env(vars: Obj, up: Optional[Obj]) -> Obj:
    obj = Obj(C.TENV)
    obj.vars = vars
    obj.up = up
    return obj


def make_primitive(fn: Callable[[Obj, Obj], Obj]) -> Obj:
    obj = Obj(C.TPRIMITIVE)
    obj.fn = fn
    return obj


def make_symbol(name: str) -> Obj:
    obj = Obj(C.TSYMBOL)
    obj.name = name
    return obj


def cons(car: Obj, cdr: Optional[Obj]) -> Obj:
    obj = Obj(C.TCELL)
    obj.car = car
    obj.cdr = cdr
    return obj


def acons(x: Obj, y: Obj, a: Obj) -> Obj:
    return cons(cons(x, y), a)


def add_variable(env: Obj, sym: Obj, val: Obj) -> None:
    env.vars = acons(sym, val, env.vars)
