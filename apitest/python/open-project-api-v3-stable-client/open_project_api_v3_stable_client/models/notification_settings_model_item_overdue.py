from enum import Enum


class NotificationSettingsModelItemOverdue(str, Enum):
    VALUE_0 = ""
    P1D = "P1D"
    P3D = "P3D"
    P1W = "P1W"

    def __str__(self) -> str:
        return str(self.value)
