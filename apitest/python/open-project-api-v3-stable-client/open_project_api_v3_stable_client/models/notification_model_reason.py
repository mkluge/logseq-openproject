from enum import Enum


class NotificationModelReason(str, Enum):
    ASSIGNED = "assigned"
    COMMENTED = "commented"
    CREATED = "created"
    DATEALERT = "dateAlert"
    MENTIONED = "mentioned"
    PRIORITIZED = "prioritized"
    PROCESSED = "processed"
    RESPONSIBLE = "responsible"
    SUBSCRIBED = "subscribed"
    SCHEDULED = "scheduled"
    WATCHED = "watched"

    def __str__(self) -> str:
        return str(self.value)
