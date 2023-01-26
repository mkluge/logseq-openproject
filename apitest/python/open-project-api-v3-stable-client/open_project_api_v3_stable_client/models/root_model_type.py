from enum import Enum


class RootModelType(str, Enum):
    ROOT = "Root"

    def __str__(self) -> str:
        return str(self.value)
