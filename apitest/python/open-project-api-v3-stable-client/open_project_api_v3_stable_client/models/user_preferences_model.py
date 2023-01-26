from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="UserPreferencesModel")


@attr.s(auto_attribs=True)
class UserPreferencesModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/my_preferences'}, 'user': {'href': '/api/v3/users/1', 'title': 'John
            Sheppard'}, 'updateImmediately': {'href': '/api/v3/users/3/preferences', 'method': 'patch'}}, '_type':
            'UserPreferences', 'commentSortDescending': True, 'hideMail': False, 'timeZone': 'Europe/Berlin',
            'warnOnLeavingUnsaved': True, 'notifications': [{'watched': False, 'involved': True, 'mentioned': False,
            'newsAdded': 'false,', 'newsCommented': False, 'documentAdded': False, 'forumMessages': False, 'wikiPageAdded':
            False, 'wikiPageUpdated': False, 'membershipAdded': False, 'membershipUpdated': False, 'workPackageCommented':
            False, 'workPackageProcessed': False, 'workPackagePrioritized': False, 'workPackageScheduled': False, '_links':
            {'project': {'href': None}}}]}

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_preferences_model = cls()

        user_preferences_model.additional_properties = d
        return user_preferences_model

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
