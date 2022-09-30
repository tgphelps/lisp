
from classes import C
from globals import g
import prims


# XXX This doesn't really test anything in lisp.py

def test_intern():
    g.nil = prims.make_special(C.TNIL)
    g.symbols = g.nil

    prims.intern('mysym1')
    prims.intern('mysym2')
    prims.intern('mysym3')

    dump_symbols()


def dump_symbols():
    print('SYMBOLS:')
    sym = g.symbols
    while sym != g.nil:
        assert sym.typ == C.TCELL
        print(f'symbol: {sym.car}')
        sym = sym.cdr
    print("Symbols OK")
