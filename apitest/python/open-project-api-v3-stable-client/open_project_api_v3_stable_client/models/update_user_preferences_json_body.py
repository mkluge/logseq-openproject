from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserPreferencesJsonBody")


@attr.s(auto_attribs=True)
class UpdateUserPreferencesJsonBody:
    """
    Example:
        {'autoHidePopups': True, 'timeZone': 'Europe/Paris'}

    Attributes:
        auto_hide_popups (Union[Unset, bool]):
        time_zone (Union[Unset, str]):
    """

    auto_hide_popups: Union[Unset, bool] = UNSET
    time_zone: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auto_hide_popups = self.auto_hide_popups
        time_zone = self.time_zone

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_hide_popups is not UNSET:
            field_dict["autoHidePopups"] = auto_hide_popups
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auto_hide_popups = d.pop("autoHidePopups", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        update_user_preferences_json_body = cls(
            auto_hide_popups=auto_hide_popups,
            time_zone=time_zone,
        )

        update_user_preferences_json_body.additional_properties = d
        return update_user_preferences_json_body

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
