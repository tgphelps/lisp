
from dataclasses import dataclass

from classes import Obj


@dataclass
class Globals:
    nil: Obj
    dot: Obj
    cparen: Obj
    true: Obj

    symbols: Obj


g = Globals
