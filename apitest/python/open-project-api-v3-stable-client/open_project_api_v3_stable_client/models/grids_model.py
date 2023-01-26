from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GridsModel")


@attr.s(auto_attribs=True)
class GridsModel:
    """
    Example:
        {'_type': 'Collection', 'total': 1, 'count': 1, 'pageSize': 30, 'offset': 1, '_embedded': {'elements':
            [{'_type': 'Grid', 'id': 2, 'rowCount': 8, 'columnCount': 5, 'widgets': [{'_type': 'GridWidget', 'identifier':
            'time_entries_current_user', 'startRow': 1, 'endRow': 8, 'startColumn': 1, 'endColumn': 3}, {'_type':
            'GridWidget', 'identifier': 'news', 'startRow': 3, 'endRow': 8, 'startColumn': 4, 'endColumn': 5}, {'_type':
            'GridWidget', 'identifier': 'documents', 'startRow': 1, 'endRow': 3, 'startColumn': 3, 'endColumn': 6}],
            'createdAt': '2018-12-03T16:58:30Z', 'updatedAt': '2018-12-13T19:36:40Z', '_links': {'scope': {'href':
            '/my/page', 'type': 'text/html'}, 'updateImmediately': {'href': '/api/v3/grids/2', 'method': 'patch'}, 'update':
            {'href': '/api/v3/grids/2/form', 'method': 'post'}, 'self': {'href': '/api/v3/grids/2'}}}, {'_type': 'Grid',
            'id': 5, 'rowCount': 1, 'columnCount': 4, 'widgets': [{'_type': 'GridWidget', 'identifier':
            'work_package_query', 'startRow': 1, 'endRow': 8, 'startColumn': 1, 'endColumn': 3}, {'_type': 'GridWidget',
            'identifier': 'work_package_query', 'startRow': 3, 'endRow': 8, 'startColumn': 4, 'endColumn': 5}, {'_type':
            'GridWidget', 'identifier': 'work_package_query', 'startRow': 1, 'endRow': 3, 'startColumn': 3, 'endColumn':
            6}], 'createdAt': '2019-01-05T16:58:30Z', 'updatedAt': '2019-01-07T19:36:40Z', '_links': {'scope': {'href':
            '/projects/a_project/boards', 'type': 'text/html'}, 'updateImmediately': {'href': '/api/v3/grids/5', 'method':
            'patch'}, 'update': {'href': '/api/v3/grids/5/form', 'method': 'post'}, 'self': {'href': '/api/v3/grids/5'}}}]},
            '_links': {'self': {'href': '/api/v3/grids?offset=1&pageSize=30'}, 'jumpTo': {'href':
            '/api/v3/grids?offset=%7Boffset%7D&pageSize=30', 'templated': True}, 'changeSize': {'href':
            '/api/v3/grids?offset=1&pageSize=%7Bsize%7D', 'templated': True}}}

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
        grids_model = cls()

        grids_model.additional_properties = d
        return grids_model

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
