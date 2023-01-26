from enum import Enum


class UserModelType(str, Enum):
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
