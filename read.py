
import sys
from classes import Obj
from globals import g
import prims
import util


last_char = ''


def getchar() -> str:
    global last_char
    if last_char == '':
        return sys.stdin.read(1)
    else:
        c = last_char
        last_char = ''
        return c


def ungetc(c: str) -> None:
    global last_char
    assert last_char == ''
    last_char = c


def peek() -> str:
    c = getchar()
    ungetc(c)
    return c


def read():
    while True:
        c = getchar()
        if not c:
            return None
        if c in ' \n\r\t':
            continue
        if c == ')':
            return g.cparen
        if c == '.':
            return g.dot
        if c == ';':
            skip_line()
            continue
        if c == '\'':
            return read_quote()
        if c.isdigit():
            return prims.make_int(read_number(ord(c) - ord('0')))
        if c == '-':
            return prims.make_int(-read_number(0))
        if c.isalpha() or c in '+=!@#$%^&*':
            return read_symbol(c)
        if c == '(':
            # return read_list()
            util.error('Cannt read a list yet')
        util.error("Don't know how to handle %c", c)


def skip_line() -> None:
    while True:
        c = getchar()
        if (c is None) or (c == '\n'):
            return


def read_quote() -> Obj:
    sym = prims.intern('quote')
    return prims.cons(sym, prims.cons(read(), g.nil))


def read_number(val: int) -> int:
    while peek().isdigit():
        val = val * 10 + (ord(getchar()) - ord('0'))
    return val


MAX_SYMLEN = 100


def read_symbol(c: str) -> Obj:
    buf = c
    symlen = 1
    while peek().isalnum() or peek() == '-':
        if symlen >= MAX_SYMLEN:
            util.error('symbol too long')
        buf += getchar()
        symlen += 1
    return prims.intern(buf)
