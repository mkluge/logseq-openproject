from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ViewCapabilitiesModel")


@attr.s(auto_attribs=True)
class ViewCapabilitiesModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/capabilities/work_packages/create/p123-567'}, 'action': {'href':
            '/api/v3/actions/work_packages/create', 'title': 'Add work package'}, 'context': {'href':
            '/api/v3/projects/123', 'title': 'A project'}, 'principal': {'href': '/api/v3/users/567', 'title': 'Some
            user'}}, '_type': 'Capability', 'id': 'work_packages/create/p123-567'}

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
        view_capabilities_model = cls()

        view_capabilities_model.additional_properties = d
        return view_capabilities_model

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
