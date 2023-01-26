from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigurationModel")


@attr.s(auto_attribs=True)
class ConfigurationModel:
    """
    Attributes:
        maximum_attachment_file_size (Union[Unset, int]): The maximum allowed size of an attachment in Bytes
        host_name (Union[Unset, str]): The host name configured for the system
        per_page_options (Union[Unset, List[int]]): Page size steps to be offered in paginated list UI
        active_feature_flags (Union[Unset, List[str]]): The list of all feature flags that are active
    """

    maximum_attachment_file_size: Union[Unset, int] = UNSET
    host_name: Union[Unset, str] = UNSET
    per_page_options: Union[Unset, List[int]] = UNSET
    active_feature_flags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        maximum_attachment_file_size = self.maximum_attachment_file_size
        host_name = self.host_name
        per_page_options: Union[Unset, List[int]] = UNSET
        if not isinstance(self.per_page_options, Unset):
            per_page_options = self.per_page_options

        active_feature_flags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.active_feature_flags, Unset):
            active_feature_flags = self.active_feature_flags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if maximum_attachment_file_size is not UNSET:
            field_dict["maximumAttachmentFileSize"] = maximum_attachment_file_size
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if per_page_options is not UNSET:
            field_dict["perPageOptions"] = per_page_options
        if active_feature_flags is not UNSET:
            field_dict["activeFeatureFlags"] = active_feature_flags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        maximum_attachment_file_size = d.pop("maximumAttachmentFileSize", UNSET)

        host_name = d.pop("hostName", UNSET)

        per_page_options = cast(List[int], d.pop("perPageOptions", UNSET))

        active_feature_flags = cast(List[str], d.pop("activeFeatureFlags", UNSET))

        configuration_model = cls(
            maximum_attachment_file_size=maximum_attachment_file_size,
            host_name=host_name,
            per_page_options=per_page_options,
            active_feature_flags=active_feature_flags,
        )

        configuration_model.additional_properties = d
        return configuration_model

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
