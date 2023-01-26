from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ListMembershipsModel")


@attr.s(auto_attribs=True)
class ListMembershipsModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/memberships'}}, 'total': 2, 'count': 2, '_type': 'Collection',
            '_embedded': {'elements': [{'_links': {'self': {'href': '/api/v3/memberships/11'}, 'schema': {'href':
            '/api/v3/memberships/schema'}, 'project': {'href': '/api/v3/projects/3', 'title': 'A Project'}, 'principal':
            {'href': '/api/v3/users/5', 'title': 'A user'}, 'roles': [{'href': '/api/v3/roles/4', 'title': 'Reader'}]},
            '_type': 'Membership', 'id': 11, 'createdAt': '2015-03-20T12:56:56Z', 'updatedAt': '2018-12-20T18:16:11Z'},
            {'_links': {'self': {'href': '/api/v3/memberships/41'}, 'schema': {'href': '/api/v3/memberships/schema'},
            'project': {'href': '/api/v3/projects/6', 'title': 'Another Project'}, 'principal': {'href': '/api/v3/groups/5',
            'title': 'A group'}, 'roles': [{'href': '/api/v3/roles/8', 'title': 'Project admin'}]}, '_type': 'Membership',
            'id': 41, 'createdAt': '2019-12-22T12:56:06Z', 'updatedAt': '2020-12-20T18:16:12Z'}]}}

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
        list_memberships_model = cls()

        list_memberships_model.additional_properties = d
        return list_memberships_model

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
