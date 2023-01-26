import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.storage_model_type import StorageModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_model_links import StorageModelLinks


T = TypeVar("T", bound="StorageModel")


@attr.s(auto_attribs=True)
class StorageModel:
    """
    Example:
        {'id': 1337, '_type': 'Storage', 'name': "It's no moon", 'createdAt': '2021-12-20T13:37:00.211Z', 'updatedAt':
            '2021-12-20T13:37:00.211Z', '_links': {'self': {'href': '/api/v3/storages/1337', 'title': "It's no moon"},
            'type': {'href': 'urn:openproject-org:api:v3:storages:nextcloud', 'title': 'Nextcloud'}, 'origin': {'href':
            'https://nextcloud.deathstar.rocks/'}, 'open': {'href': 'https://nextcloud.deathstar.rocks/apps/files'},
            'authorizationState': {'href': 'urn:openproject-org:api:v3:storages:authorization:FailedAuthorization', 'title':
            'Failed Authorization'}, 'authorize': {'href': 'https://nextcloud.deathstar.rocks/authorize/', 'title':
            'Authorize'}}}

    Attributes:
        id (int): Storage id
        field_type (StorageModelType):
        name (str): Storage name
        field_links (StorageModelLinks):
        created_at (Union[Unset, datetime.datetime]): Time of creation
        updated_at (Union[Unset, datetime.datetime]): Time of the most recent change to the storage
    """

    id: int
    field_type: StorageModelType
    name: str
    field_links: "StorageModelLinks"
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        field_type = self.field_type.value

        name = self.name
        field_links = self.field_links.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "_type": field_type,
                "name": name,
                "_links": field_links,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.storage_model_links import StorageModelLinks

        d = src_dict.copy()
        id = d.pop("id")

        field_type = StorageModelType(d.pop("_type"))

        name = d.pop("name")

        field_links = StorageModelLinks.from_dict(d.pop("_links"))

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

        storage_model = cls(
            id=id,
            field_type=field_type,
            name=name,
            field_links=field_links,
            created_at=created_at,
            updated_at=updated_at,
        )

        storage_model.additional_properties = d
        return storage_model

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
