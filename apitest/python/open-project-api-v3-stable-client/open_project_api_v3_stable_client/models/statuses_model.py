from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="StatusesModel")


@attr.s(auto_attribs=True)
class StatusesModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/statuses'}}, 'total': 6, 'count': 6, '_type': 'Collection', '_embedded':
            {'elements': [{'_links': {'self': {'href': '/api/v3/statuses/1'}}, '_type': 'Status', 'id': 1, 'name': 'New',
            'position': 1, 'isDefault': True, 'isClosed': False, 'defaultDoneRatio': 0}, {'_links': {'self': {'href':
            '/api/v3/statuses/3'}}, '_type': 'Status', 'id': 3, 'name': 'Resolved', 'position': 3, 'isDefault': False,
            'isClosed': False, 'isReadonly': False, 'defaultDoneRatio': 75}, {'_links': {'self': {'href':
            '/api/v3/statuses/4'}}, '_type': 'Status', 'id': 4, 'name': 'Feedback', 'position': 4, 'isDefault': False,
            'isClosed': False, 'defaultDoneRatio': 25}, {'_links': {'self': {'href': '/api/v3/statuses/5'}}, '_type':
            'Status', 'id': 5, 'name': 'Closed', 'position': 5, 'isDefault': False, 'isClosed': True, 'defaultDoneRatio':
            100}, {'_links': {'self': {'href': '/api/v3/statuses/6'}}, '_type': 'Status', 'id': 6, 'name': 'Rejected',
            'position': 6, 'isDefault': False, 'isClosed': True, 'defaultDoneRatio': 100}, {'_links': {'self': {'href':
            '/api/v3/statuses/2'}}, '_type': 'Status', 'id': 2, 'name': 'In Progress', 'position': 3, 'isDefault': False,
            'isClosed': False, 'defaultDoneRatio': 50}]}}

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
        statuses_model = cls()

        statuses_model.additional_properties = d
        return statuses_model

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
