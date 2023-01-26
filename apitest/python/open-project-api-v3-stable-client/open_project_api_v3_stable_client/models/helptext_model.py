from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.helptext_model_help_text import HelptextModelHelpText
    from ..models.helptext_model_links import HelptextModelLinks


T = TypeVar("T", bound="HelptextModel")


@attr.s(auto_attribs=True)
class HelptextModel:
    """
    Attributes:
        id (Union[Unset, int]): Help text id
        attribute (Union[Unset, str]): Attribute name
        attribute_caption (Union[Unset, str]): Attribute caption
        help_text (Union[Unset, HelptextModelHelpText]):
        field_links (Union[Unset, HelptextModelLinks]):
    """

    id: Union[Unset, int] = UNSET
    attribute: Union[Unset, str] = UNSET
    attribute_caption: Union[Unset, str] = UNSET
    help_text: Union[Unset, "HelptextModelHelpText"] = UNSET
    field_links: Union[Unset, "HelptextModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        attribute = self.attribute
        attribute_caption = self.attribute_caption
        help_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.help_text, Unset):
            help_text = self.help_text.to_dict()

        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if attribute_caption is not UNSET:
            field_dict["attributeCaption"] = attribute_caption
        if help_text is not UNSET:
            field_dict["helpText"] = help_text
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.helptext_model_help_text import HelptextModelHelpText
        from ..models.helptext_model_links import HelptextModelLinks

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        attribute = d.pop("attribute", UNSET)

        attribute_caption = d.pop("attributeCaption", UNSET)

        _help_text = d.pop("helpText", UNSET)
        help_text: Union[Unset, HelptextModelHelpText]
        if isinstance(_help_text, Unset):
            help_text = UNSET
        else:
            help_text = HelptextModelHelpText.from_dict(_help_text)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, HelptextModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = HelptextModelLinks.from_dict(_field_links)

        helptext_model = cls(
            id=id,
            attribute=attribute,
            attribute_caption=attribute_caption,
            help_text=help_text,
            field_links=field_links,
        )

        helptext_model.additional_properties = d
        return helptext_model

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
