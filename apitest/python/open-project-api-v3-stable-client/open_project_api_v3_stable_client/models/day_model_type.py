from enum import Enum


class DayModelType(str, Enum):
    DAY = "Day"

    def __str__(self) -> str:
        return str(self.value)
