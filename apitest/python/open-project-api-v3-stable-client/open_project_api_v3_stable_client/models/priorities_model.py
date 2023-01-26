from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PrioritiesModel")


@attr.s(auto_attribs=True)
class PrioritiesModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/priorities'}}, '_type': 'Collection', 'total': 4, 'count': 4, '_embedded':
            {'elements': [{'_type': 'Priority', '_links': {'self': {'href': '/api/v3/priorities/1', 'title': 'Low'}}, 'id':
            1, 'name': 'Low', 'position': 1, 'isDefault': False, 'isActive': True}, {'_type': 'Priority', '_links': {'self':
            {'href': '/api/v3/priorities/2', 'title': 'Normal'}}, 'id': 2, 'name': 'Normal', 'position': 2, 'isDefault':
            True, 'isActive': True}, {'_type': 'Priority', '_links': {'self': {'href': '/api/v3/priorities/3', 'title':
            'High'}}, 'id': 3, 'name': 'High', 'position': 3, 'isDefault': False, 'isActive': True}, {'_type': 'Priority',
            '_links': {'self': {'href': '/api/v3/priorities/4', 'title': 'Immediate'}}, 'id': 4, 'name': 'Immediate',
            'position': 5, 'isDefault': False, 'isActive': True}]}}

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
        priorities_model = cls()

        priorities_model.additional_properties = d
        return priorities_model

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
