from typing import TYPE_CHECKING

from directories.infrastructure.exceptions import SourceDirDoesNotExistException

if TYPE_CHECKING:
    from pathlib import Path


class MoveValidator:
    def __init__(self, *, source: "Path"):
        self.source = source

    def validate(self) -> None:
        if not self.source.exists():
            raise SourceDirDoesNotExistException()
