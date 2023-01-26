from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_model_links import StatusModelLinks


T = TypeVar("T", bound="StatusModel")


@attr.s(auto_attribs=True)
class StatusModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/statuses/1'}}, '_type': 'Status', 'id': 1, 'name': 'New', 'position': 1,
            'isDefault': True, 'isClosed': False, 'defaultDoneRatio': 0}

    Attributes:
        id (Union[Unset, int]): Status id
        name (Union[Unset, str]): Status name
        position (Union[Unset, int]): Sort index of the status
        is_default (Union[Unset, bool]):
        is_closed (Union[Unset, bool]): are tickets of this status considered closed?
        is_readonly (Union[Unset, bool]): are tickets of this status read only?
        default_done_ratio (Union[Unset, int]): The percentageDone being applied when changing to this status
        field_links (Union[Unset, StatusModelLinks]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    is_default: Union[Unset, bool] = UNSET
    is_closed: Union[Unset, bool] = UNSET
    is_readonly: Union[Unset, bool] = UNSET
    default_done_ratio: Union[Unset, int] = UNSET
    field_links: Union[Unset, "StatusModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        position = self.position
        is_default = self.is_default
        is_closed = self.is_closed
        is_readonly = self.is_readonly
        default_done_ratio = self.default_done_ratio
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
        if is_closed is not UNSET:
            field_dict["isClosed"] = is_closed
        if is_readonly is not UNSET:
            field_dict["isReadonly"] = is_readonly
        if default_done_ratio is not UNSET:
            field_dict["defaultDoneRatio"] = default_done_ratio
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.status_model_links import StatusModelLinks

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        position = d.pop("position", UNSET)

        is_default = d.pop("isDefault", UNSET)

        is_closed = d.pop("isClosed", UNSET)

        is_readonly = d.pop("isReadonly", UNSET)

        default_done_ratio = d.pop("defaultDoneRatio", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, StatusModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = StatusModelLinks.from_dict(_field_links)

        status_model = cls(
            id=id,
            name=name,
            position=position,
            is_default=is_default,
            is_closed=is_closed,
            is_readonly=is_readonly,
            default_done_ratio=default_done_ratio,
            field_links=field_links,
        )

        status_model.additional_properties = d
        return status_model

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
