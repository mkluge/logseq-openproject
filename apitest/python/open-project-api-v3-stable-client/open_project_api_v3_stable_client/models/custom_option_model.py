from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_option_model_links import CustomOptionModelLinks


T = TypeVar("T", bound="CustomOptionModel")


@attr.s(auto_attribs=True)
class CustomOptionModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/custom_options/1'}}, '_type': 'CustomOption', 'value': 'Foo'}

    Attributes:
        id (Union[Unset, int]): The identifier
        value (Union[Unset, str]): The value defined for this custom option
        field_links (Union[Unset, CustomOptionModelLinks]):
    """

    id: Union[Unset, int] = UNSET
    value: Union[Unset, str] = UNSET
    field_links: Union[Unset, "CustomOptionModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        value = self.value
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_option_model_links import CustomOptionModelLinks

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, CustomOptionModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = CustomOptionModelLinks.from_dict(_field_links)

        custom_option_model = cls(
            id=id,
            value=value,
            field_links=field_links,
        )

        custom_option_model.additional_properties = d
        return custom_option_model

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
