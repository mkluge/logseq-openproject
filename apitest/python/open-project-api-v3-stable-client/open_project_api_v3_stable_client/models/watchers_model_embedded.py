from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.watchers_model_embedded_elements_item import WatchersModelEmbeddedElementsItem


T = TypeVar("T", bound="WatchersModelEmbedded")


@attr.s(auto_attribs=True)
class WatchersModelEmbedded:
    """
    Attributes:
        elements (Union[Unset, List['WatchersModelEmbeddedElementsItem']]):
    """

    elements: Union[Unset, List["WatchersModelEmbeddedElementsItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        elements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item = elements_item_data.to_dict()

                elements.append(elements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if elements is not UNSET:
            field_dict["elements"] = elements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.watchers_model_embedded_elements_item import WatchersModelEmbeddedElementsItem

        d = src_dict.copy()
        elements = []
        _elements = d.pop("elements", UNSET)
        for elements_item_data in _elements or []:
            elements_item = WatchersModelEmbeddedElementsItem.from_dict(elements_item_data)

            elements.append(elements_item)

        watchers_model_embedded = cls(
            elements=elements,
        )

        watchers_model_embedded.additional_properties = d
        return watchers_model_embedded

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
