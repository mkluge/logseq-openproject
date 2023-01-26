from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_settings_model_item import NotificationSettingsModelItem
    from ..models.user_preference_model_links import UserPreferenceModelLinks


T = TypeVar("T", bound="UserPreferenceModel")


@attr.s(auto_attribs=True)
class UserPreferenceModel:
    """
    Attributes:
        auto_hide_popups (Union[Unset, bool]): Whether to hide popups (e.g. success messages) after 5 seconds
        hide_mail (Union[Unset, bool]): Hide mail address from other users
        notifications (Union[Unset, List['NotificationSettingsModelItem']]): The settings for the notifications to be
            received by the user
        time_zone (Union[Unset, str]): Current selected time zone
        comment_sort_descending (Union[Unset, bool]): Sort comments in descending order
        warn_on_leaving_unsaved (Union[Unset, bool]): Issue warning when leaving a page with unsaved text
        field_links (Union[Unset, UserPreferenceModelLinks]):
    """

    auto_hide_popups: Union[Unset, bool] = UNSET
    hide_mail: Union[Unset, bool] = UNSET
    notifications: Union[Unset, List["NotificationSettingsModelItem"]] = UNSET
    time_zone: Union[Unset, str] = UNSET
    comment_sort_descending: Union[Unset, bool] = UNSET
    warn_on_leaving_unsaved: Union[Unset, bool] = UNSET
    field_links: Union[Unset, "UserPreferenceModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auto_hide_popups = self.auto_hide_popups
        hide_mail = self.hide_mail
        notifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = []
            for componentsschemas_notification_settings_model_item_data in self.notifications:
                componentsschemas_notification_settings_model_item = (
                    componentsschemas_notification_settings_model_item_data.to_dict()
                )

                notifications.append(componentsschemas_notification_settings_model_item)

        time_zone = self.time_zone
        comment_sort_descending = self.comment_sort_descending
        warn_on_leaving_unsaved = self.warn_on_leaving_unsaved
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_hide_popups is not UNSET:
            field_dict["autoHidePopups"] = auto_hide_popups
        if hide_mail is not UNSET:
            field_dict["hideMail"] = hide_mail
        if notifications is not UNSET:
            field_dict["notifications"] = notifications
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if comment_sort_descending is not UNSET:
            field_dict["commentSortDescending"] = comment_sort_descending
        if warn_on_leaving_unsaved is not UNSET:
            field_dict["warnOnLeavingUnsaved"] = warn_on_leaving_unsaved
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notification_settings_model_item import NotificationSettingsModelItem
        from ..models.user_preference_model_links import UserPreferenceModelLinks

        d = src_dict.copy()
        auto_hide_popups = d.pop("autoHidePopups", UNSET)

        hide_mail = d.pop("hideMail", UNSET)

        notifications = []
        _notifications = d.pop("notifications", UNSET)
        for componentsschemas_notification_settings_model_item_data in _notifications or []:
            componentsschemas_notification_settings_model_item = NotificationSettingsModelItem.from_dict(
                componentsschemas_notification_settings_model_item_data
            )

            notifications.append(componentsschemas_notification_settings_model_item)

        time_zone = d.pop("timeZone", UNSET)

        comment_sort_descending = d.pop("commentSortDescending", UNSET)

        warn_on_leaving_unsaved = d.pop("warnOnLeavingUnsaved", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, UserPreferenceModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = UserPreferenceModelLinks.from_dict(_field_links)

        user_preference_model = cls(
            auto_hide_popups=auto_hide_popups,
            hide_mail=hide_mail,
            notifications=notifications,
            time_zone=time_zone,
            comment_sort_descending=comment_sort_descending,
            warn_on_leaving_unsaved=warn_on_leaving_unsaved,
            field_links=field_links,
        )

        user_preference_model.additional_properties = d
        return user_preference_model

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
