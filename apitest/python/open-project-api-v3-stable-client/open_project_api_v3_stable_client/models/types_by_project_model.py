from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TypesByProjectModel")


@attr.s(auto_attribs=True)
class TypesByProjectModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/projects/11/types'}}, 'total': 2, 'count': 2, '_type': 'Collection',
            '_embedded': {'elements': [{'_links': {'self': {'href': '/api/v3/types/1'}}, '_type': 'Type', 'id': 1, 'name':
            'Bug', 'color': '#ff0000', 'position': 1, 'isDefault': True, 'isMilestone': False, 'createdAt':
            '2014-05-21T08:51:20Z', 'updatedAt': '2014-05-21T08:51:20Z'}, {'_links': {'self': {'href': '/api/v3/types/2'}},
            '_type': 'Type', 'id': 2, 'name': 'Feature', 'color': '#888', 'position': 2, 'isDefault': False, 'isMilestone':
            False, 'createdAt': '2014-05-21T08:51:20Z', 'updatedAt': '2014-05-21T08:51:20Z'}]}}

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
        types_by_project_model = cls()

        types_by_project_model.additional_properties = d
        return types_by_project_model

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
