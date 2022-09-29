
import sys
from typing import NoReturn


def error(msg: str, *args) -> NoReturn:
    print(msg % args, file=sys.stderr)
    sys.exit(1)
