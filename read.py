
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


def read_quote() -> Obj:
    sym = prims.intern('quote')
    return prims.cons(sym, prims.cons(read(), g.nil))


def read_number(val: int) -> int:
    while peek().isdigit():
        val = val * 10 + (ord(getchar()) - ord('0'))
    return val


def read():
    while True:
        c = getchar()
        # Must handle:
        # '(' list
        # '-' negative int
        # alpha or other symbol char
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
        util.error("Don't know how to handle %c", c)


def skip_line() -> None:
    while True:
        c = getchar()
        if (c is None) or (c == '\n'):
            return
