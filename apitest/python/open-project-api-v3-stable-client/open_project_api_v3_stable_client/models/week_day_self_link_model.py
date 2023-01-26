from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.week_day_self_link_model_self import WeekDaySelfLinkModelSelf


T = TypeVar("T", bound="WeekDaySelfLinkModel")


@attr.s(auto_attribs=True)
class WeekDaySelfLinkModel:
    """Identify a particular week day by its href.

    Example:
        {'self': {'href': '/api/v3/days/week/3', 'title': 'Wednesday'}}

    Attributes:
        self_ (Union[Unset, WeekDaySelfLinkModelSelf]):
    """

    self_: Union[Unset, "WeekDaySelfLinkModelSelf"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.week_day_self_link_model_self import WeekDaySelfLinkModelSelf

        d = src_dict.copy()
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, WeekDaySelfLinkModelSelf]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = WeekDaySelfLinkModelSelf.from_dict(_self_)

        week_day_self_link_model = cls(
            self_=self_,
        )

        week_day_self_link_model.additional_properties = d
        return week_day_self_link_model

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
