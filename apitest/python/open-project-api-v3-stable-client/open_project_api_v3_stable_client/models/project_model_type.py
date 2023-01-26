from enum import Enum


class ProjectModelType(str, Enum):
    PROJECT = "Project"

    def __str__(self) -> str:
        return str(self.value)
