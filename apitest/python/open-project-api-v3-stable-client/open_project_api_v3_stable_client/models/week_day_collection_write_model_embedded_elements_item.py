from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.week_day_write_model_type import WeekDayWriteModelType

if TYPE_CHECKING:
    from ..models.week_day_self_link_model import WeekDaySelfLinkModel


T = TypeVar("T", bound="WeekDayCollectionWriteModelEmbeddedElementsItem")


@attr.s(auto_attribs=True)
class WeekDayCollectionWriteModelEmbeddedElementsItem:
    """
    Attributes:
        field_type (WeekDayWriteModelType):
        working (bool): `true` for a working day. `false` for a weekend day.
        field_links (WeekDaySelfLinkModel): Identify a particular week day by its href. Example: {'self': {'href':
            '/api/v3/days/week/3', 'title': 'Wednesday'}}.
    """

    field_type: WeekDayWriteModelType
    working: bool
    field_links: "WeekDaySelfLinkModel"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type.value

        working = self.working
        field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_type": field_type,
                "working": working,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.week_day_self_link_model import WeekDaySelfLinkModel

        d = src_dict.copy()
        field_type = WeekDayWriteModelType(d.pop("_type"))

        working = d.pop("working")

        field_links = WeekDaySelfLinkModel.from_dict(d.pop("_links"))

        week_day_collection_write_model_embedded_elements_item = cls(
            field_type=field_type,
            working=working,
            field_links=field_links,
        )

        week_day_collection_write_model_embedded_elements_item.additional_properties = d
        return week_day_collection_write_model_embedded_elements_item

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
