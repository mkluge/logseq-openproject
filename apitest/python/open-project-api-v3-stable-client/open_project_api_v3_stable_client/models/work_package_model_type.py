from enum import Enum


class WorkPackageModelType(str, Enum):
    WORKPACKAGE = "WorkPackage"

    def __str__(self) -> str:
        return str(self.value)
