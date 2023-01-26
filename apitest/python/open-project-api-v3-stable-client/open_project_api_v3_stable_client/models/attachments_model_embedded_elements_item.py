import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment_model_description import AttachmentModelDescription
    from ..models.attachment_model_links import AttachmentModelLinks


T = TypeVar("T", bound="AttachmentsModelEmbeddedElementsItem")


@attr.s(auto_attribs=True)
class AttachmentsModelEmbeddedElementsItem:
    """
    Attributes:
        title (str): The name of the file
        file_name (str): The name of the uploaded file
        description (AttachmentModelDescription):
        content_type (str): The files MIME-Type as determined by the server
        digest (str): A checksum for the files content
        created_at (datetime.datetime): Time of creation
        id (Union[Unset, int]): Attachment's id
        file_size (Union[Unset, int]): The size of the uploaded file in Bytes
        field_links (Union[Unset, AttachmentModelLinks]):
    """

    title: str
    file_name: str
    description: "AttachmentModelDescription"
    content_type: str
    digest: str
    created_at: datetime.datetime
    id: Union[Unset, int] = UNSET
    file_size: Union[Unset, int] = UNSET
    field_links: Union[Unset, "AttachmentModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        file_name = self.file_name
        description = self.description.to_dict()

        content_type = self.content_type
        digest = self.digest
        created_at = self.created_at.isoformat()

        id = self.id
        file_size = self.file_size
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "fileName": file_name,
                "description": description,
                "contentType": content_type,
                "digest": digest,
                "createdAt": created_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if file_size is not UNSET:
            field_dict["fileSize"] = file_size
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attachment_model_description import AttachmentModelDescription
        from ..models.attachment_model_links import AttachmentModelLinks

        d = src_dict.copy()
        title = d.pop("title")

        file_name = d.pop("fileName")

        description = AttachmentModelDescription.from_dict(d.pop("description"))

        content_type = d.pop("contentType")

        digest = d.pop("digest")

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id", UNSET)

        file_size = d.pop("fileSize", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, AttachmentModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = AttachmentModelLinks.from_dict(_field_links)

        attachments_model_embedded_elements_item = cls(
            title=title,
            file_name=file_name,
            description=description,
            content_type=content_type,
            digest=digest,
            created_at=created_at,
            id=id,
            file_size=file_size,
            field_links=field_links,
        )

        attachments_model_embedded_elements_item.additional_properties = d
        return attachments_model_embedded_elements_item

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
