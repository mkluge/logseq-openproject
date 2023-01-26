import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.day_model_type import DayModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.day_model_links import DayModelLinks


T = TypeVar("T", bound="DayModel")


@attr.s(auto_attribs=True)
class DayModel:
    """
    Example:
        {'_type': 'Day', 'date': '2022-12-25', 'name': 'Sunday (Christmas)', 'working': False, '_links': {'self':
            {'href': '/api/v3/days/2022-12-25'}, 'nonWorkingReasons': [{'href': '/api/v3/days/week/7', 'title': 'Sunday'},
            {'href': '/api/v3/days/non_working/2022-12-25', 'title': 'Christmas'}], 'weekday': {'href':
            '/api/v3/days/week/7', 'title': 'Sunday'}}}

    Attributes:
        field_type (DayModelType):
        date (datetime.date): Date of the day.
        name (str): Descriptive name for the day.
        working (bool): `true` for a working day, `false` otherwise.
        field_links (Union[Unset, DayModelLinks]):
    """

    field_type: DayModelType
    date: datetime.date
    name: str
    working: bool
    field_links: Union[Unset, "DayModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type.value

        date = self.date.isoformat()
        name = self.name
        working = self.working
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_type": field_type,
                "date": date,
                "name": name,
                "working": working,
            }
        )
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.day_model_links import DayModelLinks

        d = src_dict.copy()
        field_type = DayModelType(d.pop("_type"))

        date = isoparse(d.pop("date")).date()

        name = d.pop("name")

        working = d.pop("working")

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, DayModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = DayModelLinks.from_dict(_field_links)

        day_model = cls(
            field_type=field_type,
            date=date,
            name=name,
            working=working,
            field_links=field_links,
        )

        day_model.additional_properties = d
        return day_model

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
