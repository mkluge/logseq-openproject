from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ListTimeEntriesModel")


@attr.s(auto_attribs=True)
class ListTimeEntriesModel:
    """
    Example:
        {'_type': 'Collection', 'total': 39, 'count': 2, 'pageSize': 2, 'offset': 1, '_embedded': {'elements':
            [{'_type': 'TimeEntry', 'id': 5, 'comment': {'format': 'plain', 'raw': 'Some comment', 'html': '<p>Some
            comment</p>'}, 'spentOn': '2015-03-20', 'hours': 'PT5H', 'createdAt': '2015-03-20T12:56:56Z', 'updatedAt':
            '2015-03-20T12:56:56Z', '_links': {'self': {'href': '/api/v3/time_entries/1'}, 'updateImmediately': {'href':
            '/api/v3/time_entries/1', 'method': 'patch'}, 'delete': {'href': '/api/v3/time_entries/1', 'method': 'delete'},
            'project': {'href': '/api/v3/projects/1', 'title': 'Some project'}, 'workPackage': {'href':
            '/api/v3/work_packages/1', 'title': 'Some work package'}, 'user': {'href': '/api/v3/users/2', 'title': 'Some
            user'}, 'activity': {'href': '/api/v3/time_entries/activities/18', 'title': 'Some time entry activity'}}},
            {'_type': 'TimeEntry', 'id': 10, 'comment': {'format': 'plain', 'raw': 'Another comment', 'html': '<p>Another
            comment</p>'}, 'spentOn': '2015-03-21', 'hours': 'PT7H', 'createdAt': '2015-03-20T12:56:56Z', 'updatedAt':
            '2015-03-20T12:56:56Z', '_links': {'self': {'href': '/api/v3/time_entries/2'}, 'project': {'href':
            '/api/v3/projects/42', 'title': 'Some other project'}, 'workPackage': {'href': '/api/v3/work_packages/541',
            'title': 'Some other work package'}, 'user': {'href': '/api/v3/users/6', 'title': 'Some other project'},
            'activity': {'href': '/api/v3/time_entries/activities/14', 'title': 'some other time entry activity'}}}]},
            '_links': {'self': {'href': '/api/v3/time_entries?offset=1&pageSize=2'}, 'jumpTo': {'href':
            '/api/v3/time_entries?offset=%7Boffset%7D&pageSize=2', 'templated': True}, 'changeSize': {'href':
            '/api/v3/time_entries?offset=1&pageSize=%7Bsize%7D', 'templated': True}, 'nextByOffset': {'href':
            '/api/v3/time_entries?offset=2&pageSize=2'}, 'createTimeEntry': {'href': '/api/v3/time_entries/form', 'method':
            'post'}, 'createTimeEntryImmediately': {'href': '/api/v3/time_entries', 'method': 'post'}}}

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
        list_time_entries_model = cls()

        list_time_entries_model.additional_properties = d
        return list_time_entries_model

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
