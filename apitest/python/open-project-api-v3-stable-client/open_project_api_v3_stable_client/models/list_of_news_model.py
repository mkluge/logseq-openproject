from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ListOfNewsModel")


@attr.s(auto_attribs=True)
class ListOfNewsModel:
    """
    Example:
        {'_type': 'Collection', 'total': 78, 'count': 2, 'pageSize': 2, 'offset': 1, '_embedded': {'elements':
            [{'_type': 'News', 'id': 1, 'title': 'asperiores possimus nam doloribus ab', 'summary': 'Celebrer spiculum colo
            viscus claustrum atque. Id nulla culpa sumptus. Comparo crapula depopulo demonstro.', 'description': {'format':
            'markdown', 'raw': 'Videlicet deserunt aequitas cognatus. Concedo quia est quia pariatur vorago vallum. Calco
            autem atavus accusamus conscendo cornu ulterius. Tam patria ago consectetur ventito sustineo nihil caecus. Supra
            officiis eos velociter somniculosus tonsor qui. Suffragium aduro arguo angustus cogito quia tolero vulnus.
            Supplanto sortitus cresco apud vestrum qui.', 'html': '<p>Videlicet deserunt aequitas cognatus. Concedo quia est
            quia pariatur vorago vallum. Calco autem atavus accusamus conscendo cornu ulterius. Tam patria ago consectetur
            ventito sustineo nihil caecus. Supra officiis eos velociter somniculosus tonsor qui. Suffragium aduro arguo
            angustus cogito quia tolero vulnus. Supplanto sortitus cresco apud vestrum qui.</p>'}, 'createdAt':
            '2015-03-20T12:57:01Z', '_links': {'self': {'href': '/api/v3/news/1', 'title': 'asperiores possimus nam
            doloribus ab'}, 'project': {'href': '/api/v3/projects/1', 'title': 'Seeded Project'}, 'author': {'href':
            '/api/v3/users/2', 'title': 'Peggie Feeney'}}}, {'_type': 'News', 'id': 2, 'title': 'terminatio tutamen. Officia
            adeptio sp', 'summary': 'Consequatur sequi surculus creo tui aequitas.', 'description': {'format': 'markdown',
            'raw': 'Amicitia alius cattus voluntarius. Virgo viduo terminatio tutamen. Officia adeptio spectaculum atavus
            nisi cum concido bis. Harum caecus auxilium sol theatrum eaque consequatur. Omnis aeger suus adipisci cicuta.
            Cur delicate alias curto cursim atqui talio fugiat.', 'html': '<p>Amicitia alius cattus voluntarius. Virgo viduo
            terminatio tutamen. Officia adeptio spectaculum atavus nisi cum concido bis. Harum caecus auxilium sol theatrum
            eaque consequatur. Omnis aeger suus adipisci cicuta. Cur delicate alias curto cursim atqui talio fugiat.</p>'},
            'createdAt': '2015-03-20T12:57:01Z', '_links': {'self': {'href': '/api/v3/news/2', 'title': 'terminatio tutamen.
            Officia adeptio sp'}, 'project': {'href': '/api/v3/projects/1', 'title': 'Seeded Project'}, 'author': {'href':
            '/api/v3/users/2', 'title': 'Peggie Feeney'}}}]}, '_links': {'self': {'href':
            '/api/v3/news?offset=1&pageSize=2'}, 'jumpTo': {'href': '/api/v3/news?offset=%7Boffset%7D&pageSize=2',
            'templated': True}, 'changeSize': {'href': '/api/v3/news?offset=1&pageSize=%7Bsize%7D', 'templated': True},
            'nextByOffset': {'href': '/api/v3/news?offset=2&pageSize=2'}}}

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
        list_of_news_model = cls()

        list_of_news_model.additional_properties = d
        return list_of_news_model

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
