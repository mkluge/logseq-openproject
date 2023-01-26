import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.version_model_description import VersionModelDescription
    from ..models.version_model_links import VersionModelLinks


T = TypeVar("T", bound="VersionModel")


@attr.s(auto_attribs=True)
class VersionModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/versions/11'}, 'update': {'href': '/api/v3/versions/11/form', 'method':
            'POST'}, 'updateImmediately': {'href': '/api/v3/versions/11', 'method': 'PATCH'}, 'definingProject': {'href':
            '/api/v3/projects/11'}, 'availableInProjects': {'href': '/api/v3/versions/11/projects'}, 'customField4':
            {'href': '/api/v3/custom_options/5', 'title': 'Custom field option'}}, '_type': 'Version', 'id': 11, 'name':
            'v3.0 Alpha', 'description': {'format': 'plain', 'raw': 'This version has a description', 'html': 'This version
            has a description'}, 'startDate': '2014-11-20', 'endDate': None, 'status': 'open', 'sharing': 'system',
            'customField14': '1234567890'}

    Attributes:
        name (str): Version name
        status (str): The current status of the version
        sharing (str): The current status of the version
        created_at (datetime.datetime): Time of creation
        updated_at (datetime.datetime): Time of the most recent change to the version
        id (Union[Unset, int]): Version id
        description (Union[Unset, VersionModelDescription]):
        start_date (Union[Unset, datetime.date]):
        end_date (Union[Unset, datetime.date]):
        field_links (Union[Unset, VersionModelLinks]):
    """

    name: str
    status: str
    sharing: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    id: Union[Unset, int] = UNSET
    description: Union[Unset, "VersionModelDescription"] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    field_links: Union[Unset, "VersionModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        status = self.status
        sharing = self.sharing
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        id = self.id
        description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "sharing": sharing,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.version_model_description import VersionModelDescription
        from ..models.version_model_links import VersionModelLinks

        d = src_dict.copy()
        name = d.pop("name")

        status = d.pop("status")

        sharing = d.pop("sharing")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        id = d.pop("id", UNSET)

        _description = d.pop("description", UNSET)
        description: Union[Unset, VersionModelDescription]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = VersionModelDescription.from_dict(_description)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, VersionModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = VersionModelLinks.from_dict(_field_links)

        version_model = cls(
            name=name,
            status=status,
            sharing=sharing,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            description=description,
            start_date=start_date,
            end_date=end_date,
            field_links=field_links,
        )

        version_model.additional_properties = d
        return version_model

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
