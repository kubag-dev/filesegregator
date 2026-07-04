from typing import TYPE_CHECKING

from directories.infrastructure.collections import SupportedFileTypes
from directories.infrastructure.validators import MoveValidator

if TYPE_CHECKING:
    from pathlib import Path

class Move:
    def __init__(self, *, source: "Path") -> None:
        self.source = source

    def _resolve_file_type(self, *, file_name: str):
        pass 

    def execute(self):
        MoveValidator(source=self.source).validate()
        # TODO: move directory creation to other file
        self.source = self.source / "segregated"
        self.source.mkdir(parents=True, exist_ok=True)

        images = self.source / "images"
        images.mkdir(parents=True, exist_ok=True)

        videos = self.source / "videos"
        videos.mkdir(parents=True, exist_ok=True)

        documents = self.source / "documents"
        documents.mkdir(parents=True, exist_ok=True)

        sheets = self.source / "sheets"
        sheets.mkdir(parents=True, exist_ok=True)

        web_files = self.source / "web_files"
        web_files.mkdir(parents=True, exist_ok=True)

        archives = self.source / "archives"
        archives.mkdir(parents=True, exist_ok=True)

        executables = self.source / "executables"
        executables.mkdir(parents=True, exist_ok=True)

        audio = self.source / "audio"
        audio.mkdir(parents=True, exist_ok=True)

        directories = self.source / "directories"
        directories.mkdir(parents=True, exist_ok=True)

        others = self.source / "others"
        others.mkdir(parents=True, exist_ok=True)
