
from classes import Obj, C


def test_obj_class():
    obj = Obj(C.TCELL)
    assert obj.typ == C.TCELL
    assert str(obj) == 'Obj(2)'
