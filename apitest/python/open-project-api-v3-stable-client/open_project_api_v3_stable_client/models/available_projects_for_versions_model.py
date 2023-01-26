from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="AvailableProjectsForVersionsModel")


@attr.s(auto_attribs=True)
class AvailableProjectsForVersionsModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/versions/available_projects'}}, '_type': 'Collection', 'total': 2,
            'count': 2, '_embedded': {'elements': [{'_type': 'Project', '_links': {'self': {'href': '/api/v3/projects/6',
            'title': 'A project'}, 'editWorkPackage': {'href': '/api/v3/work_packages/{id}/form', 'templated': True,
            'method': 'post'}, 'createWorkPackage': {'href': '/api/v3/projects/6/work_packages/form', 'method': 'post'},
            'createWorkPackageImmediate': {'href': '/api/v3/projects/6/work_packages', 'method': 'post'}, 'categories':
            {'href': '/api/v3/projects/6/categories'}, 'versions': {'href': '/api/v3/projects/6/versions'}}, 'id': 6,
            'identifier': 'a_project', 'name': 'A project', 'description': 'Eveniet molestias omnis quis aut qui eum
            adipisci. Atque aut aut in exercitationem adipisci amet. Nisi asperiores quia ratione veritatis enim
            exercitationem magnam. Aut fuga architecto adipisci nihil. Et repellat pariatur. Aliquam et sed perferendis
            nostrum quaerat. Fugit doloremque voluptatem.', 'createdAt': '2015-07-06T13:28:14+00:00', 'updatedAt':
            '2015-10-01T09:55:02+00:00', 'type': 'Customer Project'}, {'_type': 'Project', '_links': {'self': {'href':
            '/api/v3/projects/14', 'title': 'Another project'}, 'createWorkPackage': {'href':
            '/api/v3/projects/14/work_packages/form', 'method': 'post'}, 'createWorkPackageImmediate': {'href':
            '/api/v3/projects/14/work_packages', 'method': 'post'}, 'categories': {'href':
            '/api/v3/projects/14/categories'}, 'versions': {'href': '/api/v3/projects/14/versions'}}, 'id': 14,
            'identifier': 'another_project', 'name': 'Another project', 'description': '', 'createdAt':
            '2016-02-29T12:50:20+00:00', 'updatedAt': '2016-02-29T12:50:20+00:00', 'type': None}]}}

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
        available_projects_for_versions_model = cls()

        available_projects_for_versions_model.additional_properties = d
        return available_projects_for_versions_model

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
