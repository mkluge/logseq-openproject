from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PrincipalsModel")


@attr.s(auto_attribs=True)
class PrincipalsModel:
    """
    Example:
        {'_type': 'Collection', 'total': 4, 'count': 4, '_embedded': {'elements': [{'_type': 'User', 'id': 4, 'login':
            'Eliza92778', 'admin': False, 'firstName': 'Danika', 'lastName': "O'Keefe", 'name': "Danika O'Keefe", 'email':
            'jackie@dicki.org', 'avatar': 'https://example.org/users/4/avatar', 'createdAt': '2015-03-20T12:57:02Z',
            'updatedAt': '2015-06-16T15:28:14Z', 'status': 'active', 'identityUrl': None, '_links': {'self': {'href':
            '/api/v3/users/4', 'title': "Danika O'Keefe"}, 'showUser': {'href': '/users/4', 'type': 'text/html'},
            'updateImmediately': {'href': '/api/v3/users/4', 'title': 'Update Eliza92778', 'method': 'patch'}, 'lock':
            {'href': '/api/v3/users/4/lock', 'title': 'Set lock on Eliza92778', 'method': 'post'}, 'delete': {'href':
            '/api/v3/users/4', 'title': 'Delete Eliza92778', 'method': 'delete'}}}, {'_type': 'User', 'id': 2, 'login':
            'Sebastian9686', 'admin': False, 'firstName': 'Peggie', 'lastName': 'Feeney', 'name': 'Peggie Feeney', 'email':
            None, 'avatar': 'https://example.org/users/4/avatar', 'createdAt': '2015-03-20T12:56:55Z', 'updatedAt':
            '2015-03-20T12:56:55Z', 'status': 'active', 'identityUrl': None, '_links': {'self': {'href': '/api/v3/users/2',
            'title': 'Peggie Feeney'}, 'showUser': {'href': '/users/2', 'type': 'text/html'}, 'updateImmediately': {'href':
            '/api/v3/users/2', 'title': 'Update Sebastian9686', 'method': 'patch'}, 'lock': {'href': '/api/v3/users/2/lock',
            'title': 'Set lock on Sebastian9686', 'method': 'post'}, 'delete': {'href': '/api/v3/users/2', 'title': 'Delete
            Sebastian9686', 'method': 'delete'}}}, {'_type': 'Group', 'id': 9, 'name': 'The group', 'createdAt':
            '2015-09-23T11:06:36Z', 'updatedAt': '2015-09-23T11:06:36Z', '_links': {'self': {'href': '/api/v3/groups/9',
            'title': 'The group'}}}, {'_type': 'PlaceholderUser', 'id': 29, 'name': 'UX Designer', 'createdAt':
            '2018-09-23T11:06:36Z', 'updatedAt': '2019-10-23T11:06:36Z', '_links': {'self': {'href':
            '/api/v3/placeholder_users/29', 'title': 'UX Designer'}}}]}, '_links': {'self': {'href': '/api/v3/principals'}}}

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
        principals_model = cls()

        principals_model.additional_properties = d
        return principals_model

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
