from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.error_response_type import ErrorResponseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_response_embedded import ErrorResponseEmbedded


T = TypeVar("T", bound="ErrorResponse")


@attr.s(auto_attribs=True)
class ErrorResponse:
    """
    Attributes:
        field_type (ErrorResponseType):
        error_identifier (str):  Example: urn:openproject-org:api:v3:errors:PropertyConstraintViolation.
        message (str):  Example: Project can't be blank..
        field_embedded (Union[Unset, ErrorResponseEmbedded]):
    """

    field_type: ErrorResponseType
    error_identifier: str
    message: str
    field_embedded: Union[Unset, "ErrorResponseEmbedded"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type.value

        error_identifier = self.error_identifier
        message = self.message
        field_embedded: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_type": field_type,
                "errorIdentifier": error_identifier,
                "message": message,
            }
        )
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_response_embedded import ErrorResponseEmbedded

        d = src_dict.copy()
        field_type = ErrorResponseType(d.pop("_type"))

        error_identifier = d.pop("errorIdentifier")

        message = d.pop("message")

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, ErrorResponseEmbedded]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = ErrorResponseEmbedded.from_dict(_field_embedded)

        error_response = cls(
            field_type=field_type,
            error_identifier=error_identifier,
            message=message,
            field_embedded=field_embedded,
        )

        error_response.additional_properties = d
        return error_response

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
