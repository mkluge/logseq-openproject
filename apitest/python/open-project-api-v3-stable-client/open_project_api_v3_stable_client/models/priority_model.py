from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.priority_model_links import PriorityModelLinks


T = TypeVar("T", bound="PriorityModel")


@attr.s(auto_attribs=True)
class PriorityModel:
    """
    Example:
        {'_type': 'Priority', '_links': {'self': {'href': '/api/v3/priorities/1', 'title': 'Low'}}, 'id': 1, 'name':
            'Low', 'position': 1, 'isDefault': False, 'isActive': True}

    Attributes:
        id (Union[Unset, int]): Priority id
        name (Union[Unset, str]): Priority name
        position (Union[Unset, int]): Sort index of the priority
        is_default (Union[Unset, bool]): Indicates whether this is the default value
        is_active (Union[Unset, bool]): Indicates whether the priority is available
        field_links (Union[Unset, PriorityModelLinks]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    is_default: Union[Unset, bool] = UNSET
    is_active: Union[Unset, bool] = UNSET
    field_links: Union[Unset, "PriorityModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        position = self.position
        is_default = self.is_default
        is_active = self.is_active
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
        if position is not UNSET:
            field_dict["position"] = position
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.priority_model_links import PriorityModelLinks

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        position = d.pop("position", UNSET)

        is_default = d.pop("isDefault", UNSET)

        is_active = d.pop("isActive", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, PriorityModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = PriorityModelLinks.from_dict(_field_links)

        priority_model = cls(
            id=id,
            name=name,
            position=position,
            is_default=is_default,
            is_active=is_active,
            field_links=field_links,
        )

        priority_model.additional_properties = d
        return priority_model

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
