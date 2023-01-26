from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.values_property_model_type import ValuesPropertyModelType

if TYPE_CHECKING:
    from ..models.values_property_model_links import ValuesPropertyModelLinks


T = TypeVar("T", bound="ValuesPropertyModel")


@attr.s(auto_attribs=True)
class ValuesPropertyModel:
    """
    Attributes:
        field_type (ValuesPropertyModelType):
        property_ (str): The key of the key - value pair represented by the Values::Property
        value (str): The value of the key - value pair represented by the Values::Property
        field_links (ValuesPropertyModelLinks):
    """

    field_type: ValuesPropertyModelType
    property_: str
    value: str
    field_links: "ValuesPropertyModelLinks"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type.value

        property_ = self.property_
        value = self.value
        field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_type": field_type,
                "property": property_,
                "value": value,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.values_property_model_links import ValuesPropertyModelLinks

        d = src_dict.copy()
        field_type = ValuesPropertyModelType(d.pop("_type"))

        property_ = d.pop("property")

        value = d.pop("value")

        field_links = ValuesPropertyModelLinks.from_dict(d.pop("_links"))

        values_property_model = cls(
            field_type=field_type,
            property_=property_,
            value=value,
            field_links=field_links,
        )

        values_property_model.additional_properties = d
        return values_property_model

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
