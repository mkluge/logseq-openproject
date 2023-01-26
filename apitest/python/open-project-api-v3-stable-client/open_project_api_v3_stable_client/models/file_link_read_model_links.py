from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_link_read_model_links_container import FileLinkReadModelLinksContainer
    from ..models.file_link_read_model_links_creator import FileLinkReadModelLinksCreator
    from ..models.file_link_read_model_links_delete import FileLinkReadModelLinksDelete
    from ..models.file_link_read_model_links_origin_open import FileLinkReadModelLinksOriginOpen
    from ..models.file_link_read_model_links_origin_open_location import FileLinkReadModelLinksOriginOpenLocation
    from ..models.file_link_read_model_links_permission import FileLinkReadModelLinksPermission
    from ..models.file_link_read_model_links_self import FileLinkReadModelLinksSelf
    from ..models.file_link_read_model_links_static_origin_download import FileLinkReadModelLinksStaticOriginDownload
    from ..models.file_link_read_model_links_static_origin_open import FileLinkReadModelLinksStaticOriginOpen
    from ..models.file_link_read_model_links_static_origin_open_location import (
        FileLinkReadModelLinksStaticOriginOpenLocation,
    )
    from ..models.file_link_read_model_links_storage import FileLinkReadModelLinksStorage


T = TypeVar("T", bound="FileLinkReadModelLinks")


@attr.s(auto_attribs=True)
class FileLinkReadModelLinks:
    """
    Attributes:
        self_ (FileLinkReadModelLinksSelf):
        storage (FileLinkReadModelLinksStorage):
        container (FileLinkReadModelLinksContainer):
        creator (FileLinkReadModelLinksCreator):
        permission (FileLinkReadModelLinksPermission):
        origin_open (FileLinkReadModelLinksOriginOpen):
        static_origin_open (FileLinkReadModelLinksStaticOriginOpen):
        origin_open_location (FileLinkReadModelLinksOriginOpenLocation):
        static_origin_open_location (FileLinkReadModelLinksStaticOriginOpenLocation):
        static_origin_download (FileLinkReadModelLinksStaticOriginDownload):
        delete (Union[Unset, FileLinkReadModelLinksDelete]):
    """

    self_: "FileLinkReadModelLinksSelf"
    storage: "FileLinkReadModelLinksStorage"
    container: "FileLinkReadModelLinksContainer"
    creator: "FileLinkReadModelLinksCreator"
    permission: "FileLinkReadModelLinksPermission"
    origin_open: "FileLinkReadModelLinksOriginOpen"
    static_origin_open: "FileLinkReadModelLinksStaticOriginOpen"
    origin_open_location: "FileLinkReadModelLinksOriginOpenLocation"
    static_origin_open_location: "FileLinkReadModelLinksStaticOriginOpenLocation"
    static_origin_download: "FileLinkReadModelLinksStaticOriginDownload"
    delete: Union[Unset, "FileLinkReadModelLinksDelete"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        storage = self.storage.to_dict()

        container = self.container.to_dict()

        creator = self.creator.to_dict()

        permission = self.permission.to_dict()

        origin_open = self.origin_open.to_dict()

        static_origin_open = self.static_origin_open.to_dict()

        origin_open_location = self.origin_open_location.to_dict()

        static_origin_open_location = self.static_origin_open_location.to_dict()

        static_origin_download = self.static_origin_download.to_dict()

        delete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delete, Unset):
            delete = self.delete.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "storage": storage,
                "container": container,
                "creator": creator,
                "permission": permission,
                "originOpen": origin_open,
                "staticOriginOpen": static_origin_open,
                "originOpenLocation": origin_open_location,
                "staticOriginOpenLocation": static_origin_open_location,
                "staticOriginDownload": static_origin_download,
            }
        )
        if delete is not UNSET:
            field_dict["delete"] = delete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_link_read_model_links_container import FileLinkReadModelLinksContainer
        from ..models.file_link_read_model_links_creator import FileLinkReadModelLinksCreator
        from ..models.file_link_read_model_links_delete import FileLinkReadModelLinksDelete
        from ..models.file_link_read_model_links_origin_open import FileLinkReadModelLinksOriginOpen
        from ..models.file_link_read_model_links_origin_open_location import FileLinkReadModelLinksOriginOpenLocation
        from ..models.file_link_read_model_links_permission import FileLinkReadModelLinksPermission
        from ..models.file_link_read_model_links_self import FileLinkReadModelLinksSelf
        from ..models.file_link_read_model_links_static_origin_download import (
            FileLinkReadModelLinksStaticOriginDownload,
        )
        from ..models.file_link_read_model_links_static_origin_open import FileLinkReadModelLinksStaticOriginOpen
        from ..models.file_link_read_model_links_static_origin_open_location import (
            FileLinkReadModelLinksStaticOriginOpenLocation,
        )
        from ..models.file_link_read_model_links_storage import FileLinkReadModelLinksStorage

        d = src_dict.copy()
        self_ = FileLinkReadModelLinksSelf.from_dict(d.pop("self"))

        storage = FileLinkReadModelLinksStorage.from_dict(d.pop("storage"))

        container = FileLinkReadModelLinksContainer.from_dict(d.pop("container"))

        creator = FileLinkReadModelLinksCreator.from_dict(d.pop("creator"))

        permission = FileLinkReadModelLinksPermission.from_dict(d.pop("permission"))

        origin_open = FileLinkReadModelLinksOriginOpen.from_dict(d.pop("originOpen"))

        static_origin_open = FileLinkReadModelLinksStaticOriginOpen.from_dict(d.pop("staticOriginOpen"))

        origin_open_location = FileLinkReadModelLinksOriginOpenLocation.from_dict(d.pop("originOpenLocation"))

        static_origin_open_location = FileLinkReadModelLinksStaticOriginOpenLocation.from_dict(
            d.pop("staticOriginOpenLocation")
        )

        static_origin_download = FileLinkReadModelLinksStaticOriginDownload.from_dict(d.pop("staticOriginDownload"))

        _delete = d.pop("delete", UNSET)
        delete: Union[Unset, FileLinkReadModelLinksDelete]
        if isinstance(_delete, Unset):
            delete = UNSET
        else:
            delete = FileLinkReadModelLinksDelete.from_dict(_delete)

        file_link_read_model_links = cls(
            self_=self_,
            storage=storage,
            container=container,
            creator=creator,
            permission=permission,
            origin_open=origin_open,
            static_origin_open=static_origin_open,
            origin_open_location=origin_open_location,
            static_origin_open_location=static_origin_open_location,
            static_origin_download=static_origin_download,
            delete=delete,
        )

        file_link_read_model_links.additional_properties = d
        return file_link_read_model_links

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
