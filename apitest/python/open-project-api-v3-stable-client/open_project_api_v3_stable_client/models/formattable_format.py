from enum import Enum


class FormattableFormat(str, Enum):
    PLAIN = "plain"
    MARKDOWN = "markdown"
    CUSTOM = "custom"

    def __str__(self) -> str:
        return str(self.value)
