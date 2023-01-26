from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_model_links import CategoryModelLinks


T = TypeVar("T", bound="CategoryModel")


@attr.s(auto_attribs=True)
class CategoryModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/categories/10', 'title': 'Category with assignee'}, 'project': {'href':
            '/api/v3/projects/11', 'title': 'Example project'}, 'defaultAssignee': {'href': '/api/v3/users/42', 'title':
            'John Sheppard'}}, '_type': 'Category', 'id': 10, 'name': 'Foo'}

    Attributes:
        id (Union[Unset, int]): Category id
        name (Union[Unset, str]): Category name
        field_links (Union[Unset, CategoryModelLinks]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    field_links: Union[Unset, "CategoryModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.category_model_links import CategoryModelLinks

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CategoryModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CategoryModelLinks.from_dict(_field_links)

        category_model = cls(
            id=id,
            name=name,
            field_links=field_links,
        )

        category_model.additional_properties = d
        return category_model

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
