from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="QueriesModel")


@attr.s(auto_attribs=True)
class QueriesModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/queries'}}, 'total': 1, 'count': 1, '_type': 'Collection', '_embedded':
            {'elements': [{'_type': 'Query', 'id': 9, 'name': 'fdsfdsfdsf', 'createdAt': '2015-03-20T12:56:56Z',
            'updatedAt': '2015-05-20T18:16:53Z', 'filters': [{'_type': 'StatusQueryFilter', 'name': 'Status', '_links':
            {'filter': {'href': '/api/v3/queries/filters/status', 'title': 'Status'}, 'operator': {'href':
            '/api/v3/queries/operators/o', 'title': 'open'}, 'schema': {'href':
            '/api/v3/queries/filter_instance_schemas/status'}, 'values': []}}, {'_type': 'DueDateQueryFilter', 'name':
            'Finish date', 'values': ['1'], '_links': {'filter': {'href': '/api/v3/queries/filters/dueDate', 'title':
            'Finish date'}, 'operator': {'href': '/api/v3/queries/operators/<t+', 'title': 'in less than'}, 'schema':
            {'href': '/api/v3/queries/filter_instance_schemas/dueDate'}}}], 'public': False, 'sums': False, 'starred': True,
            'projections': [{'_type': 'Query::TableProjection'}, {'_type': 'Query::TeamPlannerProjection', '_links':
            {'rows': [{'href': '/api/v3/users/1', 'title': 'Bob Bobbit'}]}}, {'_type': 'Query::CalendarProjection'}],
            '_embedded': {'results': {'_type': 'WorkPackageCollection', 'total': 234, 'count': 30, 'pageSize': 30, 'offset':
            1, '_embedded': {'elements': ['<--- shortened for brevity --->']}, '_links': {'self': {'href': '/api/v3/projects
            /3/work_packages?filters=%5B%7B%22status%22%3A%7B%22operator%22%3A%22o%22%2C%22values%22%3A%5B%5D%7D%7D%2C%7B%22
            dueDate%22%3A%7B%22operator%22%3A%22%3Ct%2B%22%2C%22values%22%3A%5B%221%22%5D%7D%7D%5D&offset=1&pageSize=2&sortB
            y=%5B%5B%22parent%22%2C%22desc%22%5D%5D'}, 'jumpTo': {'href': '/api/v3/projects/3/work_packages?filters=%5B%7B%2
            2status%22%3A%7B%22operator%22%3A%22o%22%2C%22values%22%3A%5B%5D%7D%7D%2C%7B%22dueDate%22%3A%7B%22operator%22%3A
            %22%3Ct%2B%22%2C%22values%22%3A%5B%221%22%5D%7D%7D%5D&offset=%7Boffset%7D&pageSize=2&sortBy=%5B%5B%22parent%22%2
            C%22desc%22%5D%5D', 'templated': True}, 'changeSize': {'href': '/api/v3/projects/3/work_packages?filters=%5B%7B%
            22status%22%3A%7B%22operator%22%3A%22o%22%2C%22values%22%3A%5B%5D%7D%7D%2C%7B%22dueDate%22%3A%7B%22operator%22%3
            A%22%3Ct%2B%22%2C%22values%22%3A%5B%221%22%5D%7D%7D%5D&offset=1&pageSize=%7Bsize%7D&sortBy=%5B%5B%22parent%22%2C
            %22desc%22%5D%5D', 'templated': True}, 'createWorkPackage': {'href': '/api/v3/work_packages/form', 'method':
            'post'}, 'createWorkPackageImmediate': {'href': '/api/v3/work_packages', 'method': 'post'}}}}, '_links':
            {'self': {'href': '/api/v3/queries/9', 'title': 'fdsfdsfdsf'}, 'results': {'href': '/api/v3/projects/3/work_pack
            ages?filters=%5B%7B%22status%22%3A%7B%22operator%22%3A%22o%22%2C%22values%22%3A%5B%5D%7D%7D%2C%7B%22dueDate%22%3
            A%7B%22operator%22%3A%22%3Ct%2B%22%2C%22values%22%3A%5B%221%22%5D%7D%7D%5D&offset=1&pageSize=2&sortBy=%5B%5B%22p
            arent%22%2C%22desc%22%5D%5D'}, 'columns': [{'href': '/api/v3/queries/columns/id', 'title': 'ID'}, {'href':
            '/api/v3/queries/columns/subject', 'title': 'Subject'}, {'href': '/api/v3/queries/columns/type', 'title':
            'Type'}, {'href': '/api/v3/queries/columns/status', 'title': 'Status'}, {'href':
            '/api/v3/queries/columns/priority', 'title': 'Priority'}, {'href': '/api/v3/queries/columns/assignee', 'title':
            'Assignee'}, {'href': '/api/v3/queries/columns/updated_at', 'title': 'Updated on'}], 'groupBy': {'href': None,
            'title': None}, 'sortBy': [{'href': '/api/v3/queries/sort_bys/parent-desc', 'title': 'Parent (Descending)'}],
            'user': {'href': '/api/v3/users/1', 'title': 'OpenProject Admin'}, 'project': {'href': '/api/v3/projects/3',
            'title': 'copy'}}}]}}

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
        queries_model = cls()

        queries_model.additional_properties = d
        return queries_model

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
