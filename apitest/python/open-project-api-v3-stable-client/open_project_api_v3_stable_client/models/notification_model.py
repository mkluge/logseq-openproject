import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.notification_model_reason import NotificationModelReason
from ..models.notification_model_type import NotificationModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_model_embedded import NotificationModelEmbedded
    from ..models.notification_model_links import NotificationModelLinks
    from ..models.values_property_model import ValuesPropertyModel


T = TypeVar("T", bound="NotificationModel")


@attr.s(auto_attribs=True)
class NotificationModel:
    """
    Attributes:
        field_type (Union[Unset, NotificationModelType]):
        id (Union[Unset, int]): Notification id
        reason (Union[Unset, NotificationModelReason]): The reason for the notification
        read_ian (Union[Unset, bool]): Whether the notification is marked as read
        details (Union[Unset, List['ValuesPropertyModel']]): A list of objects including detailed information about the
            notification.
        created_at (Union[Unset, datetime.datetime]): The time the notification was created at
        updated_at (Union[Unset, datetime.datetime]): The time the notification was last updated
        field_embedded (Union[Unset, NotificationModelEmbedded]):
        field_links (Union[Unset, NotificationModelLinks]):
    """

    field_type: Union[Unset, NotificationModelType] = UNSET
    id: Union[Unset, int] = UNSET
    reason: Union[Unset, NotificationModelReason] = UNSET
    read_ian: Union[Unset, bool] = UNSET
    details: Union[Unset, List["ValuesPropertyModel"]] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    field_embedded: Union[Unset, "NotificationModelEmbedded"] = UNSET
    field_links: Union[Unset, "NotificationModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type: Union[Unset, str] = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value

        id = self.id
        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        read_ian = self.read_ian
        details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()

                details.append(details_item)

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_embedded: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_type is not UNSET:
            field_dict["_type"] = field_type
        if id is not UNSET:
            field_dict["id"] = id
        if reason is not UNSET:
            field_dict["reason"] = reason
        if read_ian is not UNSET:
            field_dict["readIAN"] = read_ian
        if details is not UNSET:
            field_dict["details"] = details
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notification_model_embedded import NotificationModelEmbedded
        from ..models.notification_model_links import NotificationModelLinks
        from ..models.values_property_model import ValuesPropertyModel

        d = src_dict.copy()
        _field_type = d.pop("_type", UNSET)
        field_type: Union[Unset, NotificationModelType]
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = NotificationModelType(_field_type)

        id = d.pop("id", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, NotificationModelReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = NotificationModelReason(_reason)

        read_ian = d.pop("readIAN", UNSET)

        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = ValuesPropertyModel.from_dict(details_item_data)

            details.append(details_item)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, NotificationModelEmbedded]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = NotificationModelEmbedded.from_dict(_field_embedded)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, NotificationModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = NotificationModelLinks.from_dict(_field_links)

        notification_model = cls(
            field_type=field_type,
            id=id,
            reason=reason,
            read_ian=read_ian,
            details=details,
            created_at=created_at,
            updated_at=updated_at,
            field_embedded=field_embedded,
            field_links=field_links,
        )

        notification_model.additional_properties = d
        return notification_model

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
