from typing import TYPE_CHECKING

from directories.infrastructure.validators import MoveValidator

if TYPE_CHECKING:
    from pathlib import Path

class Move:
    def __init__(self, *, source: "Path") -> None:
        self.source = source

    def execute():
        pass