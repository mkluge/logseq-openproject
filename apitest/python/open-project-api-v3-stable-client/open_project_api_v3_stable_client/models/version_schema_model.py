from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="VersionSchemaModel")


@attr.s(auto_attribs=True)
class VersionSchemaModel:
    """
    Example:
        {'_type': 'Schema', '_dependencies': [], 'id': {'type': 'Integer', 'name': 'ID', 'required': True, 'hasDefault':
            False, 'writable': False}, 'name': {'type': 'String', 'name': 'Name', 'required': True, 'hasDefault': False,
            'writable': True, 'minLength': 1, 'maxLength': 60}, 'description': {'type': 'Formattable', 'name':
            'Description', 'required': False, 'hasDefault': False, 'writable': True}, 'startDate': {'type': 'Date', 'name':
            'Start date', 'required': False, 'hasDefault': False, 'writable': True}, 'endDate': {'type': 'Date', 'name':
            'Finish date', 'required': False, 'hasDefault': False, 'writable': False}, 'status': {'type': 'String', 'name':
            'Status', 'required': True, 'hasDefault': False, 'writable': True, 'visibility': 'default', '_links': {}},
            'sharing': {'type': 'String', 'name': 'Sharing', 'required': True, 'hasDefault': False, 'writable': True,
            'visibility': 'default', '_links': {}}, 'createdAt': {'type': 'DateTime', 'name': 'Created on', 'required':
            True, 'hasDefault': False, 'writable': False}, 'updatedAt': {'type': 'DateTime', 'name': 'Updated on',
            'required': True, 'hasDefault': False, 'writable': False}, 'definingProject': {'type': 'Project', 'name':
            'Project', 'required': True, 'hasDefault': False, 'writable': True, '_links': {}}, 'customField14': {'type':
            'String', 'name': 'text CF', 'required': False, 'hasDefault': False, 'writable': True, 'visibility': 'default'},
            'customField40': {'type': 'CustomOption', 'name': 'List CF', 'required': False, 'hasDefault': False, 'writable':
            True, 'location': '_links', 'visibility': 'default', '_links': {}}, '_links': {'self': {'href':
            '/api/v3/versions/schema'}}}

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
        version_schema_model = cls()

        version_schema_model.additional_properties = d
        return version_schema_model

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
