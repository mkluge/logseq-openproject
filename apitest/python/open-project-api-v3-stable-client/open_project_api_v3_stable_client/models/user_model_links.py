from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_model_links_delete import UserModelLinksDelete
    from ..models.user_model_links_lock import UserModelLinksLock
    from ..models.user_model_links_memberships import UserModelLinksMemberships
    from ..models.user_model_links_self import UserModelLinksSelf
    from ..models.user_model_links_show_user import UserModelLinksShowUser
    from ..models.user_model_links_unlock import UserModelLinksUnlock
    from ..models.user_model_links_update_immediately import UserModelLinksUpdateImmediately


T = TypeVar("T", bound="UserModelLinks")


@attr.s(auto_attribs=True)
class UserModelLinks:
    """
    Attributes:
        self_ (UserModelLinksSelf):
        memberships (UserModelLinksMemberships):
        show_user (UserModelLinksShowUser):
        update_immediately (Union[Unset, UserModelLinksUpdateImmediately]):
        lock (Union[Unset, UserModelLinksLock]):
        unlock (Union[Unset, UserModelLinksUnlock]):
        delete (Union[Unset, UserModelLinksDelete]):
    """

    self_: "UserModelLinksSelf"
    memberships: "UserModelLinksMemberships"
    show_user: "UserModelLinksShowUser"
    update_immediately: Union[Unset, "UserModelLinksUpdateImmediately"] = UNSET
    lock: Union[Unset, "UserModelLinksLock"] = UNSET
    unlock: Union[Unset, "UserModelLinksUnlock"] = UNSET
    delete: Union[Unset, "UserModelLinksDelete"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        memberships = self.memberships.to_dict()

        show_user = self.show_user.to_dict()

        update_immediately: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_immediately, Unset):
            update_immediately = self.update_immediately.to_dict()

        lock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock, Unset):
            lock = self.lock.to_dict()

        unlock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock, Unset):
            unlock = self.unlock.to_dict()

        delete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delete, Unset):
            delete = self.delete.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "memberships": memberships,
                "showUser": show_user,
            }
        )
        if update_immediately is not UNSET:
            field_dict["updateImmediately"] = update_immediately
        if lock is not UNSET:
            field_dict["lock"] = lock
        if unlock is not UNSET:
            field_dict["unlock"] = unlock
        if delete is not UNSET:
            field_dict["delete"] = delete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_model_links_delete import UserModelLinksDelete
        from ..models.user_model_links_lock import UserModelLinksLock
        from ..models.user_model_links_memberships import UserModelLinksMemberships
        from ..models.user_model_links_self import UserModelLinksSelf
        from ..models.user_model_links_show_user import UserModelLinksShowUser
        from ..models.user_model_links_unlock import UserModelLinksUnlock
        from ..models.user_model_links_update_immediately import UserModelLinksUpdateImmediately

        d = src_dict.copy()
        self_ = UserModelLinksSelf.from_dict(d.pop("self"))

        memberships = UserModelLinksMemberships.from_dict(d.pop("memberships"))

        show_user = UserModelLinksShowUser.from_dict(d.pop("showUser"))

        _update_immediately = d.pop("updateImmediately", UNSET)
        update_immediately: Union[Unset, UserModelLinksUpdateImmediately]
        if isinstance(_update_immediately, Unset):
            update_immediately = UNSET
        else:
            update_immediately = UserModelLinksUpdateImmediately.from_dict(_update_immediately)

        _lock = d.pop("lock", UNSET)
        lock: Union[Unset, UserModelLinksLock]
        if isinstance(_lock, Unset):
            lock = UNSET
        else:
            lock = UserModelLinksLock.from_dict(_lock)

        _unlock = d.pop("unlock", UNSET)
        unlock: Union[Unset, UserModelLinksUnlock]
        if isinstance(_unlock, Unset):
            unlock = UNSET
        else:
            unlock = UserModelLinksUnlock.from_dict(_unlock)

        _delete = d.pop("delete", UNSET)
        delete: Union[Unset, UserModelLinksDelete]
        if isinstance(_delete, Unset):
            delete = UNSET
        else:
            delete = UserModelLinksDelete.from_dict(_delete)

        user_model_links = cls(
            self_=self_,
            memberships=memberships,
            show_user=show_user,
            update_immediately=update_immediately,
            lock=lock,
            unlock=unlock,
            delete=delete,
        )

        user_model_links.additional_properties = d
        return user_model_links

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
