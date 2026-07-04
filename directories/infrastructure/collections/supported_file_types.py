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

    # TODO: consider how to do directories

    # TODO: consider property methods with each group
