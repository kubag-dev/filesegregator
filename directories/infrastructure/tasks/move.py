import shutil
from typing import TYPE_CHECKING

from directories.infrastructure.collections import SupportedFileTypes
from directories.infrastructure.validators import MoveValidator
from directories.infrastructure.tasks.create_directories import CreateDirectories

if TYPE_CHECKING:
    from pathlib import Path


class Move:
    def __init__(self, *, source: "Path") -> None:
        self.source = source

    def _resolve_file_type(self, *, file_name: str):
        pass

    def execute(self):
        MoveValidator(source=self.source).validate()
        # TODO: Definitely pass a folder structure through method/init
        # TODO: Move move.py and create_directories.py to common folder
        # as they carry out given task
        created_directories: dict[str, "Path"] = CreateDirectories(
            source=self.source
        ).execute()

        for file in self.source.glob("*"):
            if file.suffix in SupportedFileTypes.picture_types():
                new_dir = created_directories["images"] / file.name
                shutil.move(file, new_dir)

            elif file.suffix in SupportedFileTypes.audio_types():
                new_dir = created_directories["videos"] / file.name
                shutil.move(file, new_dir)

            elif file.suffix in SupportedFileTypes.document_types():
                new_dir = created_directories["documents"] / file.name
                shutil.move(file, new_dir)

            elif file.suffix in SupportedFileTypes.sheets_types():
                new_dir = created_directories["sheets"] / file.name
                shutil.move(file, new_dir)

            elif file.suffix in SupportedFileTypes.web_types():
                new_dir = created_directories["web_files"] / file.name
                shutil.move(file, new_dir)

            elif file.suffix in SupportedFileTypes.archive_types():
                new_dir = created_directories["archives"] / file.name
                shutil.move(file, new_dir)

            elif file.suffix in SupportedFileTypes.executable_types():
                new_dir = created_directories["executables"] / file.name
                shutil.move(file, new_dir)

            elif file.suffix in SupportedFileTypes.audio_types():
                new_dir = created_directories["audio"] / file.name
                shutil.move(file, new_dir)

            else:
                continue
