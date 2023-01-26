from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execute_custom_action_json_body_links import ExecuteCustomActionJsonBodyLinks


T = TypeVar("T", bound="ExecuteCustomActionJsonBody")


@attr.s(auto_attribs=True)
class ExecuteCustomActionJsonBody:
    """
    Example:
        {'_links': {'workPackage': {'href': '/api/v3/work_packages/42'}}, 'lockVersion': '3'}

    Attributes:
        field_links (Union[Unset, ExecuteCustomActionJsonBodyLinks]):
        lock_version (Union[Unset, str]):
    """

    field_links: Union[Unset, "ExecuteCustomActionJsonBodyLinks"] = UNSET
    lock_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        lock_version = self.lock_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.execute_custom_action_json_body_links import ExecuteCustomActionJsonBodyLinks

        d = src_dict.copy()
        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, ExecuteCustomActionJsonBodyLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = ExecuteCustomActionJsonBodyLinks.from_dict(_field_links)

        lock_version = d.pop("lockVersion", UNSET)

        execute_custom_action_json_body = cls(
            field_links=field_links,
            lock_version=lock_version,
        )

        execute_custom_action_json_body.additional_properties = d
        return execute_custom_action_json_body

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
