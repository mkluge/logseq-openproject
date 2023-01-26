from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.news_model_links_author import NewsModelLinksAuthor
    from ..models.news_model_links_project import NewsModelLinksProject
    from ..models.news_model_links_self import NewsModelLinksSelf


T = TypeVar("T", bound="NewsModelLinks")


@attr.s(auto_attribs=True)
class NewsModelLinks:
    """
    Attributes:
        self_ (NewsModelLinksSelf):
        project (NewsModelLinksProject):
        author (NewsModelLinksAuthor):
    """

    self_: "NewsModelLinksSelf"
    project: "NewsModelLinksProject"
    author: "NewsModelLinksAuthor"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        project = self.project.to_dict()

        author = self.author.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "project": project,
                "author": author,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.news_model_links_author import NewsModelLinksAuthor
        from ..models.news_model_links_project import NewsModelLinksProject
        from ..models.news_model_links_self import NewsModelLinksSelf

        d = src_dict.copy()
        self_ = NewsModelLinksSelf.from_dict(d.pop("self"))

        project = NewsModelLinksProject.from_dict(d.pop("project"))

        author = NewsModelLinksAuthor.from_dict(d.pop("author"))

        news_model_links = cls(
            self_=self_,
            project=project,
            author=author,
        )

        news_model_links.additional_properties = d
        return news_model_links

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
