from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CategoriesByProjectModel")


@attr.s(auto_attribs=True)
class CategoriesByProjectModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/projects/11/categories'}}, 'total': 2, 'count': 2, '_type': 'Collection',
            '_embedded': {'elements': [{'_links': {'self': {'href': '/api/v3/categories/10', 'title': 'Category with
            assignee'}, 'project': {'href': '/api/v3/projects/11', 'title': 'Example project'}, 'defaultAssignee': {'href':
            '/api/v3/users/42', 'title': 'John Sheppard'}}, '_type': 'Category', 'id': 10, 'name': 'Foo'}, {'_links':
            {'self': {'href': '/api/v3/categories/11'}, 'project': {'href': '/api/v3/projects/11'}}, '_type': 'Category',
            'id': 11, 'name': 'Bar'}]}}

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
        categories_by_project_model = cls()

        categories_by_project_model.additional_properties = d
        return categories_by_project_model

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
