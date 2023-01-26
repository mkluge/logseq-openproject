from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="VersionsByProjectModel")


@attr.s(auto_attribs=True)
class VersionsByProjectModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/projects/11/versions'}}, 'total': 3, 'count': 3, '_type': 'Collection',
            '_embedded': {'elements': [{'_links': {'self': {'href': '/api/v3/versions/11'}, 'definingProject': {'href':
            '/api/v3/projects/11'}, 'availableInProjects': {'href': '/api/v3/versions/11/projects'}}, '_type': 'Version',
            'id': 11, 'name': 'v3.0 Alpha', 'description': {'format': 'plain', 'raw': 'This version has a description',
            'html': 'This version has a description'}, 'startDate': '2014-11-20', 'endDate': None, 'status': 'Open'},
            {'_links': {'self': {'href': '/api/v3/versions/12'}, 'definingProject': {'href': '/api/v3/projects/11'},
            'availableInProjects': {'href': '/api/v3/versions/12/projects'}}, '_type': 'Version', 'id': 12, 'name': 'v2.0',
            'description': {'format': 'plain', 'raw': '', 'html': ''}, 'startDate': None, 'endDate': None, 'status':
            'Closed'}, {'_links': {'self': {'href': '/api/v3/versions/10'}, 'definingProject': {'href':
            '/api/v3/projects/11'}, 'availableInProjects': {'href': '/api/v3/versions/10/projects'}}, '_type': 'Version',
            'id': 10, 'name': 'v1.0', 'description': {'format': 'plain', 'raw': '', 'html': ''}, 'startDate': None,
            'endDate': None, 'status': 'Open'}]}}

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
        versions_by_project_model = cls()

        versions_by_project_model.additional_properties = d
        return versions_by_project_model

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
