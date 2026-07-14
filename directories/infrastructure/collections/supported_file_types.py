from enum import StrEnum


class SupportedFileTypes(StrEnum):
    # Picture types
    JPG = ".jpg"
    PNG = ".png"
    WEBP = ".webp"
    GIF = ".gif"

    # Video types
    MP4 = ".mp4"
    MOV = ".mov"

    # Document types
    TXT = ".txt"
    ODT = ".odt"
    PDF = ".pdf"
    DOCX = ".docx"

    # Sheets types
    CSV = ".csv"
    XLSX = ".xlsx"
    XML = ".xml"
    JSON = ".json"

    # Web files
    HTML = ".html"

    # Archives
    ZIP = ".zip"
    SEVEN_Z = ".7z"
    RAR = ".rar"
    GZ = ".gz"

    # Executables
    EXE = ".exe"

    # Audio
    MP3 = ".mp3"
    FLAC = ".flac"
    WAV = ".wav"

    # Directories have been marked as a different type than file
    # as such it's considered a special case not included here

    @classmethod
    def picture_types(cls) -> set[str]:
        return {cls.JPG.value, cls.PNG.value, cls.WEBP.value, cls.GIF.value}

    @classmethod
    def video_types(cls) -> set[str]:
        return {cls.MP4.value, cls.MOV.value}

    @classmethod
    def document_types(cls) -> set[str]:
        return {cls.TXT.value, cls.ODT.value, cls.PDF.value, cls.DOCX.value}

    @classmethod
    def sheets_types(cls) -> set[str]:
        return {cls.CSV.value, cls.XLSX.value, cls.XML.value, cls.JSON.value}

    @classmethod
    def web_types(cls) -> set[str]:
        return {cls.HTML.value}

    @classmethod
    def archive_types(cls) -> set[str]:
        return {cls.ZIP.value, cls.SEVEN_Z.value, cls.RAR.value, cls.GZ.value}

    @classmethod
    def executable_types(cls) -> set[str]:
        return {cls.EXE.value}

    @classmethod
    def audio_types(cls) -> set[str]:
        return {cls.MP3.value, cls.FLAC.value, cls.WAV.value}
