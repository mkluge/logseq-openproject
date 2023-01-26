from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.non_working_day_model_links_self import NonWorkingDayModelLinksSelf


T = TypeVar("T", bound="NonWorkingDayModelLinks")


@attr.s(auto_attribs=True)
class NonWorkingDayModelLinks:
    """
    Attributes:
        self_ (NonWorkingDayModelLinksSelf):
    """

    self_: "NonWorkingDayModelLinksSelf"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.non_working_day_model_links_self import NonWorkingDayModelLinksSelf

        d = src_dict.copy()
        self_ = NonWorkingDayModelLinksSelf.from_dict(d.pop("self"))

        non_working_day_model_links = cls(
            self_=self_,
        )

        non_working_day_model_links.additional_properties = d
        return non_working_day_model_links

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
