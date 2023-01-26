from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ExampleSchemaModel")


@attr.s(auto_attribs=True)
class ExampleSchemaModel:
    """
    Example:
        {'_type': 'Schema', '_dependencies': [], '_links': {'self': {'href': '/api/v3/example/schema'}}, 'lockVersion':
            {'name': 'Resource Version', 'type': 'Integer', 'writable': False}, 'subject': {'name': 'Subject', 'type':
            'String', 'minLength': 1, 'maxLength': 255}, 'status': {'_links': {'allowedValues': [{'href':
            '/api/v3/statuses/1', 'title': 'New'}, {'href': '/api/v3/statuses/2', 'title': 'Closed'}]}, 'name': 'Status',
            'type': 'Status', 'location': '_links', '_embedded': {'allowedValues': [{'_links': {'self': {'href':
            '/api/v3/statuses/1'}}, '_type': 'Status', 'id': 1, 'name': 'New', 'position': 1, 'isDefault': True, 'isClosed':
            False, 'defaultDoneRatio': 0, 'createdAt': '2014-05-21T08:51:20Z', 'updatedAt': '2014-05-21T09:12:00Z'},
            {'_links': {'self': {'href': '/api/v3/statuses/2'}}, '_type': 'Status', 'id': 2, 'name': 'Closed', 'position':
            2, 'isDefault': False, 'isClosed': True, 'defaultDoneRatio': 100, 'createdAt': '2014-05-21T08:51:20Z',
            'updatedAt': '2014-05-21T09:12:00Z'}]}}}

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        example_schema_model = cls()

        example_schema_model.additional_properties = d
        return example_schema_model

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
