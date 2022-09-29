
from typing import Any, Optional, Callable


class Obj:
    subtype: int
    vars: Any
    up: Optional[Any]
    car: Any
    cdr: Any
    fn: Callable[[Any, Any], Any]
    name: str

    def __init__(self, typ: int):
        self.typ: int = typ

    def __repr__(self):
        return f'Obj({self.typ})'

    #
    # An Obj is like a C tagged union. 'typ' is the tag. There will be
    # some number of other fields in the Obj, depending on 'typ':
    # int -> value
    # cell -> car, cdr
    # symbol -> name
    # primitive -> fn
    # macro -> params, body, env
    # special -> subtype
    # environment frame -> vars, up


class C:
    # Object types
    TINT = 1
    TCELL = 2
    TSYMBOL = 3
    TPRIMITIVE = 4
    TFUNCTION = 5
    TMACRO = 6
    TSPECIAL = 7
    TENV = 8

    # Special types
    TNIL = 1
    TDOT = 2
    TCPAREN = 3
    TTRUE = 4
