from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ViewTimeEntrySchemaModel")


@attr.s(auto_attribs=True)
class ViewTimeEntrySchemaModel:
    """
    Example:
        {'_type': 'Schema', '_dependencies': [], 'id': {'type': 'Integer', 'name': 'ID', 'required': True, 'hasDefault':
            False, 'writable': False, 'options': {}}, 'createdAt': {'type': 'DateTime', 'name': 'Created on', 'required':
            True, 'hasDefault': False, 'writable': False, 'options': {}}, 'updatedAt': {'type': 'DateTime', 'name': 'Updated
            on', 'required': True, 'hasDefault': False, 'writable': False, 'options': {}}, 'spentOn': {'type': 'Date',
            'name': 'Date', 'required': True, 'hasDefault': False, 'writable': True, 'options': {}}, 'hours': {'type':
            'Duration', 'name': 'Hours', 'required': True, 'hasDefault': False, 'writable': True, 'options': {}}, 'user':
            {'type': 'User', 'name': 'User', 'required': True, 'hasDefault': False, 'writable': False, 'options': {}},
            'workPackage': {'type': 'WorkPackage', 'name': 'Work package', 'required': False, 'hasDefault': False,
            'writable': True, 'location': '_links', '_links': {}}, 'project': {'type': 'Project', 'name': 'Project',
            'required': False, 'hasDefault': False, 'writable': True, 'location': '_links', '_links': {}}, 'activity':
            {'type': 'TimeEntriesActivity', 'name': 'Activity', 'required': True, 'hasDefault': True, 'writable': True,
            'location': '_links', '_links': {}}, 'customField29': {'type': 'String', 'name': 'sfsdfsdfsdfsdfdsf',
            'required': False, 'hasDefault': False, 'writable': True, 'options': {'rtl': None}}, '_links': {'self': {'href':
            '/api/v3/time_entries/schema'}}}

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
        view_time_entry_schema_model = cls()

        view_time_entry_schema_model.additional_properties = d
        return view_time_entry_schema_model

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
