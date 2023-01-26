from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.file_link_write_model_links_type_0_storage import FileLinkWriteModelLinksType0Storage


T = TypeVar("T", bound="FileLinkWriteModelLinksType0")


@attr.s(auto_attribs=True)
class FileLinkWriteModelLinksType0:
    """
    Attributes:
        storage (FileLinkWriteModelLinksType0Storage):
    """

    storage: "FileLinkWriteModelLinksType0Storage"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        storage = self.storage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storage": storage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_link_write_model_links_type_0_storage import FileLinkWriteModelLinksType0Storage

        d = src_dict.copy()
        storage = FileLinkWriteModelLinksType0Storage.from_dict(d.pop("storage"))

        file_link_write_model_links_type_0 = cls(
            storage=storage,
        )

        file_link_write_model_links_type_0.additional_properties = d
        return file_link_write_model_links_type_0

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
