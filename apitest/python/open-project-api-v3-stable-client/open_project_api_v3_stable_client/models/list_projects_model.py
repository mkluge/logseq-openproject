from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ListProjectsModel")


@attr.s(auto_attribs=True)
class ListProjectsModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/projects'}, 'representations': [{'href': '/projects.csv?filters=%5B%7B%22n
            ameAndIdentifier%22%3A%7B%22operator%22%3A%22%3D%22%2C%22values%22%3A%5B%22open%22%5D%7D%7D%5D&offset=1&pageSize
            =50', 'identifier': 'csv', 'type': 'text/csv', 'title': 'CSV'}, {'href': '/projects.xls?filters=%5B%7B%22nameAnd
            Identifier%22%3A%7B%22operator%22%3A%22%3D%22%2C%22values%22%3A%5B%22open%22%5D%7D%7D%5D&offset=1&pageSize=50',
            'identifier': 'xls', 'type': 'application/vnd.ms-excel', 'title': 'XLS'}]}, '_type': 'Collection', 'total': 2,
            'count': 2, '_embedded': {'elements': [{'_type': 'Project', '_links': {'self': {'href': '/api/v3/projects/6',
            'title': 'A project'}, 'createWorkPackage': {'href': '/api/v3/projects/6/work_packages/form', 'method': 'post'},
            'createWorkPackageImmediate': {'href': '/api/v3/projects/6/work_packages', 'method': 'post'}, 'categories':
            {'href': '/api/v3/projects/6/categories'}, 'versions': {'href': '/api/v3/projects/6/versions'}, 'projects':
            {'href': '/api/v3/projects/123'}, 'status': {'href': '/api/v3/project_statuses/on_track', 'title': 'On track'}},
            'id': 6, 'identifier': 'a_project', 'name': 'A project', 'active': True, 'statusExplanation': {'format':
            'markdown', 'raw': 'Everything **fine**', 'html': '<p>Everything <strong>fine</strong></p>'}, 'public': False,
            'description': {'format': 'markdown', 'raw': 'Lorem **ipsum** dolor sit amet', 'html': '<p>Lorem
            <strong>ipsum</strong> dolor sit amet</p>'}, 'createdAt': '2015-07-06T13:28:14+00:00', 'updatedAt':
            '2015-10-01T09:55:02+00:00', 'type': 'Customer Project'}, {'_type': 'Project', '_links': {'self': {'href':
            '/api/v3/projects/14', 'title': 'Another project'}, 'createWorkPackage': {'href':
            '/api/v3/projects/14/work_packages/form', 'method': 'post'}, 'createWorkPackageImmediate': {'href':
            '/api/v3/projects/14/work_packages', 'method': 'post'}, 'categories': {'href':
            '/api/v3/projects/14/categories'}, 'versions': {'href': '/api/v3/projects/14/versions'}, 'projects': {'href':
            None}, 'status': {'href': '/api/v3/project_statuses/off_track', 'title': 'Off track'}}, 'id': 14, 'identifier':
            'another_project', 'name': 'Another project', 'active': False, 'statusExplanation': {'format': 'markdown',
            'raw': 'Uh **oh**', 'html': '<p>Uh <strong>oh</strong></p>'}, 'public': True, 'description': {'format':
            'markdown', 'raw': '', 'html': ''}, 'createdAt': '2016-02-29T12:50:20+00:00', 'updatedAt':
            '2016-02-29T12:50:20+00:00', 'type': None}]}}

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
        list_projects_model = cls()

        list_projects_model.additional_properties = d
        return list_projects_model

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
