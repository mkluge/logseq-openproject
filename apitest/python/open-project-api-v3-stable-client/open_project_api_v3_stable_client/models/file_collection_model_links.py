from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.file_collection_model_links_self import FileCollectionModelLinksSelf


T = TypeVar("T", bound="FileCollectionModelLinks")


@attr.s(auto_attribs=True)
class FileCollectionModelLinks:
    """
    Attributes:
        self_ (FileCollectionModelLinksSelf):
    """

    self_: "FileCollectionModelLinksSelf"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_collection_model_links_self import FileCollectionModelLinksSelf

        d = src_dict.copy()
        self_ = FileCollectionModelLinksSelf.from_dict(d.pop("self"))

        file_collection_model_links = cls(
            self_=self_,
        )

        file_collection_model_links.additional_properties = d
        return file_collection_model_links

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
