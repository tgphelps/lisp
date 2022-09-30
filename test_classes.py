
from classes import Obj, C
import prims


def test_obj_class():
    obj = Obj(C.TCELL)
    obj.car = prims.make_special(C.TDOT)
    obj.cdr = prims.make_special(C.TSYMBOL)
    assert obj.typ == C.TCELL
    # print(obj)
