from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.day_model_links_week_day import DayModelLinksWeekDay
    from ..models.link import Link


T = TypeVar("T", bound="DayModelLinks")


@attr.s(auto_attribs=True)
class DayModelLinks:
    """
    Attributes:
        self_ (Link):  Example: {'href': '/api/v3/work_packages', 'method': 'POST'}.
        non_working_reasons (Union[Unset, List['Link']]): A list of resources describing why this day is a non-working
            day.
            Linked resources can be `NonWorkingDay` and `WeekDay` resources.
            This property is absent for working days.
        week_day (Union[Unset, DayModelLinksWeekDay]):
    """

    self_: "Link"
    non_working_reasons: Union[Unset, List["Link"]] = UNSET
    week_day: Union[Unset, "DayModelLinksWeekDay"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        non_working_reasons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.non_working_reasons, Unset):
            non_working_reasons = []
            for non_working_reasons_item_data in self.non_working_reasons:
                non_working_reasons_item = non_working_reasons_item_data.to_dict()

                non_working_reasons.append(non_working_reasons_item)

        week_day: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.week_day, Unset):
            week_day = self.week_day.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
            }
        )
        if non_working_reasons is not UNSET:
            field_dict["nonWorkingReasons"] = non_working_reasons
        if week_day is not UNSET:
            field_dict["weekDay"] = week_day

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.day_model_links_week_day import DayModelLinksWeekDay
        from ..models.link import Link

        d = src_dict.copy()
        self_ = Link.from_dict(d.pop("self"))

        non_working_reasons = []
        _non_working_reasons = d.pop("nonWorkingReasons", UNSET)
        for non_working_reasons_item_data in _non_working_reasons or []:
            non_working_reasons_item = Link.from_dict(non_working_reasons_item_data)

            non_working_reasons.append(non_working_reasons_item)

        _week_day = d.pop("weekDay", UNSET)
        week_day: Union[Unset, DayModelLinksWeekDay]
        if isinstance(_week_day, Unset):
            week_day = UNSET
        else:
            week_day = DayModelLinksWeekDay.from_dict(_week_day)

        day_model_links = cls(
            self_=self_,
            non_working_reasons=non_working_reasons,
            week_day=week_day,
        )

        day_model_links.additional_properties = d
        return day_model_links

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
