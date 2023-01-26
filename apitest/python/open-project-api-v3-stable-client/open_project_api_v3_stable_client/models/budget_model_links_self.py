from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_payload import LinkPayload


T = TypeVar("T", bound="BudgetModelLinksSelf")


@attr.s(auto_attribs=True)
class BudgetModelLinksSelf:
    """
    Attributes:
        href (Optional[str]): URL to the referenced resource (might be relative)
        title (Union[Unset, str]): 	Representative label for the resource
        templated (Union[Unset, bool]): If true the href contains parts that need to be replaced by the client
        method (Union[Unset, str]): The HTTP verb to use when requesting the resource Default: 'GET'.
        payload (Union[Unset, LinkPayload]): The payload to send in the request to achieve the desired result
        identifier (Union[Unset, str]): 	An optional unique identifier to the link object
    """

    href: Optional[str]
    title: Union[Unset, str] = UNSET
    templated: Union[Unset, bool] = False
    method: Union[Unset, str] = "GET"
    payload: Union[Unset, "LinkPayload"] = UNSET
    identifier: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        href = self.href
        title = self.title
        templated = self.templated
        method = self.method
        payload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        identifier = self.identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "href": href,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if templated is not UNSET:
            field_dict["templated"] = templated
        if method is not UNSET:
            field_dict["method"] = method
        if payload is not UNSET:
            field_dict["payload"] = payload
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link_payload import LinkPayload

        d = src_dict.copy()
        href = d.pop("href")

        title = d.pop("title", UNSET)

        templated = d.pop("templated", UNSET)

        method = d.pop("method", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, LinkPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = LinkPayload.from_dict(_payload)

        identifier = d.pop("identifier", UNSET)

        budget_model_links_self = cls(
            href=href,
            title=title,
            templated=templated,
            method=method,
            payload=payload,
            identifier=identifier,
        )

        budget_model_links_self.additional_properties = d
        return budget_model_links_self

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
