from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role_model_links import RoleModelLinks


T = TypeVar("T", bound="RoleModel")


@attr.s(auto_attribs=True)
class RoleModel:
    """
    Example:
        {'_type': 'Role', 'id': 3, 'name': 'Manager', '_links': {'self': {'href': '/api/v3/roles/3', 'title':
            'Manager'}}}

    Attributes:
        name (str): Role name
        id (Union[Unset, int]): Role id
        field_links (Union[Unset, RoleModelLinks]):
    """

    name: str
    id: Union[Unset, int] = UNSET
    field_links: Union[Unset, "RoleModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.role_model_links import RoleModelLinks

        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, RoleModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RoleModelLinks.from_dict(_field_links)

        role_model = cls(
            name=name,
            id=id,
            field_links=field_links,
        )

        role_model.additional_properties = d
        return role_model

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
