from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="AvailableRelationCandidatesModel")


@attr.s(auto_attribs=True)
class AvailableRelationCandidatesModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/projects/14/work_packages'}}, 'total': 2, 'count': 2, '_type':
            'Collection', '_embedded': {'elements': [{'_type': 'WorkPackage', '_links': {'self': {'href':
            '/api/v3/work_packages/1'}}, 'id': 1, 'subject': 'Skipped other properties for brevity'}, {'_type':
            'WorkPackage', '_links': {'self': {'href': '/api/v3/work_packages/2'}}, 'id': 2, 'subject': 'Skipped other
            properties for brevity'}]}}

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
        available_relation_candidates_model = cls()

        available_relation_candidates_model.additional_properties = d
        return available_relation_candidates_model

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
