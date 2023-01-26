from enum import Enum


class NonWorkingDayModelType(str, Enum):
    NONWORKINGDAY = "NonWorkingDay"

    def __str__(self) -> str:
        return str(self.value)
