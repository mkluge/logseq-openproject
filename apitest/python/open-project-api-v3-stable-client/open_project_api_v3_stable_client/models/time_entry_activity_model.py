import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_entry_activity_model_links import TimeEntryActivityModelLinks


T = TypeVar("T", bound="TimeEntryActivityModel")


@attr.s(auto_attribs=True)
class TimeEntryActivityModel:
    """
    Attributes:
        id (Union[Unset, int]): Time entries' id
        name (Union[Unset, str]): The human readable name chosen for this activity
        position (Union[Unset, datetime.date]): The rank the activity has in a list of activities
        default (Union[Unset, bool]): Flag to signal whether this activity is the default activity
        field_links (Union[Unset, TimeEntryActivityModelLinks]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    position: Union[Unset, datetime.date] = UNSET
    default: Union[Unset, bool] = UNSET
    field_links: Union[Unset, "TimeEntryActivityModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        position: Union[Unset, str] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.isoformat()

        default = self.default
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if position is not UNSET:
            field_dict["position"] = position
        if default is not UNSET:
            field_dict["default"] = default
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.time_entry_activity_model_links import TimeEntryActivityModelLinks

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _position = d.pop("position", UNSET)
        position: Union[Unset, datetime.date]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = isoparse(_position).date()

        default = d.pop("default", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, TimeEntryActivityModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = TimeEntryActivityModelLinks.from_dict(_field_links)

        time_entry_activity_model = cls(
            id=id,
            name=name,
            position=position,
            default=default,
            field_links=field_links,
        )

        time_entry_activity_model.additional_properties = d
        return time_entry_activity_model

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
