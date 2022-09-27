
class Obj:
    def __init__(self, typ: int):
        self.typ: int = typ
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
