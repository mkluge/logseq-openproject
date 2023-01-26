from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ProjectsSchemaModel")


@attr.s(auto_attribs=True)
class ProjectsSchemaModel:
    """
    Example:
        {'_type': 'Schema', '_dependencies': [], 'id': {'type': 'Integer', 'name': 'ID', 'required': True, 'hasDefault':
            False, 'writable': False}, 'name': {'type': 'String', 'name': 'Name', 'required': True, 'hasDefault': False,
            'writable': True, 'minLength': 1, 'maxLength': 255}, 'identifier': {'type': 'String', 'name': 'Identifier',
            'required': True, 'hasDefault': False, 'writable': True, 'minLength': 1, 'maxLength': 100}, 'description':
            {'type': 'Formattable', 'name': 'Description', 'required': False, 'hasDefault': False, 'writable': True},
            'public': {'type': 'Boolean', 'name': 'Public', 'required': True, 'hasDefault': False, 'writable': True},
            'active': {'type': 'Boolean', 'name': 'Active', 'required': True, 'hasDefault': True, 'writable': True},
            'status': {'type': 'ProjectStatus', 'name': 'Status', 'required': False, 'hasDefault': True, 'writable': True,
            '_links': {'allowedValues': [{'href': '/api/v3/project_statuses/on_track', 'title': 'On track'}, {'href':
            '/api/v3/project_statuses/at_risk', 'title': 'At risk'}, {'href': '/api/v3/project_statuses/off_track', 'title':
            'Off track'}]}}, 'statusExplanation': {'type': 'Formattable', 'name': 'Status explanation', 'required': False,
            'hasDefault': False, 'writable': True}, 'parent': {'type': 'Project', 'name': 'Subproject of', 'required':
            False, 'hasDefault': False, 'writable': True, 'location': '_links', 'visibility': 'default', '_links': {}},
            'createdAt': {'type': 'DateTime', 'name': 'Created on', 'required': True, 'hasDefault': False, 'writable':
            False}, 'updatedAt': {'type': 'DateTime', 'name': 'Updated on', 'required': True, 'hasDefault': False,
            'writable': False}, 'customField30': {'type': 'Integer', 'name': 'Integer project custom field', 'required':
            False, 'hasDefault': False, 'writable': True, 'visibility': 'default'}, 'customField31': {'type':
            'CustomOption', 'name': 'List project custom field', 'required': False, 'hasDefault': False, 'writable': True,
            'location': '_links', 'visibility': 'default', '_links': {}}, 'customField32': {'type': 'Version', 'name':
            'Version project custom field', 'required': False, 'hasDefault': False, 'writable': True, 'location': '_links',
            'visibility': 'default', '_links': {}}, 'customField34': {'type': 'Boolean', 'name': 'Boolean project custom
            field', 'required': False, 'hasDefault': False, 'writable': True, 'visibility': 'default'}, 'customField35':
            {'type': 'String', 'name': 'Text project custom field', 'required': True, 'hasDefault': False, 'writable': True,
            'visibility': 'default'}, '_links': {'self': {'href': '/api/v3/projects/schema'}}}

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
        projects_schema_model = cls()

        projects_schema_model.additional_properties = d
        return projects_schema_model

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
