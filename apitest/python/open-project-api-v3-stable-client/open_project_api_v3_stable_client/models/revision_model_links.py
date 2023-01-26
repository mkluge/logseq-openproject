from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.revision_model_links_author import RevisionModelLinksAuthor
    from ..models.revision_model_links_project import RevisionModelLinksProject
    from ..models.revision_model_links_self import RevisionModelLinksSelf
    from ..models.revision_model_links_show_revision import RevisionModelLinksShowRevision


T = TypeVar("T", bound="RevisionModelLinks")


@attr.s(auto_attribs=True)
class RevisionModelLinks:
    """
    Attributes:
        self_ (RevisionModelLinksSelf):
        project (RevisionModelLinksProject):
        show_revision (RevisionModelLinksShowRevision):
        author (Union[Unset, RevisionModelLinksAuthor]):
    """

    self_: "RevisionModelLinksSelf"
    project: "RevisionModelLinksProject"
    show_revision: "RevisionModelLinksShowRevision"
    author: Union[Unset, "RevisionModelLinksAuthor"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        project = self.project.to_dict()

        show_revision = self.show_revision.to_dict()

        author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "project": project,
                "showRevision": show_revision,
            }
        )
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.revision_model_links_author import RevisionModelLinksAuthor
        from ..models.revision_model_links_project import RevisionModelLinksProject
        from ..models.revision_model_links_self import RevisionModelLinksSelf
        from ..models.revision_model_links_show_revision import RevisionModelLinksShowRevision

        d = src_dict.copy()
        self_ = RevisionModelLinksSelf.from_dict(d.pop("self"))

        project = RevisionModelLinksProject.from_dict(d.pop("project"))

        show_revision = RevisionModelLinksShowRevision.from_dict(d.pop("showRevision"))

        _author = d.pop("author", UNSET)
        author: Union[Unset, RevisionModelLinksAuthor]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = RevisionModelLinksAuthor.from_dict(_author)

        revision_model_links = cls(
            self_=self_,
            project=project,
            show_revision=show_revision,
            author=author,
        )

        revision_model_links.additional_properties = d
        return revision_model_links

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
