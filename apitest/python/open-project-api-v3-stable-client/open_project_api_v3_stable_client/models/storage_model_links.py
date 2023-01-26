from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_model_links_authorization_state import StorageModelLinksAuthorizationState
    from ..models.storage_model_links_authorize import StorageModelLinksAuthorize
    from ..models.storage_model_links_open import StorageModelLinksOpen
    from ..models.storage_model_links_origin import StorageModelLinksOrigin
    from ..models.storage_model_links_self import StorageModelLinksSelf
    from ..models.storage_model_links_type import StorageModelLinksType


T = TypeVar("T", bound="StorageModelLinks")


@attr.s(auto_attribs=True)
class StorageModelLinks:
    """
    Attributes:
        self_ (StorageModelLinksSelf):
        type (StorageModelLinksType):
        origin (StorageModelLinksOrigin):
        open_ (StorageModelLinksOpen):
        authorization_state (StorageModelLinksAuthorizationState):
        authorize (Union[Unset, StorageModelLinksAuthorize]):
    """

    self_: "StorageModelLinksSelf"
    type: "StorageModelLinksType"
    origin: "StorageModelLinksOrigin"
    open_: "StorageModelLinksOpen"
    authorization_state: "StorageModelLinksAuthorizationState"
    authorize: Union[Unset, "StorageModelLinksAuthorize"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        type = self.type.to_dict()

        origin = self.origin.to_dict()

        open_ = self.open_.to_dict()

        authorization_state = self.authorization_state.to_dict()

        authorize: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.authorize, Unset):
            authorize = self.authorize.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "type": type,
                "origin": origin,
                "open": open_,
                "authorizationState": authorization_state,
            }
        )
        if authorize is not UNSET:
            field_dict["authorize"] = authorize

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.storage_model_links_authorization_state import StorageModelLinksAuthorizationState
        from ..models.storage_model_links_authorize import StorageModelLinksAuthorize
        from ..models.storage_model_links_open import StorageModelLinksOpen
        from ..models.storage_model_links_origin import StorageModelLinksOrigin
        from ..models.storage_model_links_self import StorageModelLinksSelf
        from ..models.storage_model_links_type import StorageModelLinksType

        d = src_dict.copy()
        self_ = StorageModelLinksSelf.from_dict(d.pop("self"))

        type = StorageModelLinksType.from_dict(d.pop("type"))

        origin = StorageModelLinksOrigin.from_dict(d.pop("origin"))

        open_ = StorageModelLinksOpen.from_dict(d.pop("open"))

        authorization_state = StorageModelLinksAuthorizationState.from_dict(d.pop("authorizationState"))

        _authorize = d.pop("authorize", UNSET)
        authorize: Union[Unset, StorageModelLinksAuthorize]
        if isinstance(_authorize, Unset):
            authorize = UNSET
        else:
            authorize = StorageModelLinksAuthorize.from_dict(_authorize)

        storage_model_links = cls(
            self_=self_,
            type=type,
            origin=origin,
            open_=open_,
            authorization_state=authorization_state,
            authorize=authorize,
        )

        storage_model_links.additional_properties = d
        return storage_model_links

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
