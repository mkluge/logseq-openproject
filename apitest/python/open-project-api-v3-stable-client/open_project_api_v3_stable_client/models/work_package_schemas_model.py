from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="WorkPackageSchemasModel")


@attr.s(auto_attribs=True)
class WorkPackageSchemasModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/work_packages/schemas'}}, 'total': 5, 'count': 2, '_type': 'Collection',
            '_embedded': {'elements': [{'_type': 'Schema...', '_links': {'self': {'href':
            '/api/v3/work_packages/schemas/13-1'}}}, {'_type': 'Schema...', '_links': {'self': {'href':
            '/api/v3/work_packages/schemas/7-6'}}}]}}

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
        work_package_schemas_model = cls()

        work_package_schemas_model.additional_properties = d
        return work_package_schemas_model

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
