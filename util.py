
import sys
from typing import NoReturn


def error(msg: str, *args) -> NoReturn:
    msg = 'ERROR: ' + msg
    print(msg % args, file=sys.stderr)
    sys.exit(1)
