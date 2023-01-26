from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ListProjectsByVersionModel")


@attr.s(auto_attribs=True)
class ListProjectsByVersionModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/versions/2/projects'}}, 'total': 1, 'count': 1, '_type': 'Collection',
            '_embedded': {'elements': [{'_type': 'Project', '_links': {'self': {'href': '/api/v3/projects/1', 'title':
            'Lorem'}, 'categories': {'href': '/api/v3/projects/1/categories'}, 'versions': {'href':
            '/api/v3/projects/1/versions'}, 'status': {'href': '/api/v3/project_statuses/on_track', 'title': 'On track'}},
            'id': 1, 'identifier': 'project_identifier', 'name': 'Project example', 'description': {'format': 'markdown',
            'raw': 'Lorem **ipsum** dolor sit amet', 'html': '<p>Lorem <strong>ipsum</strong> dolor sit amet</p>'},
            'active': True, 'statusExplanation': {'format': 'markdown', 'raw': 'Everything **fine**', 'html': '<p>Everything
            <strong>fine</strong></p>'}, 'createdAt': '2014-05-21T08:51:20Z', 'updatedAt': '2014-05-21T08:51:20Z'}]}}

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
        list_projects_by_version_model = cls()

        list_projects_by_version_model.additional_properties = d
        return list_projects_by_version_model

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
