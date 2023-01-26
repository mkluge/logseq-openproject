from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_collection_model_links_change_size import NotificationCollectionModelLinksChangeSize
    from ..models.notification_collection_model_links_jump_to import NotificationCollectionModelLinksJumpTo
    from ..models.notification_collection_model_links_self import NotificationCollectionModelLinksSelf


T = TypeVar("T", bound="NotificationCollectionModelLinks")


@attr.s(auto_attribs=True)
class NotificationCollectionModelLinks:
    """
    Attributes:
        self_ (NotificationCollectionModelLinksSelf):
        jump_to (Union[Unset, NotificationCollectionModelLinksJumpTo]):
        change_size (Union[Unset, NotificationCollectionModelLinksChangeSize]):
    """

    self_: "NotificationCollectionModelLinksSelf"
    jump_to: Union[Unset, "NotificationCollectionModelLinksJumpTo"] = UNSET
    change_size: Union[Unset, "NotificationCollectionModelLinksChangeSize"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        jump_to: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.jump_to, Unset):
            jump_to = self.jump_to.to_dict()

        change_size: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.change_size, Unset):
            change_size = self.change_size.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
            }
        )
        if jump_to is not UNSET:
            field_dict["jumpTo"] = jump_to
        if change_size is not UNSET:
            field_dict["changeSize"] = change_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notification_collection_model_links_change_size import NotificationCollectionModelLinksChangeSize
        from ..models.notification_collection_model_links_jump_to import NotificationCollectionModelLinksJumpTo
        from ..models.notification_collection_model_links_self import NotificationCollectionModelLinksSelf

        d = src_dict.copy()
        self_ = NotificationCollectionModelLinksSelf.from_dict(d.pop("self"))

        _jump_to = d.pop("jumpTo", UNSET)
        jump_to: Union[Unset, NotificationCollectionModelLinksJumpTo]
        if isinstance(_jump_to, Unset):
            jump_to = UNSET
        else:
            jump_to = NotificationCollectionModelLinksJumpTo.from_dict(_jump_to)

        _change_size = d.pop("changeSize", UNSET)
        change_size: Union[Unset, NotificationCollectionModelLinksChangeSize]
        if isinstance(_change_size, Unset):
            change_size = UNSET
        else:
            change_size = NotificationCollectionModelLinksChangeSize.from_dict(_change_size)

        notification_collection_model_links = cls(
            self_=self_,
            jump_to=jump_to,
            change_size=change_size,
        )

        notification_collection_model_links.additional_properties = d
        return notification_collection_model_links

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
