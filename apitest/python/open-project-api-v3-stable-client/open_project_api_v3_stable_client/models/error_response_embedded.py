from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response_embedded_details import ErrorResponseEmbeddedDetails


T = TypeVar("T", bound="ErrorResponseEmbedded")


@attr.s(auto_attribs=True)
class ErrorResponseEmbedded:
    """
    Attributes:
        details (Union[Unset, ErrorResponseEmbeddedDetails]):
    """

    details: Union[Unset, "ErrorResponseEmbeddedDetails"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_response_embedded_details import ErrorResponseEmbeddedDetails

        d = src_dict.copy()
        _details = d.pop("details", UNSET)
        details: Union[Unset, ErrorResponseEmbeddedDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ErrorResponseEmbeddedDetails.from_dict(_details)

        error_response_embedded = cls(
            details=details,
        )

        error_response_embedded.additional_properties = d
        return error_response_embedded

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
