
from classes import C, Obj
import prims


def test_make_funcs():
    obj = prims.make_special(C.TDOT)

    assert obj.typ == C.TSPECIAL
    assert obj.subtype == C.TDOT


def test_cons():
    obj1 = prims.make_special(1)
    obj2 = prims.make_special(2)
    obj3 = prims.cons(obj1, obj2)

    assert obj3.typ == C.TCELL
    assert obj3.car == obj1
    assert obj3.cdr == obj2


def test_acons():
    obj1 = prims.make_special(1)
    obj2 = prims.make_special(2)
    obj3 = prims.make_special(3)
    obj4 = prims.acons(obj1, obj2, obj3)

    pair = obj4.car
    val = obj4.cdr

    assert pair.car == obj1
    assert pair.cdr == obj2
    assert val == obj3


def dummy(obj1: Obj, obj2: Obj) -> Obj:
    return prims.make_special(1)


def test_make_primitive():
    obj = prims.make_primitive(dummy)
    obj1 = prims.make_special(1)
    obj2 = prims.make_special(2)
    obj.fn(obj1, obj2)


def test_make_symbol():
    obj = prims.make_symbol('mysym')
    assert obj.name == 'mysym'
