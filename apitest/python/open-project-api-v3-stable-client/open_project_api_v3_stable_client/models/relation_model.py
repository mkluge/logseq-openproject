from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relation_model_links import RelationModelLinks


T = TypeVar("T", bound="RelationModel")


@attr.s(auto_attribs=True)
class RelationModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/relations/1'}, 'update': {'href': '/api/v3/relations/1/form', 'method':
            'POST'}, 'updateImmediately': {'href': '/api/v3/relations/1', 'method': 'PATCH'}, 'delete': {'href':
            '/api/v3/relations/1', 'method': 'DELETE'}, 'from': {'href': '/api/v3/work_packages/42', 'title': 'Steel
            Delivery'}, 'to': {'href': '/api/v3/work_packages/84', 'title': 'Bending the steel'}}, '_type': 'Relation',
            'id': 1, 'name': 'precedes', 'type': 'precedes', 'reverseType': 'follows', 'description': "We can't bend the
            steel before it's been delivered!", 'delay': 0}

    Attributes:
        id (Union[Unset, int]): Relation ID
        name (Union[Unset, str]): The internationalized name of this kind of relation
        type (Union[Unset, str]): Which kind of relation (blocks, precedes, etc.)
        reverse_type (Union[Unset, str]): The kind of relation from the other WP's perspective
        description (Union[Unset, str]): Short text further describing the relation
        delay (Union[Unset, int]): The delay in days between closing of `from` and start of `to`
        field_links (Union[Unset, RelationModelLinks]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    reverse_type: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    delay: Union[Unset, int] = UNSET
    field_links: Union[Unset, "RelationModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type = self.type
        reverse_type = self.reverse_type
        description = self.description
        delay = self.delay
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
        if type is not UNSET:
            field_dict["type"] = type
        if reverse_type is not UNSET:
            field_dict["reverseType"] = reverse_type
        if description is not UNSET:
            field_dict["description"] = description
        if delay is not UNSET:
            field_dict["delay*"] = delay
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.relation_model_links import RelationModelLinks

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        reverse_type = d.pop("reverseType", UNSET)

        description = d.pop("description", UNSET)

        delay = d.pop("delay*", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, RelationModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RelationModelLinks.from_dict(_field_links)

        relation_model = cls(
            id=id,
            name=name,
            type=type,
            reverse_type=reverse_type,
            description=description,
            delay=delay,
            field_links=field_links,
        )

        relation_model.additional_properties = d
        return relation_model

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
