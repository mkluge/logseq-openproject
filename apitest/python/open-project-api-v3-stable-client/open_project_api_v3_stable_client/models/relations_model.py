from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RelationsModel")


@attr.s(auto_attribs=True)
class RelationsModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/relations'}}, 'total': 3, 'count': 1, '_type': 'Collection', '_embedded':
            {'elements': [{'_links': {'self': {'href': '/api/v3/relations/1'}, 'update': {'href':
            '/api/v3/relations/1/form', 'method': 'POST'}, 'updateImmediately': {'href': '/api/v3/relations/1', 'method':
            'PATCH'}, 'delete': {'href': '/api/v3/relations/1', 'method': 'DELETE'}, 'from': {'href':
            '/api/v3/work_packages/42', 'title': 'Steel Delivery'}, 'to': {'href': '/api/v3/work_packages/84', 'title':
            'Bending the steel'}}, '_type': 'Relation', 'id': 1, 'name': 'precedes', 'type': 'precedes', 'reverseType':
            'follows', 'description': "We can't bend the steel before it's been delivered!", 'delay': 0}]}}

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
        relations_model = cls()

        relations_model.additional_properties = d
        return relations_model

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
