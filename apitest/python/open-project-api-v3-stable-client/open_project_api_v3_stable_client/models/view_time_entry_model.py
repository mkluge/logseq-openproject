from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ViewTimeEntryModel")


@attr.s(auto_attribs=True)
class ViewTimeEntryModel:
    """
    Example:
        {'_type': 'TimeEntry', 'id': 1, 'comment': {'format': 'plain', 'raw': 'Some text explaining why the time entry
            was created', 'html': '<p>Some text explaining why the time entry was created</p>'}, 'spentOn': '2015-03-20',
            'hours': 'PT5H', 'createdAt': '2015-03-20T12:56:56Z', 'updatedAt': '2015-03-20T12:56:56Z', 'customField12': 5,
            '_embedded': {'project...': {}, 'workPackage...': {}, 'user...': {}, 'activity...': {}}, '_links': {'self':
            {'href': '/api/v3/time_entries/1'}, 'updateImmediately': {'href': '/api/v3/time_entries/1', 'method': 'patch'},
            'delete': {'href': '/api/v3/time_entries/1', 'method': 'delete'}, 'project': {'href': '/api/v3/projects/1',
            'title': 'Some project'}, 'workPackage': {'href': '/api/v3/work_packages/1', 'title': 'Some work package'},
            'user': {'href': '/api/v3/users/2', 'title': 'Some user'}, 'activity': {'href':
            '/api/v3/time_entries/activities/18', 'title': 'Some time entry activity'}, 'customField4': {'href':
            '/api/v3/users/5', 'title': 'Some other user'}}}

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
        view_time_entry_model = cls()

        view_time_entry_model.additional_properties = d
        return view_time_entry_model

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
