from enum import Enum


class ValuesPropertyModelType(str, Enum):
    VALUESPROPERTY = "Values::Property"

    def __str__(self) -> str:
        return str(self.value)
