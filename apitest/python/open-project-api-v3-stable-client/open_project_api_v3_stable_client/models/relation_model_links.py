from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relation_model_links_delete import RelationModelLinksDelete
    from ..models.relation_model_links_from import RelationModelLinksFrom
    from ..models.relation_model_links_schema import RelationModelLinksSchema
    from ..models.relation_model_links_self import RelationModelLinksSelf
    from ..models.relation_model_links_to import RelationModelLinksTo
    from ..models.relation_model_links_update import RelationModelLinksUpdate
    from ..models.relation_model_links_update_immediately import RelationModelLinksUpdateImmediately


T = TypeVar("T", bound="RelationModelLinks")


@attr.s(auto_attribs=True)
class RelationModelLinks:
    """
    Attributes:
        self_ (RelationModelLinksSelf):
        schema (RelationModelLinksSchema):
        from_ (RelationModelLinksFrom):
        to (RelationModelLinksTo):
        update (Union[Unset, RelationModelLinksUpdate]):
        update_immediately (Union[Unset, RelationModelLinksUpdateImmediately]):
        delete (Union[Unset, RelationModelLinksDelete]):
    """

    self_: "RelationModelLinksSelf"
    schema: "RelationModelLinksSchema"
    from_: "RelationModelLinksFrom"
    to: "RelationModelLinksTo"
    update: Union[Unset, "RelationModelLinksUpdate"] = UNSET
    update_immediately: Union[Unset, "RelationModelLinksUpdateImmediately"] = UNSET
    delete: Union[Unset, "RelationModelLinksDelete"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        schema = self.schema.to_dict()

        from_ = self.from_.to_dict()

        to = self.to.to_dict()

        update: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.to_dict()

        update_immediately: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_immediately, Unset):
            update_immediately = self.update_immediately.to_dict()

        delete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delete, Unset):
            delete = self.delete.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "schema": schema,
                "from": from_,
                "to": to,
            }
        )
        if update is not UNSET:
            field_dict["update"] = update
        if update_immediately is not UNSET:
            field_dict["updateImmediately"] = update_immediately
        if delete is not UNSET:
            field_dict["delete"] = delete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.relation_model_links_delete import RelationModelLinksDelete
        from ..models.relation_model_links_from import RelationModelLinksFrom
        from ..models.relation_model_links_schema import RelationModelLinksSchema
        from ..models.relation_model_links_self import RelationModelLinksSelf
        from ..models.relation_model_links_to import RelationModelLinksTo
        from ..models.relation_model_links_update import RelationModelLinksUpdate
        from ..models.relation_model_links_update_immediately import RelationModelLinksUpdateImmediately

        d = src_dict.copy()
        self_ = RelationModelLinksSelf.from_dict(d.pop("self"))

        schema = RelationModelLinksSchema.from_dict(d.pop("schema"))

        from_ = RelationModelLinksFrom.from_dict(d.pop("from"))

        to = RelationModelLinksTo.from_dict(d.pop("to"))

        _update = d.pop("update", UNSET)
        update: Union[Unset, RelationModelLinksUpdate]
        if isinstance(_update, Unset):
            update = UNSET
        else:
            update = RelationModelLinksUpdate.from_dict(_update)

        _update_immediately = d.pop("updateImmediately", UNSET)
        update_immediately: Union[Unset, RelationModelLinksUpdateImmediately]
        if isinstance(_update_immediately, Unset):
            update_immediately = UNSET
        else:
            update_immediately = RelationModelLinksUpdateImmediately.from_dict(_update_immediately)

        _delete = d.pop("delete", UNSET)
        delete: Union[Unset, RelationModelLinksDelete]
        if isinstance(_delete, Unset):
            delete = UNSET
        else:
            delete = RelationModelLinksDelete.from_dict(_delete)

        relation_model_links = cls(
            self_=self_,
            schema=schema,
            from_=from_,
            to=to,
            update=update,
            update_immediately=update_immediately,
            delete=delete,
        )

        relation_model_links.additional_properties = d
        return relation_model_links

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
