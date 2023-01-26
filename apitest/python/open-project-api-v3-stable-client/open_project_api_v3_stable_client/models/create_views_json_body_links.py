from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_views_json_body_links_query import CreateViewsJsonBodyLinksQuery


T = TypeVar("T", bound="CreateViewsJsonBodyLinks")


@attr.s(auto_attribs=True)
class CreateViewsJsonBodyLinks:
    """
    Attributes:
        query (Union[Unset, CreateViewsJsonBodyLinksQuery]):
    """

    query: Union[Unset, "CreateViewsJsonBodyLinksQuery"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_views_json_body_links_query import CreateViewsJsonBodyLinksQuery

        d = src_dict.copy()
        _query = d.pop("query", UNSET)
        query: Union[Unset, CreateViewsJsonBodyLinksQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = CreateViewsJsonBodyLinksQuery.from_dict(_query)

        create_views_json_body_links = cls(
            query=query,
        )

        create_views_json_body_links.additional_properties = d
        return create_views_json_body_links

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
