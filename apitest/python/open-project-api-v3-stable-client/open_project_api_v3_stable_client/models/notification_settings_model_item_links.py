from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.notification_settings_model_item_links_project import NotificationSettingsModelItemLinksProject


T = TypeVar("T", bound="NotificationSettingsModelItemLinks")


@attr.s(auto_attribs=True)
class NotificationSettingsModelItemLinks:
    """
    Attributes:
        project (NotificationSettingsModelItemLinksProject):
    """

    project: "NotificationSettingsModelItemLinksProject"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project = self.project.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project": project,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notification_settings_model_item_links_project import NotificationSettingsModelItemLinksProject

        d = src_dict.copy()
        project = NotificationSettingsModelItemLinksProject.from_dict(d.pop("project"))

        notification_settings_model_item_links = cls(
            project=project,
        )

        notification_settings_model_item_links.additional_properties = d
        return notification_settings_model_item_links

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
