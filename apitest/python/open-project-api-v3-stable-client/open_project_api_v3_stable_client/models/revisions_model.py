from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RevisionsModel")


@attr.s(auto_attribs=True)
class RevisionsModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/work_packages/42/revisions'}}, 'total': 2, 'count': 2, '_type':
            'Collection', '_embedded': {'elements': [{'_type': 'Revision', '_links': {'self': {'href':
            '/api/v3/revisions/13'}, 'project': {'href': '/api/v3/projects/1', 'title': 'A Test Project'}, 'author':
            {'href': '/api/v3/users/1', 'title': 'John Sheppard - j.sheppard'}, 'showRevision': {'href':
            '/projects/identifier/repository/revision/11f4b07'}}, 'id': 13, 'identifier':
            '11f4b07dff4f4ce9548a52b7d002daca7cd63ec6', 'formattedIdentifier': '11f4b07', 'authorName': 'John Sheppard',
            'message': {'format': 'plain', 'raw': 'This revision provides new features\n\nAn elaborate description', 'html':
            '<p>This revision provides new features<br/><br/>An elaborate description</p>'}, 'createdAt':
            '2015-07-21T13:36:59Z'}, {'_type': 'Revision', '_links': {'self': {'href': '/api/v3/revisions/14'}, 'project':
            {'href': '/api/v3/projects/1', 'title': 'A Test Project'}, 'author': {'href': '/api/v3/users/2', 'title': 'Jim
            Sheppard - j.sheppard'}, 'showRevision': {'href': '/projects/identifier/repository/revision/029ed72a'}}, 'id':
            13, 'identifier': '029ed72a3b7b7c4ab332b1f6eaa6576e7c946059', 'formattedIdentifier': '029ed72a', 'authorName':
            'j1msheppard', 'message': {'format': 'plain', 'raw': 'This revision fixes some stuff\n\nMore information here',
            'html': '<p>This revision fixes some stuff<br/><br/>More information here</p>'}, 'createdAt':
            '2015-06-30T08:47:00Z'}]}}

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
        revisions_model = cls()

        revisions_model.additional_properties = d
        return revisions_model

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
