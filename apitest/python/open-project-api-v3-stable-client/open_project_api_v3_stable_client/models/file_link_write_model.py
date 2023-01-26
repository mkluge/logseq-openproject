from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

if TYPE_CHECKING:
    from ..models.file_link_origin_data_model import FileLinkOriginDataModel
    from ..models.file_link_write_model_links_type_0 import FileLinkWriteModelLinksType0
    from ..models.file_link_write_model_links_type_1 import FileLinkWriteModelLinksType1


T = TypeVar("T", bound="FileLinkWriteModel")


@attr.s(auto_attribs=True)
class FileLinkWriteModel:
    """
    Example:
        {'originData': {'id': 5503, 'name': 'logo.png', 'mimeType': 'image/png', 'size': 16042, 'createdAt':
            '2021-12-19T09:42:10.170Z', 'lastModifiedAt': '2021-12-20T14:00:13.987Z', 'createdByName': 'Luke Skywalker',
            'lastModifiedByName': 'Anakin Skywalker'}, '_links': {'storageUrl': {'href': 'https://nextcloud.my-
            deathstar.org'}}}

    Attributes:
        origin_data (FileLinkOriginDataModel):
        field_links (Union['FileLinkWriteModelLinksType0', 'FileLinkWriteModelLinksType1']):
    """

    origin_data: "FileLinkOriginDataModel"
    field_links: Union["FileLinkWriteModelLinksType0", "FileLinkWriteModelLinksType1"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.file_link_write_model_links_type_0 import FileLinkWriteModelLinksType0

        origin_data = self.origin_data.to_dict()

        field_links: Dict[str, Any]

        if isinstance(self.field_links, FileLinkWriteModelLinksType0):
            field_links = self.field_links.to_dict()

        else:
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "originData": origin_data,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_link_origin_data_model import FileLinkOriginDataModel
        from ..models.file_link_write_model_links_type_0 import FileLinkWriteModelLinksType0
        from ..models.file_link_write_model_links_type_1 import FileLinkWriteModelLinksType1

        d = src_dict.copy()
        origin_data = FileLinkOriginDataModel.from_dict(d.pop("originData"))

        def _parse_field_links(data: object) -> Union["FileLinkWriteModelLinksType0", "FileLinkWriteModelLinksType1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_links_type_0 = FileLinkWriteModelLinksType0.from_dict(data)

                return field_links_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            field_links_type_1 = FileLinkWriteModelLinksType1.from_dict(data)

            return field_links_type_1

        field_links = _parse_field_links(d.pop("_links"))

        file_link_write_model = cls(
            origin_data=origin_data,
            field_links=field_links,
        )

        file_link_write_model.additional_properties = d
        return file_link_write_model

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
