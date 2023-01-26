from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_model_links_delete import GroupModelLinksDelete
    from ..models.group_model_links_members import GroupModelLinksMembers
    from ..models.group_model_links_memberships import GroupModelLinksMemberships
    from ..models.group_model_links_self import GroupModelLinksSelf
    from ..models.group_model_links_update_immediately import GroupModelLinksUpdateImmediately


T = TypeVar("T", bound="GroupModelLinks")


@attr.s(auto_attribs=True)
class GroupModelLinks:
    """
    Attributes:
        self_ (GroupModelLinksSelf):
        delete (Union[Unset, GroupModelLinksDelete]):
        update_immediately (Union[Unset, GroupModelLinksUpdateImmediately]):
        memberships (Union[Unset, GroupModelLinksMemberships]):
        members (Union[Unset, GroupModelLinksMembers]):
    """

    self_: "GroupModelLinksSelf"
    delete: Union[Unset, "GroupModelLinksDelete"] = UNSET
    update_immediately: Union[Unset, "GroupModelLinksUpdateImmediately"] = UNSET
    memberships: Union[Unset, "GroupModelLinksMemberships"] = UNSET
    members: Union[Unset, "GroupModelLinksMembers"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        delete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delete, Unset):
            delete = self.delete.to_dict()

        update_immediately: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_immediately, Unset):
            update_immediately = self.update_immediately.to_dict()

        memberships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.memberships, Unset):
            memberships = self.memberships.to_dict()

        members: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.members, Unset):
            members = self.members.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
            }
        )
        if delete is not UNSET:
            field_dict["delete"] = delete
        if update_immediately is not UNSET:
            field_dict["updateImmediately"] = update_immediately
        if memberships is not UNSET:
            field_dict["memberships"] = memberships
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_model_links_delete import GroupModelLinksDelete
        from ..models.group_model_links_members import GroupModelLinksMembers
        from ..models.group_model_links_memberships import GroupModelLinksMemberships
        from ..models.group_model_links_self import GroupModelLinksSelf
        from ..models.group_model_links_update_immediately import GroupModelLinksUpdateImmediately

        d = src_dict.copy()
        self_ = GroupModelLinksSelf.from_dict(d.pop("self"))

        _delete = d.pop("delete", UNSET)
        delete: Union[Unset, GroupModelLinksDelete]
        if isinstance(_delete, Unset):
            delete = UNSET
        else:
            delete = GroupModelLinksDelete.from_dict(_delete)

        _update_immediately = d.pop("updateImmediately", UNSET)
        update_immediately: Union[Unset, GroupModelLinksUpdateImmediately]
        if isinstance(_update_immediately, Unset):
            update_immediately = UNSET
        else:
            update_immediately = GroupModelLinksUpdateImmediately.from_dict(_update_immediately)

        _memberships = d.pop("memberships", UNSET)
        memberships: Union[Unset, GroupModelLinksMemberships]
        if isinstance(_memberships, Unset):
            memberships = UNSET
        else:
            memberships = GroupModelLinksMemberships.from_dict(_memberships)

        _members = d.pop("members", UNSET)
        members: Union[Unset, GroupModelLinksMembers]
        if isinstance(_members, Unset):
            members = UNSET
        else:
            members = GroupModelLinksMembers.from_dict(_members)

        group_model_links = cls(
            self_=self_,
            delete=delete,
            update_immediately=update_immediately,
            memberships=memberships,
            members=members,
        )

        group_model_links.additional_properties = d
        return group_model_links

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
