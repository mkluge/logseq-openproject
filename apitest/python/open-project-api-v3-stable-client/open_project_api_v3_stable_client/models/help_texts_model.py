from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="HelpTextsModel")


@attr.s(auto_attribs=True)
class HelpTextsModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/help_texts'}}, 'total': 2, 'count': 2, '_type': 'Collection', '_embedded':
            {'elements': [{'_type': 'HelpText', '_links': {'self': {'href': '/api/v3/help_texts/1'}}, 'id': 1, 'attribute':
            'id', 'attributeCaption': 'ID', 'scope': 'WorkPackage', 'helpText': {'format': 'markdown', 'raw': 'Help text for
            id attribute.', 'html': '<p>Help text for id attribute.</p>'}}, {'_type': 'HelpText', '_links': {'self':
            {'href': '/api/v3/help_texts/2'}}, 'id': 2, 'attribute': 'status', 'attributeCaption': 'Status', 'scope':
            'WorkPackage', 'helpText': {'format': 'markdown', 'raw': 'Help text for status attribute.', 'html': '<p>Help
            text for status attribute.</p>'}}]}}

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
        help_texts_model = cls()

        help_texts_model.additional_properties = d
        return help_texts_model

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
