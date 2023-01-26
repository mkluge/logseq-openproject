from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="QueryFilterInstanceSchemasModel")


@attr.s(auto_attribs=True)
class QueryFilterInstanceSchemasModel:
    """
    Example:
        {'_type': 'Collection', 'total': 2, 'count': 2, '_embedded': {'elements': [{'_type':
            'QueryFilterInstanceSchema', '_dependencies': [{'_type': 'SchemaDependency', 'on': 'operator', 'dependencies':
            {'/api/v3/queries/operators/=': {'values': {'type': '[]User', 'name': 'Values', 'required': True, 'hasDefault':
            False, 'writable': True, '_links': {}}}, '/api/v3/queries/operators/!': {'values': {'type': '[]User', 'name':
            'Values', 'required': True, 'hasDefault': False, 'writable': True, '_links': {}}},
            '/api/v3/queries/operators/!*': {}, '/api/v3/queries/operators/*': {}}}], 'name': {'type': 'String', 'name':
            'Name', 'required': True, 'hasDefault': True, 'writable': False}, 'filter': {'type': 'QueryFilter', 'name':
            'Filter', 'required': True, 'hasDefault': False, 'writable': True, '_links': {}}, '_links': {'self': {'href':
            '/api/v3/queries/filter_instance_schemas/assignee'}, 'filter': {'href': '/api/v3/queries/filters/assignee',
            'title': 'Assignee'}}}, {'_type': 'QueryFilterInstanceSchema', '_dependencies': [{'_type': 'SchemaDependency',
            'on': 'operator', 'dependencies': {'/api/v3/queries/operators/=': {'values': {'type': '[]User', 'name':
            'Values', 'required': True, 'hasDefault': False, 'writable': True, '_links': {}}},
            '/api/v3/queries/operators/!': {'values': {'type': '[]User', 'name': 'Values', 'required': True, 'hasDefault':
            False, 'writable': True, '_links': {}}}}}], 'name': {'type': 'String', 'name': 'Name', 'required': True,
            'hasDefault': True, 'writable': False}, 'filter': {'type': 'QueryFilter', 'name': 'Filter', 'required': True,
            'hasDefault': False, 'writable': True, '_links': {}}, '_links': {'self': {'href':
            '/api/v3/queries/filter_instance_schemas/author'}, 'filter': {'href': '/api/v3/queries/filters/author', 'title':
            'Author'}}}]}, '_links': {'self': {'href': '/api/v3/queries/filter_instance_schemas'}}}

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
        query_filter_instance_schemas_model = cls()

        query_filter_instance_schemas_model.additional_properties = d
        return query_filter_instance_schemas_model

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
