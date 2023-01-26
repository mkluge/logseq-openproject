from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

from ..models.week_day_collection_write_model_type import WeekDayCollectionWriteModelType

if TYPE_CHECKING:
    from ..models.week_day_collection_write_model_embedded import WeekDayCollectionWriteModelEmbedded


T = TypeVar("T", bound="WeekDayCollectionWriteModel")


@attr.s(auto_attribs=True)
class WeekDayCollectionWriteModel:
    """
    Example:
        {'_type': 'Collection', '_embedded': {'elements': [{'_type': 'WeekDay', 'working': True, '_links': {'self':
            {'href': '/api/v3/days/week/1'}}}, {'_type': 'WeekDay', 'working': True, '_links': {'self': {'href':
            '/api/v3/days/week/2'}}}, {'_type': 'WeekDay', 'working': True, '_links': {'self': {'href':
            '/api/v3/days/week/4'}}}, {'_type': 'WeekDay', 'working': False, '_links': {'self': {'href':
            '/api/v3/days/week/6'}}}, {'_type': 'WeekDay', 'working': False, '_links': {'self': {'href':
            '/api/v3/days/week/7'}}}]}}

    Attributes:
        field_type (WeekDayCollectionWriteModelType):
        field_embedded (WeekDayCollectionWriteModelEmbedded):
    """

    field_type: WeekDayCollectionWriteModelType
    field_embedded: "WeekDayCollectionWriteModelEmbedded"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type.value

        field_embedded = self.field_embedded.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_type": field_type,
                "_embedded": field_embedded,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.week_day_collection_write_model_embedded import WeekDayCollectionWriteModelEmbedded

        d = src_dict.copy()
        field_type = WeekDayCollectionWriteModelType(d.pop("_type"))

        field_embedded = WeekDayCollectionWriteModelEmbedded.from_dict(d.pop("_embedded"))

        week_day_collection_write_model = cls(
            field_type=field_type,
            field_embedded=field_embedded,
        )

        week_day_collection_write_model.additional_properties = d
        return week_day_collection_write_model

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
