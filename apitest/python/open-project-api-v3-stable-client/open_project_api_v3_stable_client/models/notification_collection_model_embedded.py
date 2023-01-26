from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.notification_model import NotificationModel
    from ..models.schema_model import SchemaModel


T = TypeVar("T", bound="NotificationCollectionModelEmbedded")


@attr.s(auto_attribs=True)
class NotificationCollectionModelEmbedded:
    """
    Attributes:
        elements (List['NotificationModel']):
        details_schemas (List['SchemaModel']):
    """

    elements: List["NotificationModel"]
    details_schemas: List["SchemaModel"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        elements = []
        for elements_item_data in self.elements:
            elements_item = elements_item_data.to_dict()

            elements.append(elements_item)

        details_schemas = []
        for details_schemas_item_data in self.details_schemas:
            details_schemas_item = details_schemas_item_data.to_dict()

            details_schemas.append(details_schemas_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "elements": elements,
                "detailsSchemas": details_schemas,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notification_model import NotificationModel
        from ..models.schema_model import SchemaModel

        d = src_dict.copy()
        elements = []
        _elements = d.pop("elements")
        for elements_item_data in _elements:
            elements_item = NotificationModel.from_dict(elements_item_data)

            elements.append(elements_item)

        details_schemas = []
        _details_schemas = d.pop("detailsSchemas")
        for details_schemas_item_data in _details_schemas:
            details_schemas_item = SchemaModel.from_dict(details_schemas_item_data)

            details_schemas.append(details_schemas_item)

        notification_collection_model_embedded = cls(
            elements=elements,
            details_schemas=details_schemas,
        )

        notification_collection_model_embedded.additional_properties = d
        return notification_collection_model_embedded

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
