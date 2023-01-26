from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SchemaForProjectQueriesModel")


@attr.s(auto_attribs=True)
class SchemaForProjectQueriesModel:
    """
    Example:
        {'_type': 'Schema', '_dependencies': [], 'id': {'type': 'Integer', 'name': 'ID', 'required': True, 'hasDefault':
            False, 'writable': False}, 'name': {'type': 'String', 'name': 'Name', 'required': True, 'hasDefault': False,
            'writable': True, 'minLength': 1, 'maxLength': 255}, 'createdAt': {'type': 'DateTime', 'name': 'Created on',
            'required': True, 'hasDefault': False, 'writable': False}, 'updatedAt': {'type': 'DateTime', 'name': 'Updated
            on', 'required': True, 'hasDefault': False, 'writable': False}, 'user': {'type': 'User', 'name': 'User',
            'required': True, 'hasDefault': True, 'writable': False}, 'project': {'type': 'Project', 'name': 'Project',
            'required': False, 'hasDefault': False, 'writable': True, '_links': {}}, 'public': {'type': 'Boolean', 'name':
            'Public', 'required': False, 'hasDefault': True, 'writable': True}, 'sums': {'type': 'Boolean', 'name': 'Sums',
            'required': False, 'hasDefault': True, 'writable': True}, 'timelineVisible': {'type': 'Boolean', 'name':
            'Timeline visible', 'required': False, 'hasDefault': True, 'writable': True}, 'timelineZoomLevel': {'type':
            'String', 'name': 'Timeline zoom level', 'required': False, 'hasDefault': True, 'writable': True},
            'showHierarchies': {'type': 'Boolean', 'name': 'Show hierarchies', 'required': False, 'hasDefault': True,
            'writable': True}, 'starred': {'type': 'Boolean', 'name': 'Starred', 'required': False, 'hasDefault': True,
            'writable': True}, 'columns': {'type': '[]QueryColumn', 'name': 'Columns', 'required': False, 'hasDefault':
            True, 'writable': True, '_links': {}}, 'filters': {'type': '[]QueryFilterInstance', 'name': 'Filters',
            'required': False, 'writable': True, 'hasDefault': True, '_links': {'allowedValuesSchemas': {'href':
            '/api/v3/projects/42/queries/filter_instance_schemas'}}}, 'groupBy': {'type': '[]QueryGroupBy', 'name': 'Group
            results by', 'required': False, 'hasDefault': False, 'writable': True, '_links': {}}, 'sortBy': {'type':
            '[]QuerySortBy', 'name': 'Sort by', 'required': False, 'hasDefault': True, 'writable': True, '_links': {}},
            'results': {'type': 'WorkPackageCollection', 'name': 'Results', 'required': False, 'hasDefault': False,
            'writable': False}, '_embedded': {'filtersSchemas': {'_type': 'Collection', 'total': 20, 'count': 20,
            '_embedded': {'elements': [{'_type': 'QueryFilterInstanceSchema', '_dependencies': [{'_type':
            'SchemaDependency', 'on': 'operator', 'dependencies': {'/api/v3/queries/operators/=': {'values': {'type':
            '[]User', 'name': 'Values', 'required': True, 'hasDefault': False, 'writable': True, '_links': {}}},
            '/api/v3/queries/operators/!': {'values': {'type': '[]User', 'name': 'Values', 'required': True, 'hasDefault':
            False, 'writable': True, '_links': {}}}, '/api/v3/queries/operators/!*': {}, '/api/v3/queries/operators/*':
            {}}}], 'name': {'type': 'String', 'name': 'Name', 'required': True, 'hasDefault': True, 'writable': False},
            'filter': {'type': 'QueryFilter', 'name': 'Filter', 'required': True, 'hasDefault': False, 'writable': True,
            '_links': {}}, '_links': {'self': {'href': '/api/v3/queries/filter_instance_schemas/assignee'}, 'filter':
            {'href': '/api/v3/queries/filters/assignee', 'title': 'Assignee'}}}, {'_type': 'QueryFilterInstanceSchema',
            '_dependencies': [{'_type': 'SchemaDependency', 'on': 'operator', 'dependencies':
            {'/api/v3/queries/operators/=': {'values': {'type': '[]User', 'name': 'Values', 'required': True, 'hasDefault':
            False, 'writable': True, '_links': {}}}, '/api/v3/queries/operators/!': {'values': {'type': '[]User', 'name':
            'Values', 'required': True, 'hasDefault': False, 'writable': True, '_links': {}}}}}], 'name': {'type': 'String',
            'name': 'Name', 'required': True, 'hasDefault': True, 'writable': False}, 'filter': {'type': 'QueryFilter',
            'name': 'Filter', 'required': True, 'hasDefault': False, 'writable': True, '_links': {}}, '_links': {'self':
            {'href': '/api/v3/queries/filter_instance_schemas/author'}, 'filter': {'href': '/api/v3/queries/filters/author',
            'title': 'Author'}}}]}, '_links': {'self': {'href': '/api/v3/projects/42/queries/filter_instance_schemas'}}}},
            '_links': {'self': {'href': '/api/v3/projects/42/queries/schema'}}}

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
        schema_for_project_queries_model = cls()

        schema_for_project_queries_model.additional_properties = d
        return schema_for_project_queries_model

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
