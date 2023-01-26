from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.week_day_write_model_type import WeekDayWriteModelType

T = TypeVar("T", bound="WeekDayWriteModel")


@attr.s(auto_attribs=True)
class WeekDayWriteModel:
    """Describes a week day as a working day or a non-working day (weekend).

    Example:
        {'_type': 'WeekDay', 'working': False}

    Attributes:
        field_type (WeekDayWriteModelType):
        working (bool): `true` for a working day. `false` for a weekend day.
    """

    field_type: WeekDayWriteModelType
    working: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type.value

        working = self.working

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_type": field_type,
                "working": working,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_type = WeekDayWriteModelType(d.pop("_type"))

        working = d.pop("working")

        week_day_write_model = cls(
            field_type=field_type,
            working=working,
        )

        week_day_write_model.additional_properties = d
        return week_day_write_model

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
