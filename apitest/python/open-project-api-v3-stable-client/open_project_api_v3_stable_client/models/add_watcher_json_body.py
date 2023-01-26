from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_watcher_json_body_user import AddWatcherJsonBodyUser


T = TypeVar("T", bound="AddWatcherJsonBody")


@attr.s(auto_attribs=True)
class AddWatcherJsonBody:
    """
    Example:
        {'user': {'href': '/api/v3/users/1'}}

    Attributes:
        user (Union[Unset, AddWatcherJsonBodyUser]):
    """

    user: Union[Unset, "AddWatcherJsonBodyUser"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.add_watcher_json_body_user import AddWatcherJsonBodyUser

        d = src_dict.copy()
        _user = d.pop("user", UNSET)
        user: Union[Unset, AddWatcherJsonBodyUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = AddWatcherJsonBodyUser.from_dict(_user)

        add_watcher_json_body = cls(
            user=user,
        )

        add_watcher_json_body.additional_properties = d
        return add_watcher_json_body

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
