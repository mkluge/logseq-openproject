from enum import Enum


class WeekDayCollectionWriteModelType(str, Enum):
    COLLECTION = "Collection"

    def __str__(self) -> str:
        return str(self.value)
