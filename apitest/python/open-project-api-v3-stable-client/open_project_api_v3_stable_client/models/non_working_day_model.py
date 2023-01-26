import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.non_working_day_model_type import NonWorkingDayModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.non_working_day_model_links import NonWorkingDayModelLinks


T = TypeVar("T", bound="NonWorkingDayModel")


@attr.s(auto_attribs=True)
class NonWorkingDayModel:
    """
    Example:
        {'_type': 'NonWorkingDay', 'date': '2022-12-25', 'name': 'Christmas', '_links': {'self': {'href':
            '/api/v3/days/non_working/2022-12-25', 'title': 'Christmas'}}}

    Attributes:
        field_type (NonWorkingDayModelType):
        date (datetime.date): Date of the non-working day.
        name (str): Descriptive name for the non-working day.
        field_links (Union[Unset, NonWorkingDayModelLinks]):
    """

    field_type: NonWorkingDayModelType
    date: datetime.date
    name: str
    field_links: Union[Unset, "NonWorkingDayModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type.value

        date = self.date.isoformat()
        name = self.name
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
            }
        )
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.non_working_day_model_links import NonWorkingDayModelLinks

        d = src_dict.copy()
        field_type = NonWorkingDayModelType(d.pop("_type"))

        date = isoparse(d.pop("date")).date()

        name = d.pop("name")

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, NonWorkingDayModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = NonWorkingDayModelLinks.from_dict(_field_links)

        non_working_day_model = cls(
            field_type=field_type,
            date=date,
            name=name,
            field_links=field_links,
        )

        non_working_day_model.additional_properties = d
        return non_working_day_model

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
