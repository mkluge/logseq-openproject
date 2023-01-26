from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ViewUserSchemaModel")


@attr.s(auto_attribs=True)
class ViewUserSchemaModel:
    """
    Example:
        {'_type': 'Schema', '_dependencies': [], 'id': {'type': 'Integer', 'name': 'ID', 'required': True, 'hasDefault':
            False, 'writable': False, 'options': {}}, 'login': {'type': 'String', 'name': 'Username', 'required': True,
            'hasDefault': False, 'writable': True, 'minLength': 1, 'maxLength': 255, 'options': {}}, 'admin': {'type':
            'Boolean', 'name': 'Administrator', 'required': False, 'hasDefault': False, 'writable': True, 'options': {}},
            'mail': {'type': 'String', 'name': 'Email', 'required': True, 'hasDefault': False, 'writable': True,
            'minLength': 1, 'maxLength': 255, 'options': {}}, 'firstName': {'type': 'String', 'name': 'First name',
            'required': True, 'hasDefault': False, 'writable': False, 'minLength': 1, 'maxLength': 255, 'options': {}},
            'lastName': {'type': 'String', 'name': 'Last name', 'required': True, 'hasDefault': False, 'writable': False,
            'minLength': 1, 'maxLength': 255, 'options': {}}, 'avatar': {'type': 'String', 'name': 'Avatar', 'required':
            False, 'hasDefault': False, 'writable': False, 'options': {}}, 'status': {'type': 'String', 'name': 'Status',
            'required': False, 'hasDefault': False, 'writable': True, 'options': {}}, 'identityUrl': {'type': 'String',
            'name': 'Identity url', 'required': False, 'hasDefault': False, 'writable': True, 'options': {}}, 'language':
            {'type': 'String', 'name': 'Language', 'required': False, 'hasDefault': False, 'writable': True, 'options': {}},
            'password': {'type': 'Password', 'name': 'Password', 'required': False, 'hasDefault': False, 'writable': False,
            'options': {}}, 'createdAt': {'type': 'DateTime', 'name': 'Created on', 'required': True, 'hasDefault': False,
            'writable': False, 'options': {}}, 'updatedAt': {'type': 'DateTime', 'name': 'Updated on', 'required': True,
            'hasDefault': False, 'writable': False, 'options': {}}, 'customField1': {'type': 'String', 'name': 'User String
            CF', 'required': False, 'hasDefault': False, 'writable': True}, 'customField2': {'type': 'CustomOption', 'name':
            'User List cf', 'required': False, 'hasDefault': False, 'writable': True, 'location': '_links'}, '_links':
            {'self': {'href': '/api/v3/users/schema'}}}

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
        view_user_schema_model = cls()

        view_user_schema_model.additional_properties = d
        return view_user_schema_model

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
