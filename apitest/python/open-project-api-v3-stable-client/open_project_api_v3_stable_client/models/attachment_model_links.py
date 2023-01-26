from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment_model_links_author import AttachmentModelLinksAuthor
    from ..models.attachment_model_links_container import AttachmentModelLinksContainer
    from ..models.attachment_model_links_delete import AttachmentModelLinksDelete
    from ..models.attachment_model_links_download_location import AttachmentModelLinksDownloadLocation
    from ..models.attachment_model_links_self import AttachmentModelLinksSelf


T = TypeVar("T", bound="AttachmentModelLinks")


@attr.s(auto_attribs=True)
class AttachmentModelLinks:
    """
    Attributes:
        self_ (AttachmentModelLinksSelf):
        container (AttachmentModelLinksContainer):
        author (AttachmentModelLinksAuthor):
        download_location (AttachmentModelLinksDownloadLocation):
        delete (Union[Unset, AttachmentModelLinksDelete]):
    """

    self_: "AttachmentModelLinksSelf"
    container: "AttachmentModelLinksContainer"
    author: "AttachmentModelLinksAuthor"
    download_location: "AttachmentModelLinksDownloadLocation"
    delete: Union[Unset, "AttachmentModelLinksDelete"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        container = self.container.to_dict()

        author = self.author.to_dict()

        download_location = self.download_location.to_dict()

        delete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delete, Unset):
            delete = self.delete.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "container": container,
                "author": author,
                "downloadLocation": download_location,
            }
        )
        if delete is not UNSET:
            field_dict["delete"] = delete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attachment_model_links_author import AttachmentModelLinksAuthor
        from ..models.attachment_model_links_container import AttachmentModelLinksContainer
        from ..models.attachment_model_links_delete import AttachmentModelLinksDelete
        from ..models.attachment_model_links_download_location import AttachmentModelLinksDownloadLocation
        from ..models.attachment_model_links_self import AttachmentModelLinksSelf

        d = src_dict.copy()
        self_ = AttachmentModelLinksSelf.from_dict(d.pop("self"))

        container = AttachmentModelLinksContainer.from_dict(d.pop("container"))

        author = AttachmentModelLinksAuthor.from_dict(d.pop("author"))

        download_location = AttachmentModelLinksDownloadLocation.from_dict(d.pop("downloadLocation"))

        _delete = d.pop("delete", UNSET)
        delete: Union[Unset, AttachmentModelLinksDelete]
        if isinstance(_delete, Unset):
            delete = UNSET
        else:
            delete = AttachmentModelLinksDelete.from_dict(_delete)

        attachment_model_links = cls(
            self_=self_,
            container=container,
            author=author,
            download_location=download_location,
            delete=delete,
        )

        attachment_model_links.additional_properties = d
        return attachment_model_links

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
