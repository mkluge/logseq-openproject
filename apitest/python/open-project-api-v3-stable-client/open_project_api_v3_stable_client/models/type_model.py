import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.type_model_links import TypeModelLinks


T = TypeVar("T", bound="TypeModel")


@attr.s(auto_attribs=True)
class TypeModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/types/1'}}, '_type': 'Type', 'id': 1, 'name': 'Bug', 'color': '#ff0000',
            'position': 1, 'isDefault': True, 'isMilestone': False, 'createdAt': '2014-05-21T08:51:20Z', 'updatedAt':
            '2014-05-21T08:51:20Z'}

    Attributes:
        id (Union[Unset, int]): Type id
        name (Union[Unset, str]): Type name
        color (Union[Unset, str]): The color used to represent this type
        position (Union[Unset, int]): Sort index of the type
        is_default (Union[Unset, bool]): Is this type active by default in new projects?
        is_milestone (Union[Unset, bool]): Do work packages of this type represent a milestone?
        created_at (Union[Unset, datetime.datetime]): Time of creation
        updated_at (Union[Unset, datetime.datetime]): Time of the most recent change to the user
        field_links (Union[Unset, TypeModelLinks]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    color: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    is_default: Union[Unset, bool] = UNSET
    is_milestone: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    field_links: Union[Unset, "TypeModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        color = self.color
        position = self.position
        is_default = self.is_default
        is_milestone = self.is_milestone
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if color is not UNSET:
            field_dict["color"] = color
        if position is not UNSET:
            field_dict["position"] = position
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if is_milestone is not UNSET:
            field_dict["isMilestone"] = is_milestone
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.type_model_links import TypeModelLinks

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        color = d.pop("color", UNSET)

        position = d.pop("position", UNSET)

        is_default = d.pop("isDefault", UNSET)

        is_milestone = d.pop("isMilestone", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, TypeModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = TypeModelLinks.from_dict(_field_links)

        type_model = cls(
            id=id,
            name=name,
            color=color,
            position=position,
            is_default=is_default,
            is_milestone=is_milestone,
            created_at=created_at,
            updated_at=updated_at,
            field_links=field_links,
        )

        type_model.additional_properties = d
        return type_model

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
