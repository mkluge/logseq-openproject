from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execute_custom_action_json_body_links_work_package import ExecuteCustomActionJsonBodyLinksWorkPackage


T = TypeVar("T", bound="ExecuteCustomActionJsonBodyLinks")


@attr.s(auto_attribs=True)
class ExecuteCustomActionJsonBodyLinks:
    """
    Attributes:
        work_package (Union[Unset, ExecuteCustomActionJsonBodyLinksWorkPackage]):
    """

    work_package: Union[Unset, "ExecuteCustomActionJsonBodyLinksWorkPackage"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        work_package: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.work_package, Unset):
            work_package = self.work_package.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if work_package is not UNSET:
            field_dict["workPackage"] = work_package

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.execute_custom_action_json_body_links_work_package import (
            ExecuteCustomActionJsonBodyLinksWorkPackage,
        )

        d = src_dict.copy()
        _work_package = d.pop("workPackage", UNSET)
        work_package: Union[Unset, ExecuteCustomActionJsonBodyLinksWorkPackage]
        if isinstance(_work_package, Unset):
            work_package = UNSET
        else:
            work_package = ExecuteCustomActionJsonBodyLinksWorkPackage.from_dict(_work_package)

        execute_custom_action_json_body_links = cls(
            work_package=work_package,
        )

        execute_custom_action_json_body_links.additional_properties = d
        return execute_custom_action_json_body_links

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
