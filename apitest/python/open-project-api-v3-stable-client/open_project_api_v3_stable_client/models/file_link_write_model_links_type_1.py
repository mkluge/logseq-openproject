from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.file_link_write_model_links_type_1_storage_url import FileLinkWriteModelLinksType1StorageUrl


T = TypeVar("T", bound="FileLinkWriteModelLinksType1")


@attr.s(auto_attribs=True)
class FileLinkWriteModelLinksType1:
    """
    Attributes:
        storage_url (FileLinkWriteModelLinksType1StorageUrl):
    """

    storage_url: "FileLinkWriteModelLinksType1StorageUrl"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        storage_url = self.storage_url.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storageUrl": storage_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_link_write_model_links_type_1_storage_url import FileLinkWriteModelLinksType1StorageUrl

        d = src_dict.copy()
        storage_url = FileLinkWriteModelLinksType1StorageUrl.from_dict(d.pop("storageUrl"))

        file_link_write_model_links_type_1 = cls(
            storage_url=storage_url,
        )

        file_link_write_model_links_type_1.additional_properties = d
        return file_link_write_model_links_type_1

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
