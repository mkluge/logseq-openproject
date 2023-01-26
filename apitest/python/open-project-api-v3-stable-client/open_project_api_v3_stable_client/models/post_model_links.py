from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_model_links_add_attachment import PostModelLinksAddAttachment


T = TypeVar("T", bound="PostModelLinks")


@attr.s(auto_attribs=True)
class PostModelLinks:
    """
    Attributes:
        add_attachment (Union[Unset, PostModelLinksAddAttachment]):
    """

    add_attachment: Union[Unset, "PostModelLinksAddAttachment"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        add_attachment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.add_attachment, Unset):
            add_attachment = self.add_attachment.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_attachment is not UNSET:
            field_dict["addAttachment"] = add_attachment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_model_links_add_attachment import PostModelLinksAddAttachment

        d = src_dict.copy()
        _add_attachment = d.pop("addAttachment", UNSET)
        add_attachment: Union[Unset, PostModelLinksAddAttachment]
        if isinstance(_add_attachment, Unset):
            add_attachment = UNSET
        else:
            add_attachment = PostModelLinksAddAttachment.from_dict(_add_attachment)

        post_model_links = cls(
            add_attachment=add_attachment,
        )

        post_model_links.additional_properties = d
        return post_model_links

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
