from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="NotificationSettingsModelItemLinksProject")


@attr.s(auto_attribs=True)
class NotificationSettingsModelItemLinksProject:
    """
    Attributes:
        href (str):
    """

    href: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "href": href,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        href = d.pop("href")

        notification_settings_model_item_links_project = cls(
            href=href,
        )

        notification_settings_model_item_links_project.additional_properties = d
        return notification_settings_model_item_links_project

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
