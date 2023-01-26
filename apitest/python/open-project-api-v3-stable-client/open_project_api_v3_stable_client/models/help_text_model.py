from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="HelpTextModel")


@attr.s(auto_attribs=True)
class HelpTextModel:
    """
    Example:
        {'_type': 'HelpText', '_links': {'self': {'href': '/api/v3/help_texts/1'}, 'editText': {'type': 'text/html',
            'href': '/admin/attribute_help_texts/1/edit'}}, 'id': 1, 'attribute': 'id', 'attributeCaption': 'ID', 'scope':
            'WorkPackage', 'helpText': {'format': 'markdown', 'raw': 'Help text for id attribute.', 'html': '<p>Help text
            for id attribute.</p>'}}

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
        help_text_model = cls()

        help_text_model.additional_properties = d
        return help_text_model

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
