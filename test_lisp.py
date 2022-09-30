
from classes import C
import lisp

def test_intern():
    lisp.intern('mysym1')
    lisp.intern('mysym2')
    lisp.intern('mysym3')

    sym = lisp.Symbols
    while sym is not None:
        assert sym.typ == C.TCELL
        print(f'symbol: {sym.car}')
        sym = sym.cdr
    print("Symbols OK")