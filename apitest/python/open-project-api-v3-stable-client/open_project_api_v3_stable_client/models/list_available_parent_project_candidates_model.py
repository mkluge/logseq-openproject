from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ListAvailableParentProjectCandidatesModel")


@attr.s(auto_attribs=True)
class ListAvailableParentProjectCandidatesModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/projects/available_parent_projects?of=123'}}, '_type': 'Collection',
            'total': 2, 'count': 2, '_embedded': {'elements': [{'_type': 'Project', '_links': {'self': {'href':
            '/api/v3/projects/6', 'title': 'A project'}, 'createWorkPackage': {'href':
            '/api/v3/projects/6/work_packages/form', 'method': 'post'}, 'createWorkPackageImmediate': {'href':
            '/api/v3/projects/6/work_packages', 'method': 'post'}, 'categories': {'href': '/api/v3/projects/6/categories'},
            'versions': {'href': '/api/v3/projects/6/versions'}, 'status': {'href': '/api/v3/project_statuses/on_track',
            'title': 'On track'}}, 'id': 6, 'identifier': 'a_project', 'name': 'A project', 'active': True,
            'statusExplanation': {'format': 'markdown', 'raw': 'Everything **fine**', 'html': '<p>Everything
            <strong>fine</strong></p>'}, 'public': False, 'description': {'format': 'markdown', 'raw': 'Lorem **ipsum**
            dolor sit amet', 'html': '<p>Lorem <strong>ipsum</strong> dolor sit amet</p>'}, 'createdAt':
            '2015-07-06T13:28:14+00:00', 'updatedAt': '2015-10-01T09:55:02+00:00', 'type': 'Customer Project'}, {'_type':
            'Project', '_links': {'self': {'href': '/api/v3/projects/14', 'title': 'Another project'}, 'createWorkPackage':
            {'href': '/api/v3/projects/14/work_packages/form', 'method': 'post'}, 'createWorkPackageImmediate': {'href':
            '/api/v3/projects/14/work_packages', 'method': 'post'}, 'categories': {'href':
            '/api/v3/projects/14/categories'}, 'versions': {'href': '/api/v3/projects/14/versions'}, 'status': {'href':
            '/api/v3/project_statuses/on_track', 'title': 'On track'}}, 'id': 14, 'identifier': 'another_project', 'name':
            'Another project', 'active': True, 'statusExplanation': {'format': 'markdown', 'raw': 'Everything super
            **fine**', 'html': '<p>Everything super <strong>fine</strong></p>'}, 'public': True, 'description': {'format':
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
        list_available_parent_project_candidates_model = cls()

        list_available_parent_project_candidates_model.additional_properties = d
        return list_available_parent_project_candidates_model

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
