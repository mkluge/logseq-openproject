from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_model_links_star import QueryModelLinksStar
    from ..models.query_model_links_unstar import QueryModelLinksUnstar
    from ..models.query_model_links_update import QueryModelLinksUpdate
    from ..models.query_model_links_update_immediately import QueryModelLinksUpdateImmediately


T = TypeVar("T", bound="QueryModelLinks")


@attr.s(auto_attribs=True)
class QueryModelLinks:
    """
    Attributes:
        star (Union[Unset, QueryModelLinksStar]):
        unstar (Union[Unset, QueryModelLinksUnstar]):
        update (Union[Unset, QueryModelLinksUpdate]):
        update_immediately (Union[Unset, QueryModelLinksUpdateImmediately]):
    """

    star: Union[Unset, "QueryModelLinksStar"] = UNSET
    unstar: Union[Unset, "QueryModelLinksUnstar"] = UNSET
    update: Union[Unset, "QueryModelLinksUpdate"] = UNSET
    update_immediately: Union[Unset, "QueryModelLinksUpdateImmediately"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        star: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.star, Unset):
            star = self.star.to_dict()

        unstar: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unstar, Unset):
            unstar = self.unstar.to_dict()

        update: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.to_dict()

        update_immediately: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_immediately, Unset):
            update_immediately = self.update_immediately.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if star is not UNSET:
            field_dict["star"] = star
        if unstar is not UNSET:
            field_dict["unstar"] = unstar
        if update is not UNSET:
            field_dict["update"] = update
        if update_immediately is not UNSET:
            field_dict["updateImmediately"] = update_immediately

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_model_links_star import QueryModelLinksStar
        from ..models.query_model_links_unstar import QueryModelLinksUnstar
        from ..models.query_model_links_update import QueryModelLinksUpdate
        from ..models.query_model_links_update_immediately import QueryModelLinksUpdateImmediately

        d = src_dict.copy()
        _star = d.pop("star", UNSET)
        star: Union[Unset, QueryModelLinksStar]
        if isinstance(_star, Unset):
            star = UNSET
        else:
            star = QueryModelLinksStar.from_dict(_star)

        _unstar = d.pop("unstar", UNSET)
        unstar: Union[Unset, QueryModelLinksUnstar]
        if isinstance(_unstar, Unset):
            unstar = UNSET
        else:
            unstar = QueryModelLinksUnstar.from_dict(_unstar)

        _update = d.pop("update", UNSET)
        update: Union[Unset, QueryModelLinksUpdate]
        if isinstance(_update, Unset):
            update = UNSET
        else:
            update = QueryModelLinksUpdate.from_dict(_update)

        _update_immediately = d.pop("updateImmediately", UNSET)
        update_immediately: Union[Unset, QueryModelLinksUpdateImmediately]
        if isinstance(_update_immediately, Unset):
            update_immediately = UNSET
        else:
            update_immediately = QueryModelLinksUpdateImmediately.from_dict(_update_immediately)

        query_model_links = cls(
            star=star,
            unstar=unstar,
            update=update,
            update_immediately=update_immediately,
        )

        query_model_links.additional_properties = d
        return query_model_links

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
