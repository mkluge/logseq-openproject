from enum import Enum


class StorageModelType(str, Enum):
    STORAGE = "Storage"

    def __str__(self) -> str:
        return str(self.value)
