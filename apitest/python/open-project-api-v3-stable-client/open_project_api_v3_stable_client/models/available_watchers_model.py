from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="AvailableWatchersModel")


@attr.s(auto_attribs=True)
class AvailableWatchersModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/work_packages/1/available_watchers'}}, 'total': 2, 'count': 2, '_type':
            'Collection', '_embedded': {'elements': [{'_type': 'User', '_links': {'self': {'href': '/api/v3/users/1',
            'title': 'John Sheppard - j.sheppard'}, 'lock': {'href': '/api/v3/users/1/lock', 'title': 'Set lock on
            j.sheppard', 'method': 'POST'}, 'delete': {'href': '/api/v3/users/1', 'title': 'Delete j.sheppard', 'method':
            'DELETE'}}, 'id': 1, 'login': 'j.sheppard', 'firstName': 'John', 'lastName': 'Sheppard', 'email':
            'shep@mail.com', 'avatar': 'https://example.org/users/1/avatar', 'status': 'active', 'createdAt':
            '2014-05-21T08:51:20Z', 'updatedAt': '2014-05-21T08:51:20Z'}, {'_type': 'User', '_links': {'self': {'href':
            '/api/v3/users/2', 'title': 'Jim Sheppard - j.sheppard2'}, 'lock': {'href': '/api/v3/users/2/lock', 'title':
            'Set lock on j.sheppard2', 'method': 'POST'}, 'delete': {'href': '/api/v3/users/2', 'title': 'Delete
            j.sheppard2', 'method': 'DELETE'}}, 'id': 2, 'login': 'j.sheppard2', 'firstName': 'Jim', 'lastName': 'Sheppard',
            'email': 'shep@mail.net', 'avatar': 'https://example.org/users/1/avatar', 'status': 'active', 'createdAt':
            '2014-05-21T08:51:20Z', 'updatedAt': '2014-05-21T08:51:20Z'}]}}

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
        available_watchers_model = cls()

        available_watchers_model.additional_properties = d
        return available_watchers_model

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
