from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ListGroupsModel")


@attr.s(auto_attribs=True)
class ListGroupsModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/groups'}}, 'total': 2, 'count': 2, '_type': 'Collection', '_embedded':
            {'elements': [{'_type': 'Group', 'id': 9, 'name': 'The group', 'createdAt': '2015-09-23T11:06:36Z', 'updatedAt':
            '2015-09-23T11:06:36Z', '_links': {'self': {'href': '/api/v3/groups/9', 'title': 'The group'}, 'memberships':
            {'href': '/api/v3/memberships?filters=[{"principal":{"operator":"=","values":["9"]}}]', 'title': 'Memberships'},
            'members': [{'href': '/api/v3/users/363', 'title': 'First user'}, {'href': '/api/v3/users/60', 'title': 'Second
            user'}]}}, {'_type': 'Group', 'id': 123, 'name': 'Another group', 'createdAt': '2018-09-23T11:06:36Z',
            'updatedAt': '2019-09-23T11:06:36Z', '_links': {'self': {'href': '/api/v3/groups/123', 'title': 'Another
            group'}, 'memberships': {'href':
            '/api/v3/memberships?filters=[{"principal":{"operator":"=","values":["123"]}}]', 'title': 'Memberships'},
            'members': [{'href': '/api/v3/users/343', 'title': 'Third user'}, {'href': '/api/v3/users/60', 'title': 'Second
            user'}]}}]}}

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
        list_groups_model = cls()

        list_groups_model.additional_properties = d
        return list_groups_model

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
