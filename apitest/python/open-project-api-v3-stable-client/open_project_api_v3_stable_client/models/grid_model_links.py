from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grid_model_links_page import GridModelLinksPage
    from ..models.grid_model_links_self import GridModelLinksSelf
    from ..models.grid_model_links_update import GridModelLinksUpdate
    from ..models.grid_model_links_update_immediately import GridModelLinksUpdateImmediately


T = TypeVar("T", bound="GridModelLinks")


@attr.s(auto_attribs=True)
class GridModelLinks:
    """
    Attributes:
        self_ (GridModelLinksSelf):
        page (GridModelLinksPage):
        update_immediately (Union[Unset, GridModelLinksUpdateImmediately]):
        update (Union[Unset, GridModelLinksUpdate]):
    """

    self_: "GridModelLinksSelf"
    page: "GridModelLinksPage"
    update_immediately: Union[Unset, "GridModelLinksUpdateImmediately"] = UNSET
    update: Union[Unset, "GridModelLinksUpdate"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        page = self.page.to_dict()

        update_immediately: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_immediately, Unset):
            update_immediately = self.update_immediately.to_dict()

        update: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "page": page,
            }
        )
        if update_immediately is not UNSET:
            field_dict["updateImmediately"] = update_immediately
        if update is not UNSET:
            field_dict["update"] = update

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.grid_model_links_page import GridModelLinksPage
        from ..models.grid_model_links_self import GridModelLinksSelf
        from ..models.grid_model_links_update import GridModelLinksUpdate
        from ..models.grid_model_links_update_immediately import GridModelLinksUpdateImmediately

        d = src_dict.copy()
        self_ = GridModelLinksSelf.from_dict(d.pop("self"))

        page = GridModelLinksPage.from_dict(d.pop("page"))

        _update_immediately = d.pop("updateImmediately", UNSET)
        update_immediately: Union[Unset, GridModelLinksUpdateImmediately]
        if isinstance(_update_immediately, Unset):
            update_immediately = UNSET
        else:
            update_immediately = GridModelLinksUpdateImmediately.from_dict(_update_immediately)

        _update = d.pop("update", UNSET)
        update: Union[Unset, GridModelLinksUpdate]
        if isinstance(_update, Unset):
            update = UNSET
        else:
            update = GridModelLinksUpdate.from_dict(_update)

        grid_model_links = cls(
            self_=self_,
            page=page,
            update_immediately=update_immediately,
            update=update,
        )

        grid_model_links.additional_properties = d
        return grid_model_links

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
