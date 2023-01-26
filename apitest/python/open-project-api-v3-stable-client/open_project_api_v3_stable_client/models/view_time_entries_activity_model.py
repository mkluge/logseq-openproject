from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ViewTimeEntriesActivityModel")


@attr.s(auto_attribs=True)
class ViewTimeEntriesActivityModel:
    """
    Example:
        {'_type': 'TimeEntriesActivity', 'id': 18, 'name': 'a autem', 'position': 10, 'default': False, '_embedded':
            {'projects...': []}, '_links': {'self': {'href': '/api/v3/time_entries/activities/18', 'title': 'a autem'},
            'projects': [{'href': '/api/v3/projects/seeded_project', 'title': 'Seeded Project'}, {'href':
            '/api/v3/projects/working-project', 'title': 'Working Project'}]}}

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
        view_time_entries_activity_model = cls()

        view_time_entries_activity_model.additional_properties = d
        return view_time_entries_activity_model

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
