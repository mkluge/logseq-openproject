from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customaction_model_links_execute_immediately import CustomactionModelLinksExecuteImmediately


T = TypeVar("T", bound="CustomactionModelLinks")


@attr.s(auto_attribs=True)
class CustomactionModelLinks:
    """
    Attributes:
        execute_immediately (Union[Unset, CustomactionModelLinksExecuteImmediately]):
    """

    execute_immediately: Union[Unset, "CustomactionModelLinksExecuteImmediately"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        execute_immediately: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.execute_immediately, Unset):
            execute_immediately = self.execute_immediately.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if execute_immediately is not UNSET:
            field_dict["executeImmediately"] = execute_immediately

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customaction_model_links_execute_immediately import CustomactionModelLinksExecuteImmediately

        d = src_dict.copy()
        _execute_immediately = d.pop("executeImmediately", UNSET)
        execute_immediately: Union[Unset, CustomactionModelLinksExecuteImmediately]
        if isinstance(_execute_immediately, Unset):
            execute_immediately = UNSET
        else:
            execute_immediately = CustomactionModelLinksExecuteImmediately.from_dict(_execute_immediately)

        customaction_model_links = cls(
            execute_immediately=execute_immediately,
        )

        customaction_model_links.additional_properties = d
        return customaction_model_links

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
