import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_entry_model_links import TimeEntryModelLinks


T = TypeVar("T", bound="TimeEntryModel")


@attr.s(auto_attribs=True)
class TimeEntryModel:
    """
    Attributes:
        id (Union[Unset, int]): Time entries' id
        comment (Union[Unset, str]): A text provided by the user detailing the time entry
        spent_on (Union[Unset, datetime.date]): The date the expenditure is booked for
        hours (Union[Unset, datetime.date]): The time quantifying the expenditure
        created_at (Union[Unset, datetime.datetime]): The time the time entry was created
        updated_at (Union[Unset, datetime.datetime]): The time the time entry was last updated
        field_links (Union[Unset, TimeEntryModelLinks]):
    """

    id: Union[Unset, int] = UNSET
    comment: Union[Unset, str] = UNSET
    spent_on: Union[Unset, datetime.date] = UNSET
    hours: Union[Unset, datetime.date] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    field_links: Union[Unset, "TimeEntryModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        comment = self.comment
        spent_on: Union[Unset, str] = UNSET
        if not isinstance(self.spent_on, Unset):
            spent_on = self.spent_on.isoformat()

        hours: Union[Unset, str] = UNSET
        if not isinstance(self.hours, Unset):
            hours = self.hours.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if spent_on is not UNSET:
            field_dict["spentOn"] = spent_on
        if hours is not UNSET:
            field_dict["hours"] = hours
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.time_entry_model_links import TimeEntryModelLinks

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        comment = d.pop("comment", UNSET)

        _spent_on = d.pop("spentOn", UNSET)
        spent_on: Union[Unset, datetime.date]
        if isinstance(_spent_on, Unset):
            spent_on = UNSET
        else:
            spent_on = isoparse(_spent_on).date()

        _hours = d.pop("hours", UNSET)
        hours: Union[Unset, datetime.date]
        if isinstance(_hours, Unset):
            hours = UNSET
        else:
            hours = isoparse(_hours).date()

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

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, TimeEntryModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = TimeEntryModelLinks.from_dict(_field_links)

        time_entry_model = cls(
            id=id,
            comment=comment,
            spent_on=spent_on,
            hours=hours,
            created_at=created_at,
            updated_at=updated_at,
            field_links=field_links,
        )

        time_entry_model.additional_properties = d
        return time_entry_model

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
