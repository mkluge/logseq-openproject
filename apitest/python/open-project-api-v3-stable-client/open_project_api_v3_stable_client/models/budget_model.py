from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.budget_model_links import BudgetModelLinks


T = TypeVar("T", bound="BudgetModel")


@attr.s(auto_attribs=True)
class BudgetModel:
    """
    Example:
        {'_type': 'Budget', '_links': {'self': {'href': '/api/v3/budgets/1', 'title': 'Q3 2015'}}, 'id': 1, 'subject':
            'Q3 2015'}

    Attributes:
        field_links (Union[Unset, BudgetModelLinks]):
    """

    field_links: Union[Unset, "BudgetModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.budget_model_links import BudgetModelLinks

        d = src_dict.copy()
        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, BudgetModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = BudgetModelLinks.from_dict(_field_links)

        budget_model = cls(
            field_links=field_links,
        )

        budget_model.additional_properties = d
        return budget_model

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
