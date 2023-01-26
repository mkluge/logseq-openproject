from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_group_json_body_links import UpdateGroupJsonBodyLinks


T = TypeVar("T", bound="UpdateGroupJsonBody")


@attr.s(auto_attribs=True)
class UpdateGroupJsonBody:
    """
    Example:
        {'_links': {'members': [{'href': '/api/v3/users/363'}, {'href': '/api/v3/users/60'}]}, 'name': 'The group'}

    Attributes:
        field_links (Union[Unset, UpdateGroupJsonBodyLinks]):
        name (Union[Unset, str]):
    """

    field_links: Union[Unset, "UpdateGroupJsonBodyLinks"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_group_json_body_links import UpdateGroupJsonBodyLinks

        d = src_dict.copy()
        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, UpdateGroupJsonBodyLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = UpdateGroupJsonBodyLinks.from_dict(_field_links)

        name = d.pop("name", UNSET)

        update_group_json_body = cls(
            field_links=field_links,
            name=name,
        )

        update_group_json_body.additional_properties = d
        return update_group_json_body

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
