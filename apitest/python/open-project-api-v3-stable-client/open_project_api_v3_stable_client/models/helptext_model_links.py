from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.helptext_model_links_edit_text import HelptextModelLinksEditText
    from ..models.helptext_model_links_self import HelptextModelLinksSelf


T = TypeVar("T", bound="HelptextModelLinks")


@attr.s(auto_attribs=True)
class HelptextModelLinks:
    """
    Attributes:
        self_ (HelptextModelLinksSelf):
        edit_text (Union[Unset, HelptextModelLinksEditText]):
    """

    self_: "HelptextModelLinksSelf"
    edit_text: Union[Unset, "HelptextModelLinksEditText"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        edit_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_text, Unset):
            edit_text = self.edit_text.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
            }
        )
        if edit_text is not UNSET:
            field_dict["editText"] = edit_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.helptext_model_links_edit_text import HelptextModelLinksEditText
        from ..models.helptext_model_links_self import HelptextModelLinksSelf

        d = src_dict.copy()
        self_ = HelptextModelLinksSelf.from_dict(d.pop("self"))

        _edit_text = d.pop("editText", UNSET)
        edit_text: Union[Unset, HelptextModelLinksEditText]
        if isinstance(_edit_text, Unset):
            edit_text = UNSET
        else:
            edit_text = HelptextModelLinksEditText.from_dict(_edit_text)

        helptext_model_links = cls(
            self_=self_,
            edit_text=edit_text,
        )

        helptext_model_links.additional_properties = d
        return helptext_model_links

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
