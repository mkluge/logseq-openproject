from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.work_package_model import WorkPackageModel


T = TypeVar("T", bound="WorkPackagesModelEmbedded")


@attr.s(auto_attribs=True)
class WorkPackagesModelEmbedded:
    """
    Attributes:
        elements (List['WorkPackageModel']):
    """

    elements: List["WorkPackageModel"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        elements = []
        for elements_item_data in self.elements:
            elements_item = elements_item_data.to_dict()

            elements.append(elements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "elements": elements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.work_package_model import WorkPackageModel

        d = src_dict.copy()
        elements = []
        _elements = d.pop("elements")
        for elements_item_data in _elements:
            elements_item = WorkPackageModel.from_dict(elements_item_data)

            elements.append(elements_item)

        work_packages_model_embedded = cls(
            elements=elements,
        )

        work_packages_model_embedded.additional_properties = d
        return work_packages_model_embedded

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
