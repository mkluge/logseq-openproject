from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.schema_model_type import SchemaModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schema_model_links import SchemaModelLinks


T = TypeVar("T", bound="SchemaModel")


@attr.s(auto_attribs=True)
class SchemaModel:
    """
    Attributes:
        field_type (SchemaModelType):
        field_links (SchemaModelLinks):
        field_dependencies (Union[Unset, List[str]]): A list of dependencies between one property's value and another
            property
    """

    field_type: SchemaModelType
    field_links: "SchemaModelLinks"
    field_dependencies: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type.value

        field_links = self.field_links.to_dict()

        field_dependencies: Union[Unset, List[str]] = UNSET
        if not isinstance(self.field_dependencies, Unset):
            field_dependencies = self.field_dependencies

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_type": field_type,
                "_links": field_links,
            }
        )
        if field_dependencies is not UNSET:
            field_dict["_dependencies"] = field_dependencies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schema_model_links import SchemaModelLinks

        d = src_dict.copy()
        field_type = SchemaModelType(d.pop("_type"))

        field_links = SchemaModelLinks.from_dict(d.pop("_links"))

        field_dependencies = cast(List[str], d.pop("_dependencies", UNSET))

        schema_model = cls(
            field_type=field_type,
            field_links=field_links,
            field_dependencies=field_dependencies,
        )

        schema_model.additional_properties = d
        return schema_model

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
