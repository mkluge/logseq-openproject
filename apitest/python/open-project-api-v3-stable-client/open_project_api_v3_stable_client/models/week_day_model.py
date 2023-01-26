from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.week_day_model_type import WeekDayModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.week_day_self_link_model import WeekDaySelfLinkModel


T = TypeVar("T", bound="WeekDayModel")


@attr.s(auto_attribs=True)
class WeekDayModel:
    """
    Example:
        {'_type': 'WeekDay', 'day': 5, 'name': 'Friday', 'working': False, '_links': {'self': {'href':
            '/api/v3/day/week/5', 'title': 'Friday'}}}

    Attributes:
        field_type (WeekDayModelType):
        day (int): The week day from 1 to 7. 1 is Monday. 7 is Sunday.
        name (str): The week day name.
        working (bool): `true` for a working week day, `false` otherwise.
        field_links (Union[Unset, WeekDaySelfLinkModel]): Identify a particular week day by its href. Example: {'self':
            {'href': '/api/v3/days/week/3', 'title': 'Wednesday'}}.
    """

    field_type: WeekDayModelType
    day: int
    name: str
    working: bool
    field_links: Union[Unset, "WeekDaySelfLinkModel"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type.value

        day = self.day
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
                "day": day,
                "name": name,
                "working": working,
            }
        )
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.week_day_self_link_model import WeekDaySelfLinkModel

        d = src_dict.copy()
        field_type = WeekDayModelType(d.pop("_type"))

        day = d.pop("day")

        name = d.pop("name")

        working = d.pop("working")

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, WeekDaySelfLinkModel]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = WeekDaySelfLinkModel.from_dict(_field_links)

        week_day_model = cls(
            field_type=field_type,
            day=day,
            name=name,
            working=working,
            field_links=field_links,
        )

        week_day_model.additional_properties = d
        return week_day_model

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
