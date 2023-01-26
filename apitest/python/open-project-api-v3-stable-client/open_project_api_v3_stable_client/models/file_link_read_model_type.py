from enum import Enum


class FileLinkReadModelType(str, Enum):
    FILELINK = "FileLink"

    def __str__(self) -> str:
        return str(self.value)
