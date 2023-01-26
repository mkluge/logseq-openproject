from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RelationSchemaModel")


@attr.s(auto_attribs=True)
class RelationSchemaModel:
    """
    Example:
        {'_type': 'Schema', '_links': {'self': {'href': '/api/v3/relations/schema'}}, 'id': {'name': 'ID', 'type':
            'Integer', 'writable': False}, 'type': {'name': 'Type', 'type': 'String', 'writable': True}, 'reverseType':
            {'name': 'Reverse Type', 'type': 'String', 'writable': False}, 'description': {'name': 'Description', 'type':
            'String', 'writable': True}, 'from': {'name': 'From work package', 'type': 'WorkPackage', 'writable': False},
            'to': {'name': 'To work package', 'type': 'WorkPackage', 'writable': False}, 'delay': {'name': 'Delay', 'type':
            'Integer', 'writable': True}}

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
        relation_schema_model = cls()

        relation_schema_model.additional_properties = d
        return relation_schema_model

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
