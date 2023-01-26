from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShowOrValidateFormJsonBody")


@attr.s(auto_attribs=True)
class ShowOrValidateFormJsonBody:
    """
    Example:
        {'_type': 'Example', 'lockVersion': 5, 'subject': 'An example title'}

    Attributes:
        field_type (Union[Unset, str]):
        lock_version (Union[Unset, float]):
        subject (Union[Unset, str]):
    """

    field_type: Union[Unset, str] = UNSET
    lock_version: Union[Unset, float] = UNSET
    subject: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type
        lock_version = self.lock_version
        subject = self.subject

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_type is not UNSET:
            field_dict["_type"] = field_type
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_type = d.pop("_type", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        subject = d.pop("subject", UNSET)

        show_or_validate_form_json_body = cls(
            field_type=field_type,
            lock_version=lock_version,
            subject=subject,
        )

        show_or_validate_form_json_body.additional_properties = d
        return show_or_validate_form_json_body

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
