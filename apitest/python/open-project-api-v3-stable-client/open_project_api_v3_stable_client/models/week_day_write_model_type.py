from enum import Enum


class WeekDayWriteModelType(str, Enum):
    WEEKDAY = "WeekDay"

    def __str__(self) -> str:
        return str(self.value)
