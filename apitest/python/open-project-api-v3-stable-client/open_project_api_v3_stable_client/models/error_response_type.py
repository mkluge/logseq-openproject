from enum import Enum


class ErrorResponseType(str, Enum):
    ERROR = "Error"

    def __str__(self) -> str:
        return str(self.value)
