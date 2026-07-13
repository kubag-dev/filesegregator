import shutil
from typing import TYPE_CHECKING

from directories.infrastructure.collections import SupportedFileTypes
from directories.infrastructure.validators import MoveValidator
from directories.infrastructure.create_directories import CreateDirectories

if TYPE_CHECKING:
    from pathlib import Path


class Move:
    def __init__(self, *, source: "Path") -> None:
        self.source = source

    def _resolve_file_type(self, *, file_name: str):
        pass

    def execute(self):
        MoveValidator(source=self.source).validate()
        # TODO: Depending on how the app grows consider using an orchestrator or include it at init
        created_directories: dict[str, "Path"] = CreateDirectories(
            source=self.source
        ).execute()

        for file in self.source.glob("*"):
            # TODO: encapsulate possible types into a single property or smth
            # TODO: create submethods for each file type or smth
            if file.suffix in {
                SupportedFileTypes.JPG.value,
                SupportedFileTypes.PNG.value,
                SupportedFileTypes.GIF.value,
                SupportedFileTypes.WEBP.value,
            }:
                new_dir = created_directories["images"] / file.name
                shutil.move(file, new_dir)

            elif file.suffix in {
                SupportedFileTypes.MP4.value,
                SupportedFileTypes.MOV.value,
            }:
                new_dir = created_directories["videos"] / file.name
                shutil.move(file, new_dir)

            elif file.suffix in {
                SupportedFileTypes.TXT.value,
                SupportedFileTypes.ODT.value,
                SupportedFileTypes.PDF.value,
                SupportedFileTypes.DOCX.value,
            }:
                new_dir = created_directories["documents"] / file.name
                shutil.move(file, new_dir)

            elif file.suffix in {
                SupportedFileTypes.CSV.value,
                SupportedFileTypes.XLSX.value,
                SupportedFileTypes.XML.value,
                SupportedFileTypes.JSON.value,
            }:
                new_dir = created_directories["sheets"] / file.name
                shutil.move(file, new_dir)

            elif file.suffix in set(SupportedFileTypes.HTML.value):
                new_dir = created_directories["web_files"] / file.name
                shutil.move(file, new_dir)

            elif file.suffix in {
                SupportedFileTypes.ZIP.value,
                SupportedFileTypes.SEVEN_Z.value,
                SupportedFileTypes.RAR.value,
                SupportedFileTypes.GZ.value,
            }:
                new_dir = created_directories["archives"] / file.name
                shutil.move(file, new_dir)

            elif file.suffix in set(SupportedFileTypes.EXE.value):
                new_dir = created_directories["executables"] / file.name
                shutil.move(file, new_dir)

            elif file.suffix in {
                SupportedFileTypes.MP3.value,
                SupportedFileTypes.FLAC.value,
                SupportedFileTypes.WAV.value,
            }:
                new_dir = created_directories["audio"] / file.name
                shutil.move(file, new_dir)

            else:
                continue
