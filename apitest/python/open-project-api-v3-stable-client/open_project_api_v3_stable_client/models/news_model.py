import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_model_links import NewsModelLinks


T = TypeVar("T", bound="NewsModel")


@attr.s(auto_attribs=True)
class NewsModel:
    """
    Example:
        {'_type': 'News', 'id': 1, 'title': 'asperiores possimus nam doloribus ab', 'summary': 'Celebrer spiculum colo
            viscus claustrum atque. Id nulla culpa sumptus. Comparo crapula depopulo demonstro.', 'description': {'format':
            'markdown', 'raw': 'Videlicet deserunt aequitas cognatus. Concedo quia est quia pariatur vorago vallum. Calco
            autem atavus accusamus conscendo cornu ulterius. Tam patria ago consectetur ventito sustineo nihil caecus. Supra
            officiis eos velociter somniculosus tonsor qui. Suffragium aduro arguo angustus cogito quia tolero vulnus.
            Supplanto sortitus cresco apud vestrum qui.', 'html': '<p>Videlicet deserunt aequitas cognatus. Concedo quia est
            quia pariatur vorago vallum. Calco autem atavus accusamus conscendo cornu ulterius. Tam patria ago consectetur
            ventito sustineo nihil caecus. Supra officiis eos velociter somniculosus tonsor qui. Suffragium aduro arguo
            angustus cogito quia tolero vulnus. Supplanto sortitus cresco apud vestrum qui.</p>'}, 'createdAt':
            '2015-03-20T12:57:01Z', '_links': {'self': {'href': '/api/v3/news/1', 'title': 'asperiores possimus nam
            doloribus ab'}, 'project': {'href': '/api/v3/projects/1', 'title': 'A project'}, 'author': {'href':
            '/api/v3/users/2', 'title': 'Peggie Feeney'}}, '_embedded': {'project': {'_type': 'Project...'}, 'author':
            {'_type': 'User...'}}}

    Attributes:
        id (Union[Unset, int]): News' id
        title (Union[Unset, str]): The headline of the news
        summary (Union[Unset, str]): A short summary
        description (Union[Unset, str]): The main body of the news with all the details
        created_at (Union[Unset, datetime.datetime]): The time the news was created at
        field_links (Union[Unset, NewsModelLinks]):
    """

    id: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    field_links: Union[Unset, "NewsModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        summary = self.summary
        description = self.description
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_model_links import NewsModelLinks

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        summary = d.pop("summary", UNSET)

        description = d.pop("description", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, NewsModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = NewsModelLinks.from_dict(_field_links)

        news_model = cls(
            id=id,
            title=title,
            summary=summary,
            description=description,
            created_at=created_at,
            field_links=field_links,
        )

        news_model.additional_properties = d
        return news_model

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
