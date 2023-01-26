import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.membership_model_links import MembershipModelLinks


T = TypeVar("T", bound="MembershipModel")


@attr.s(auto_attribs=True)
class MembershipModel:
    """
    Attributes:
        created_at (datetime.datetime): Time of creation
        updated_at (datetime.datetime): Time of latest update
        id (Union[Unset, int]): Membership id
        field_links (Union[Unset, MembershipModelLinks]):
    """

    created_at: datetime.datetime
    updated_at: datetime.datetime
    id: Union[Unset, int] = UNSET
    field_links: Union[Unset, "MembershipModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        id = self.id
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.membership_model_links import MembershipModelLinks

        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        id = d.pop("id", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, MembershipModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = MembershipModelLinks.from_dict(_field_links)

        membership_model = cls(
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            field_links=field_links,
        )

        membership_model.additional_properties = d
        return membership_model

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
