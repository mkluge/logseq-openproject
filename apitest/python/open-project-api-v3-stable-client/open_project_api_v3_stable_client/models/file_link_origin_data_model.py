import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileLinkOriginDataModel")


@attr.s(auto_attribs=True)
class FileLinkOriginDataModel:
    """
    Attributes:
        id (str): Linked file's id on the origin
        name (str): Linked file's name on the origin
        mime_type (Union[Unset, str]): MIME type of the linked file.

            To link a folder entity, the custom MIME type `application/x-op-directory` MUST be provided. Otherwise it
            defaults back to
            an unknown MIME type.
        size (Union[Unset, int]): file size on origin in bytes
        created_at (Union[Unset, datetime.datetime]): Timestamp of the creation datetime of the file on the origin
        last_modified_at (Union[Unset, datetime.datetime]): Timestamp of the datetime of the last modification of the
            file on the origin
        created_by_name (Union[Unset, str]): Display name of the author that created the file on the origin
        last_modified_by_name (Union[Unset, str]): Display name of the author that modified the file on the origin last
    """

    id: str
    name: str
    mime_type: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    last_modified_at: Union[Unset, datetime.datetime] = UNSET
    created_by_name: Union[Unset, str] = UNSET
    last_modified_by_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        mime_type = self.mime_type
        size = self.size
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        last_modified_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified_at, Unset):
            last_modified_at = self.last_modified_at.isoformat()

        created_by_name = self.created_by_name
        last_modified_by_name = self.last_modified_by_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if size is not UNSET:
            field_dict["size"] = size
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at
        if created_by_name is not UNSET:
            field_dict["createdByName"] = created_by_name
        if last_modified_by_name is not UNSET:
            field_dict["lastModifiedByName"] = last_modified_by_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        mime_type = d.pop("mimeType", UNSET)

        size = d.pop("size", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _last_modified_at = d.pop("lastModifiedAt", UNSET)
        last_modified_at: Union[Unset, datetime.datetime]
        if isinstance(_last_modified_at, Unset):
            last_modified_at = UNSET
        else:
            last_modified_at = isoparse(_last_modified_at)

        created_by_name = d.pop("createdByName", UNSET)

        last_modified_by_name = d.pop("lastModifiedByName", UNSET)

        file_link_origin_data_model = cls(
            id=id,
            name=name,
            mime_type=mime_type,
            size=size,
            created_at=created_at,
            last_modified_at=last_modified_at,
            created_by_name=created_by_name,
            last_modified_by_name=last_modified_by_name,
        )

        file_link_origin_data_model.additional_properties = d
        return file_link_origin_data_model

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
