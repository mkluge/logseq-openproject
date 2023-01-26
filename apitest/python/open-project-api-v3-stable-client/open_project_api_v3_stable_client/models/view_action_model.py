from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ViewActionModel")


@attr.s(auto_attribs=True)
class ViewActionModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/actions/work_packages/create', 'title': 'Add work package'}}, '_type':
            'Action', 'id': 'work_packages/create', 'name': 'Add work package', 'description': 'Creating a work package
            within a project including the uploading of attachments. Some attributes might not be selected, e.g version
            which requires a second permission', 'modules': ['work_packages']}

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
        view_action_model = cls()

        view_action_model.additional_properties = d
        return view_action_model

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
