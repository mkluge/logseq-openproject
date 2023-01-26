from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="WorkPackageActivitiesModel")


@attr.s(auto_attribs=True)
class WorkPackageActivitiesModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/work_packages/1/revisions'}}, 'total': 2, 'count': 2, '_type':
            'Collection', '_embedded': {'elements': [{'_type': 'Activity', '_links': {'self': {'href':
            '/api/v3/activity/1'}, 'workPackage': {'href': '/api/v3/work_packages/1'}, 'user': {'href': '/api/v3/users/1'}},
            'id': 1, 'details': [], 'comment': {'format': 'markdown', 'raw': 'Lorem ipsum dolor sit amet.', 'html':
            '<p>Lorem ipsum dolor sit amet.</p>'}, 'createdAt': '2014-05-21T08:51:20Z', 'updatedAt': '2014-05-21T09:14:02Z',
            'version': 1}, {'_type': 'Activity', '_links': {'self': {'href': '/api/v3/activity/2'}, 'workPackage': {'href':
            '/api/v3/work_packages/1'}, 'user': {'href': '/api/v3/users/1'}}, 'id': 2, 'details': [], 'comment': {'format':
            'markdown', 'raw': 'Lorem ipsum dolor sit amet.', 'html': '<p>Lorem ipsum dolor sit amet.</p>'}, 'createdAt':
            '2014-05-21T09:51:22Z', 'updatedAt': '2014-05-21T10:14:02Z', 'version': 2}]}}

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
        work_package_activities_model = cls()

        work_package_activities_model.additional_properties = d
        return work_package_activities_model

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
