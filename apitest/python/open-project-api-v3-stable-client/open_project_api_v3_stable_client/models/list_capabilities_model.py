from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ListCapabilitiesModel")


@attr.s(auto_attribs=True)
class ListCapabilitiesModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/capabilities'}, 'changeSize': {'href':
            '/api/v3/capabilities?pageSize={size}', 'templated': True}, 'jumpTo': {'href':
            '/api/v3/capabilities?offset={offset}', 'templated': True}}, 'total': 4, 'count': 4, '_type': 'Collection',
            '_embedded': {'elements': [{'_links': {'self': {'href': '/api/v3/capabilities/work_packages/create/p123-567'},
            'action': {'href': '/api/v3/actions/work_packages/create', 'title': 'Add work package'}, 'context': {'href':
            '/api/v3/projects/123', 'title': 'A project'}, 'principal': {'href': '/api/v3/users/567', 'title': 'Some
            user'}}, '_type': 'Capability', 'id': 'work_packages/create/p123-567'}, {'_links': {'self': {'href':
            '/api/v3/capabilities/work_packages/assignee/p123-567'}, 'action': {'href':
            '/api/v3/actions/work_packages/assignee'}, 'context': {'href': '/api/v3/projects/123', 'title': 'A project'},
            'principal': {'href': '/api/v3/users/567', 'title': 'Some user'}}, '_type': 'Capability', 'id':
            'work_packages/assignee/p123-567'}, {'_links': {'self': {'href':
            '/api/v3/capabilities/memberships/create/p345-821', 'title': 'Create members'}, 'action': {'href':
            '/api/v3/actions/memberships/create'}, 'context': {'href': '/api/v3/projects/345', 'title': 'A project'},
            'principal': {'href': '/api/v3/users/821', 'title': 'Some user'}}, '_type': 'Capability', 'id':
            'memberships/create/p345-821'}, {'_links': {'self': {'href': '/api/v3/capabilities/users/delete/g-567', 'title':
            'Delete user'}, 'context': {'href': '/api/v3/capabilities/context/global', 'title': 'Global'}, 'principal':
            {'href': '/api/v3/users/567', 'title': 'Some user'}}, '_type': 'Capability', 'id': 'users/delete/g-567'}]}}

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
        list_capabilities_model = cls()

        list_capabilities_model.additional_properties = d
        return list_capabilities_model

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
