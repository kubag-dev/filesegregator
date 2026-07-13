from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


class CreateDirectories:
    def __init__(self, *, source: "Path") -> None:
        self.source = source

    def execute(self) -> dict[str, "Path"]:
        # TODO: consider using a typed dict instead of generic string and Path combo
        path_map: dict[str, "Path"] = {}
        self.source = self.source / "segregated"
        self.source.mkdir(parents=True, exist_ok=True)
        path_map["source"] = self.source

        images = self.source / "images"
        images.mkdir(parents=True, exist_ok=True)
        path_map["images"] = images

        videos = self.source / "videos"
        videos.mkdir(parents=True, exist_ok=True)
        path_map["videos"] = videos

        documents = self.source / "documents"
        documents.mkdir(parents=True, exist_ok=True)
        path_map["documents"] = documents

        sheets = self.source / "sheets"
        sheets.mkdir(parents=True, exist_ok=True)
        path_map["sheets"] = sheets

        web_files = self.source / "web_files"
        web_files.mkdir(parents=True, exist_ok=True)
        path_map["web_files"] = web_files

        archives = self.source / "archives"
        archives.mkdir(parents=True, exist_ok=True)
        path_map["archives"] = archives

        executables = self.source / "executables"
        executables.mkdir(parents=True, exist_ok=True)
        path_map["executables"] = executables

        audio = self.source / "audio"
        audio.mkdir(parents=True, exist_ok=True)
        path_map["audio"] = audio

        directories = self.source / "directories"
        directories.mkdir(parents=True, exist_ok=True)
        # TODO: INCLUDE

        others = self.source / "others"
        others.mkdir(parents=True, exist_ok=True)
        # TODO: INCLUDE

        return path_map
