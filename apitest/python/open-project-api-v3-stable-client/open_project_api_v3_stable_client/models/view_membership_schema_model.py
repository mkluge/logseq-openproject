from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ViewMembershipSchemaModel")


@attr.s(auto_attribs=True)
class ViewMembershipSchemaModel:
    """
    Example:
        {'_type': 'Schema', '_dependencies': [], 'id': {'type': 'Integer', 'name': 'ID', 'required': True, 'hasDefault':
            False, 'writable': False}, 'createdAt': {'type': 'DateTime', 'name': 'Created on', 'required': True,
            'hasDefault': False, 'writable': False}, 'updatedAt': {'type': 'DateTime', 'name': 'Updated on', 'required':
            True, 'hasDefault': False, 'writable': False}, 'notificationMessage': {'type': 'Formattable', 'name': 'Message',
            'required': False, 'hasDefault': False, 'writable': True, 'options': {}, 'location': '_meta'}, 'project':
            {'type': 'Project', 'name': 'Project', 'required': False, 'hasDefault': False, 'writable': True, 'location':
            '_links', '_links': {}}, 'principal': {'type': 'Principal', 'name': 'Principal', 'required': True, 'hasDefault':
            False, 'writable': True, 'location': '_links', '_links': {}}, 'roles': {'type': '[]Role', 'name': 'Role',
            'required': True, 'hasDefault': False, 'writable': True, 'location': '_links', '_links': {}}, '_links': {'self':
            {'href': '/api/v3/memberships/schema'}}}

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
        view_membership_schema_model = cls()

        view_membership_schema_model.additional_properties = d
        return view_membership_schema_model

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
