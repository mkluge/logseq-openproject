from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wiki_page_model_links import WikiPageModelLinks


T = TypeVar("T", bound="WikiPageModel")


@attr.s(auto_attribs=True)
class WikiPageModel:
    """
    Example:
        {'_type': 'WikiPage', 'id': 72, 'title': 'A wiki page with a name', '_embedded': {'project': {'_type':
            'Project...', 'id': 12}}, '_links': {'self': {'href': '/api/v3/wiki_pages/72'}, 'attachments': {'href':
            '/api/v3/wiki_pages/72/attachments'}, 'addAttachment': {'href': '/api/v3/wiki_pages/72/attachments', 'method':
            'post'}, 'project': {'href': '/api/v3/projects/12', 'title': 'some project'}}}

    Attributes:
        title (str): The wiki page's title
        id (Union[Unset, int]): Identifier of this wiki page
        field_links (Union[Unset, WikiPageModelLinks]):
    """

    title: str
    id: Union[Unset, int] = UNSET
    field_links: Union[Unset, "WikiPageModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        id = self.id
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wiki_page_model_links import WikiPageModelLinks

        d = src_dict.copy()
        title = d.pop("title")

        id = d.pop("id", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, WikiPageModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = WikiPageModelLinks.from_dict(_field_links)

        wiki_page_model = cls(
            title=title,
            id=id,
            field_links=field_links,
        )

        wiki_page_model.additional_properties = d
        return wiki_page_model

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
