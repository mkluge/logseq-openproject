from enum import Enum


class SchemaModelType(str, Enum):
    SCHEMA = "Schema"

    def __str__(self) -> str:
        return str(self.value)
