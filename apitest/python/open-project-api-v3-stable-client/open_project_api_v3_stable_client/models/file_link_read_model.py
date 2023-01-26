import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.file_link_read_model_type import FileLinkReadModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_link_origin_data_model import FileLinkOriginDataModel
    from ..models.file_link_read_model_embedded import FileLinkReadModelEmbedded
    from ..models.file_link_read_model_links import FileLinkReadModelLinks


T = TypeVar("T", bound="FileLinkReadModel")


@attr.s(auto_attribs=True)
class FileLinkReadModel:
    """
    Example:
        {'id': 1337, '_type': 'FileLink', 'createdAt': '2021-12-20T13:37:00.211Z', 'updatedAt':
            '2021-12-20T13:37:00.211Z', 'originData': {'id': 5503, 'name': 'logo.png', 'mimeType': 'image/png', 'size':
            16042, 'createdAt': '2021-12-19T09:42:10.170Z', 'lastModifiedAt': '2021-12-20T14:00:13.987Z', 'createdByName':
            'Luke Skywalker', 'lastModifiedByName': 'Anakin Skywalker'}, '_embedded': {'storage': {'id': 1337, '_type':
            'Storage', 'name': "It's no moon", 'createdAt': '2021-12-20T13:37:00.211Z', 'updatedAt':
            '2021-12-20T13:37:00.211Z', '_links': {'self': {'href': '/api/v3/storages/1337', 'title': "It's no moon"},
            'type': {'href': 'urn:openproject-org:api:v3:storages:nextcloud', 'title': 'Nextcloud'}, 'origin': {'href':
            'https://nextcloud.deathstar.rocks/'}}}, 'container': {'_hint': 'Work package resource shortened for brevity',
            '_type': 'WorkPackage', '_links': {'self': {'href': '/api/v3/work_packages/1528', 'title': 'Develop API'},
            'schema': {'href': '/api/v3/work_packages/schemas/11-2'}}, 'id': 1528, 'subject': 'Develop API', 'description':
            {'format': 'markdown', 'raw': 'Develop super cool OpenProject API.', 'html': '<p>Develop super cool OpenProject
            API.</p>'}, 'scheduleManually': False, 'readonly': False, 'startDate': None, 'dueDate': None, 'createdAt':
            '2014-08-29T12:40:53Z', 'updatedAt': '2014-08-29T12:44:41Z'}}, '_links': {'self': {'href':
            '/api/v3/work_package/17/file_links/1337'}, 'storage': {'href': '/api/v3/storage/42', 'title': "It's no moon"},
            'container': {'href': '/api/v3/work_package/17', 'title': 'Develop API'}, 'creator': {'href':
            '/api/v3/users/33', 'title': 'Obi-Wan Kenobi'}, 'delete': {'href': '/api/v3/work_package/17/file_links/1337'},
            'permission': {'href': 'urn:openproject-org:api:v3:file-links:permission:View', 'title': 'View'}, 'originOpen':
            {'href': 'https://nextcloud.deathstar.rocks/index.php/f/5503?openfile=1'}, 'staticOriginOpen': {'href':
            '/api/v3/file_links/1337/open'}, 'originOpenLocation': {'href':
            'https://nextcloud.deathstar.rocks/index.php/f/5503?openfile=0'}, 'staticOriginOpenLocation': {'href':
            '/api/v3/file_links/1337/open?location=true'}, 'staticOriginDownload': {'href':
            '/api/v3/file_links/1337/download'}}}

    Attributes:
        id (int): File link id
        field_type (FileLinkReadModelType):
        origin_data (FileLinkOriginDataModel):
        field_links (FileLinkReadModelLinks):
        created_at (Union[Unset, datetime.datetime]): Time of creation
        updated_at (Union[Unset, datetime.datetime]): Time of the most recent change to the file link
        field_embedded (Union[Unset, FileLinkReadModelEmbedded]):
    """

    id: int
    field_type: FileLinkReadModelType
    origin_data: "FileLinkOriginDataModel"
    field_links: "FileLinkReadModelLinks"
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    field_embedded: Union[Unset, "FileLinkReadModelEmbedded"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        field_type = self.field_type.value

        origin_data = self.origin_data.to_dict()

        field_links = self.field_links.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_embedded: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_embedded, Unset):
            field_embedded = self.field_embedded.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "_type": field_type,
                "originData": origin_data,
                "_links": field_links,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if field_embedded is not UNSET:
            field_dict["_embedded"] = field_embedded

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_link_origin_data_model import FileLinkOriginDataModel
        from ..models.file_link_read_model_embedded import FileLinkReadModelEmbedded
        from ..models.file_link_read_model_links import FileLinkReadModelLinks

        d = src_dict.copy()
        id = d.pop("id")

        field_type = FileLinkReadModelType(d.pop("_type"))

        origin_data = FileLinkOriginDataModel.from_dict(d.pop("originData"))

        field_links = FileLinkReadModelLinks.from_dict(d.pop("_links"))

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _field_embedded = d.pop("_embedded", UNSET)
        field_embedded: Union[Unset, FileLinkReadModelEmbedded]
        if isinstance(_field_embedded, Unset):
            field_embedded = UNSET
        else:
            field_embedded = FileLinkReadModelEmbedded.from_dict(_field_embedded)

        file_link_read_model = cls(
            id=id,
            field_type=field_type,
            origin_data=origin_data,
            field_links=field_links,
            created_at=created_at,
            updated_at=updated_at,
            field_embedded=field_embedded,
        )

        file_link_read_model.additional_properties = d
        return file_link_read_model

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
