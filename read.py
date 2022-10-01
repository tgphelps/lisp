
import sys
from globals import g


def read():
    while True:
        c = sys.stdin.read(1)
        # Must handle:
        # whitespace
        # ';' comment
        # '(' list
        # '\'' quote
        # digit
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


def skip_line() -> None:
    while True:
        c = sys.stdin.read(1)
        if (c is None) or (c == '\n'):
            return
