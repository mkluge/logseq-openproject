from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_group_json_body_links_members_item import CreateGroupJsonBodyLinksMembersItem


T = TypeVar("T", bound="CreateGroupJsonBodyLinks")


@attr.s(auto_attribs=True)
class CreateGroupJsonBodyLinks:
    """
    Attributes:
        members (Union[Unset, List['CreateGroupJsonBodyLinksMembersItem']]):
    """

    members: Union[Unset, List["CreateGroupJsonBodyLinksMembersItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()

                members.append(members_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_group_json_body_links_members_item import CreateGroupJsonBodyLinksMembersItem

        d = src_dict.copy()
        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = CreateGroupJsonBodyLinksMembersItem.from_dict(members_item_data)

            members.append(members_item)

        create_group_json_body_links = cls(
            members=members,
        )

        create_group_json_body_links.additional_properties = d
        return create_group_json_body_links

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
