from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DocumentsModel")


@attr.s(auto_attribs=True)
class DocumentsModel:
    """
    Example:
        {'_type': 'Collection', 'total': 2, 'count': 2, 'pageSize': 30, 'offset': 1, '_embedded': {'elements':
            [{'description': {'format': 'markdown', 'raw': 'Videlicet deserunt aequitas cognatus. Concedo quia est quia
            pariatur vorago vallum. Calco autem atavus accusamus conscendo cornu ulterius. Tam patria ago consectetur
            ventito sustineo nihil caecus. Supra officiis eos velociter somniculosus tonsor qui. Suffragium aduro arguo
            angustus cogito quia tolero vulnus. Supplanto sortitus cresco apud vestrum qui.', 'html': '<p>Videlicet deserunt
            aequitas cognatus. Concedo quia est quia pariatur vorago vallum. Calco autem atavus accusamus conscendo cornu
            ulterius. Tam patria ago consectetur ventito sustineo nihil caecus. Supra officiis eos velociter somniculosus
            tonsor qui. Suffragium aduro arguo angustus cogito quia tolero vulnus. Supplanto sortitus cresco apud vestrum
            qui.</p>'}, '_type': 'Document', 'id': 1, 'title': 'Some other document', 'createdAt': '2018-12-10T20:53:39Z',
            '_links': {'attachments': {'href': '/api/v3/documents/1/attachments'}, 'addAttachment': {'href':
            '/api/v3/documents/1/attachments', 'method': 'post'}, 'self': {'href': '/api/v3/documents/1', 'title': 'Some
            document'}, 'project': {'href': '/api/v3/projects/19', 'title': 'Some project'}}}, {'description': {'format':
            'markdown', 'raw': 'Videlicet deserunt aequitas cognatus. Concedo quia est quia pariatur vorago vallum. Calco
            autem atavus accusamus conscendo cornu ulterius. Tam patria ago consectetur ventito sustineo nihil caecus. Supra
            officiis eos velociter somniculosus tonsor qui. Suffragium aduro arguo angustus cogito quia tolero vulnus.
            Supplanto sortitus cresco apud vestrum qui.', 'html': '<p>Videlicet deserunt aequitas cognatus. Concedo quia est
            quia pariatur vorago vallum. Calco autem atavus accusamus conscendo cornu ulterius. Tam patria ago consectetur
            ventito sustineo nihil caecus. Supra officiis eos velociter somniculosus tonsor qui. Suffragium aduro arguo
            angustus cogito quia tolero vulnus. Supplanto sortitus cresco apud vestrum qui.</p>'}, '_type': 'Document',
            'id': 2, 'title': 'Some other document', 'createdAt': '2018-12-10T20:55:54Z', '_links': {'attachments': {'href':
            '/api/v3/documents/2/attachments'}, 'addAttachment': {'href': '/api/v3/documents/2/attachments', 'method':
            'post'}, 'self': {'href': '/api/v3/documents/2', 'title': 'Some other document'}, 'project': {'href':
            '/api/v3/projects/29', 'title': 'Some other project'}}}]}, '_links': {'self': {'href':
            '/api/v3/documents?offset=1&pageSize=30'}, 'jumpTo': {'href':
            '/api/v3/documents?offset=%7Boffset%7D&pageSize=30', 'templated': True}, 'changeSize': {'href':
            '/api/v3/documents?offset=1&pageSize=%7Bsize%7D', 'templated': True}}}

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
        documents_model = cls()

        documents_model.additional_properties = d
        return documents_model

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
