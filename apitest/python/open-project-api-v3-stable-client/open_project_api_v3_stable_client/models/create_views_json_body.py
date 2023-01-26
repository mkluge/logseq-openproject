from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_views_json_body_links import CreateViewsJsonBodyLinks


T = TypeVar("T", bound="CreateViewsJsonBody")


@attr.s(auto_attribs=True)
class CreateViewsJsonBody:
    """
    Attributes:
        field_links (Union[Unset, CreateViewsJsonBodyLinks]):
    """

    field_links: Union[Unset, "CreateViewsJsonBodyLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_views_json_body_links import CreateViewsJsonBodyLinks

        d = src_dict.copy()
        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CreateViewsJsonBodyLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CreateViewsJsonBodyLinks.from_dict(_field_links)

        create_views_json_body = cls(
            field_links=field_links,
        )

        create_views_json_body.additional_properties = d
        return create_views_json_body

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
