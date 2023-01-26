from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RolesModel")


@attr.s(auto_attribs=True)
class RolesModel:
    """
    Example:
        {'_type': 'Collection', 'total': 5, 'count': 5, '_embedded': {'elements': [{'_type': 'Role', 'id': 3, 'name':
            'Manager', '_links': {'self': {'href': '/api/v3/roles/3', 'title': 'Manager'}}}, {'_type': 'Role', 'id': 2,
            'name': 'Anonymous', '_links': {'self': {'href': '/api/v3/roles/2', 'title': 'Anonymous'}}}, {'_type': 'Role',
            'id': 5, 'name': 'Reader', '_links': {'self': {'href': '/api/v3/roles/5', 'title': 'Reader'}}}, {'_type':
            'Role', 'id': 4, 'name': 'Member', '_links': {'self': {'href': '/api/v3/roles/4', 'title': 'Member'}}},
            {'_type': 'Role', 'id': 1, 'name': 'Non member', '_links': {'self': {'href': '/api/v3/roles/1', 'title': 'Non
            member'}}}]}, '_links': {'self': {'href': '/api/v3/roles'}}}

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
        roles_model = cls()

        roles_model.additional_properties = d
        return roles_model

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
