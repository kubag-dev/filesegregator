import shutil
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
        original_source = self.source.copy()
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

        for file in original_source.glob():
            # TODO: encapsulate possible types into a single property or smth
            # TODO: create submethods for each file type or smth
            if file.suffix in {
                SupportedFileTypes.JPG.value,
                SupportedFileTypes.PNG.value,
                SupportedFileTypes.GIF.value,
                SupportedFileTypes.WEBP.value,
            }:
                new_dir = images / file.name
                shutil.move(file, new_dir)

            elif file.suffix in {
                SupportedFileTypes.MP4.value,
                SupportedFileTypes.MOV.value,
            }:
                new_dir = videos / file.name
                shutil.move(file, new_dir)

            elif file.suffix in {
                SupportedFileTypes.TXT.value,
                SupportedFileTypes.ODT.value,
                SupportedFileTypes.PDF.value,
                SupportedFileTypes.DOCX.value,
            }:
                new_dir = documents / file.name
                shutil.move(file, new_dir)

            elif file.suffix in {
                SupportedFileTypes.CSV.value,
                SupportedFileTypes.XLSX.value,
                SupportedFileTypes.XML.value,
                SupportedFileTypes.JSON.value,
            }:
                new_dir = sheets / file.name
                shutil.move(file, new_dir)

            elif file.suffix in set(SupportedFileTypes.HTML.value):
                new_dir = web_files / file.name
                shutil.move(file, new_dir)

            elif file.suffix in {
                SupportedFileTypes.ZIP.value,
                SupportedFileTypes.SEVEN_Z.value,
                SupportedFileTypes.RAR.value,
                SupportedFileTypes.GZ.value,
            }:
                new_dir = archives / file.name
                shutil.move(file, new_dir)

            elif file.suffix in set(SupportedFileTypes.EXE.value):
                new_dir = executables / file.name
                shutil.move(file, new_dir)

            elif file.suffix in {
                SupportedFileTypes.MP3.value,
                SupportedFileTypes.FLAC.value,
                SupportedFileTypes.WAV.value,
            }:
                new_dir = audio / file.name
                shutil.move(file, new_dir)

            else:
                continue
