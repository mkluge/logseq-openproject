from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_filter_instance_schema_model_links import QueryFilterInstanceSchemaModelLinks


T = TypeVar("T", bound="QueryFilterInstanceSchemaModel")


@attr.s(auto_attribs=True)
class QueryFilterInstanceSchemaModel:
    """
    Example:
        {'_type': 'QueryFilterInstanceSchema', '_dependencies': [{'_type': 'SchemaDependency', 'on': 'operator',
            'dependencies': {'/api/v3/queries/operators/=': {'values': {'type': '[]User', 'name': 'Values', 'required':
            True, 'hasDefault': False, 'writable': True, '_links': {}}}, '/api/v3/queries/operators/!': {'values': {'type':
            '[]User', 'name': 'Values', 'required': True, 'hasDefault': False, 'writable': True, '_links': {}}}}}], 'name':
            {'type': 'String', 'name': 'Name', 'required': True, 'hasDefault': True, 'writable': False}, 'filter': {'type':
            'QueryFilter', 'name': 'Filter', 'required': True, 'hasDefault': False, 'writable': True, '_links': {}},
            '_links': {'self': {'href': '/api/v3/queries/filter_instance_schemas/author'}, 'filter': {'href':
            '/api/v3/queries/filters/author', 'title': 'Author'}}}

    Attributes:
        name (str): Describes the name attribute
        filter_ (str): QuerySortBy name
        field_links (Union[Unset, QueryFilterInstanceSchemaModelLinks]):
    """

    name: str
    filter_: str
    field_links: Union[Unset, "QueryFilterInstanceSchemaModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        filter_ = self.filter_
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "filter": filter_,
            }
        )
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_filter_instance_schema_model_links import QueryFilterInstanceSchemaModelLinks

        d = src_dict.copy()
        name = d.pop("name")

        filter_ = d.pop("filter")

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, QueryFilterInstanceSchemaModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = QueryFilterInstanceSchemaModelLinks.from_dict(_field_links)

        query_filter_instance_schema_model = cls(
            name=name,
            filter_=filter_,
            field_links=field_links,
        )

        query_filter_instance_schema_model.additional_properties = d
        return query_filter_instance_schema_model

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
