from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="AvailableProjectsForTimeEntriesModel")


@attr.s(auto_attribs=True)
class AvailableProjectsForTimeEntriesModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/time_entries/available_projects'}}, '_type': 'Collection', 'total': 2,
            'count': 2, '_embedded': {'elements': [{'_type': 'Project...'}, {'_type': 'Project...'}]}}

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
        available_projects_for_time_entries_model = cls()

        available_projects_for_time_entries_model.additional_properties = d
        return available_projects_for_time_entries_model

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
