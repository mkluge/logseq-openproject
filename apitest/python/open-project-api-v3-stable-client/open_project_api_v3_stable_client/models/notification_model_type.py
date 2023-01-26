from enum import Enum


class NotificationModelType(str, Enum):
    NOTIFICATION = "Notification"

    def __str__(self) -> str:
        return str(self.value)
