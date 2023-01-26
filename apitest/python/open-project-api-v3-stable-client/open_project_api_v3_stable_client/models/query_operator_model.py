from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="QueryOperatorModel")


@attr.s(auto_attribs=True)
class QueryOperatorModel:
    """
    Example:
        {'_type': 'QueryOperator', 'id': '!', 'name': 'is not', '_links': {'self': {'href':
            '/api/v3/queries/operators/!', 'title': 'is not'}}}

    Attributes:
        id (str): Query operator id
        name (str): Query operator name
    """

    id: str
    name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        query_operator_model = cls(
            id=id,
            name=name,
        )

        query_operator_model.additional_properties = d
        return query_operator_model

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
