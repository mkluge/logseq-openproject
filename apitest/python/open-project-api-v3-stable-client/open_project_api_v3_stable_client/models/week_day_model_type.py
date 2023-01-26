from enum import Enum


class WeekDayModelType(str, Enum):
    WEEKDAY = "WeekDay"

    def __str__(self) -> str:
        return str(self.value)
