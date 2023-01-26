from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ViewMembershipModel")


@attr.s(auto_attribs=True)
class ViewMembershipModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/memberships/11', 'title': 'Some user'}, 'schema': {'href':
            '/api/v3/memberships/schema'}, 'update': {'href': '/api/v3/memberships/11/form', 'method': 'post'},
            'updateImmediately': {'href': '/api/v3/memberships/11', 'method': 'patch'}, 'project': {'href':
            '/api/v3/projects/3', 'title': 'A project'}, 'principal': {'href': '/api/v3/users/4', 'title': 'Some user'},
            'roles': [{'href': '/api/v3/roles/5', 'title': 'Member'}, {'href': '/api/v3/roles/4', 'title': 'Reader'}]},
            '_type': 'Membership', 'id': 11, 'createdAt': '2015-03-20T12:56:56Z', 'updatedAt': '2018-12-20T18:16:11Z',
            '_embedded': {'project...': {}, 'principal...': {}, 'roles...': []}}

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
        view_membership_model = cls()

        view_membership_model.additional_properties = d
        return view_membership_model

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
