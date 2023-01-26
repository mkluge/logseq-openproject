import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.user_model_type import UserModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_model_links import UserModelLinks


T = TypeVar("T", bound="WatchersModelEmbeddedElementsItem")


@attr.s(auto_attribs=True)
class WatchersModelEmbeddedElementsItem:
    """
    Attributes:
        field_type (UserModelType):
        id (int): User's id
        name (str): User's full name, formatting depends on instance settings
        avatar (str): URL to user's avatar
        field_links (UserModelLinks):
        login (Union[Unset, str]): User's login name

            # Conditions

            **Permission**: Administrator, manage_user global permission
        first_name (Union[Unset, str]): User's first name

            # Conditions

            **Permission**: Administrator, manage_user global permission
        last_name (Union[Unset, str]): User's last name

            # Conditions

            **Permission**: Administrator, manage_user global permission
        email (Union[Unset, str]): User's email address

            # Conditions

            E-Mail address not hidden, **Permission**: Administrator, manage_user global permission
        admin (Union[Unset, bool]): Flag indicating whether or not the user is an admin

            # Conditions

            **Permission**: Administrator
        status (Union[Unset, str]): The current activation status of the user (see below)
        language (Union[Unset, str]): User's language | ISO 639-1 format

            # Conditions

            **Permission**: Administrator, manage_user global permission
        identity_url (Union[Unset, None, str]): User's identity_url for OmniAuth authentication

            # Conditions

            **Permission**: Administrator
        created_at (Union[Unset, datetime.datetime]): Time of creation
        updated_at (Union[Unset, datetime.datetime]): Time of the most recent change to the user
    """

    field_type: UserModelType
    id: int
    name: str
    avatar: str
    field_links: "UserModelLinks"
    login: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    admin: Union[Unset, bool] = UNSET
    status: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    identity_url: Union[Unset, None, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type.value

        id = self.id
        name = self.name
        avatar = self.avatar
        field_links = self.field_links.to_dict()

        login = self.login
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        admin = self.admin
        status = self.status
        language = self.language
        identity_url = self.identity_url
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
                "_type": field_type,
                "id": id,
                "name": name,
                "avatar": avatar,
                "_links": field_links,
            }
        )
        if login is not UNSET:
            field_dict["login"] = login
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if admin is not UNSET:
            field_dict["admin"] = admin
        if status is not UNSET:
            field_dict["status"] = status
        if language is not UNSET:
            field_dict["language"] = language
        if identity_url is not UNSET:
            field_dict["identityUrl"] = identity_url
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_model_links import UserModelLinks

        d = src_dict.copy()
        field_type = UserModelType(d.pop("_type"))

        id = d.pop("id")

        name = d.pop("name")

        avatar = d.pop("avatar")

        field_links = UserModelLinks.from_dict(d.pop("_links"))

        login = d.pop("login", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        admin = d.pop("admin", UNSET)

        status = d.pop("status", UNSET)

        language = d.pop("language", UNSET)

        identity_url = d.pop("identityUrl", UNSET)

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

        watchers_model_embedded_elements_item = cls(
            field_type=field_type,
            id=id,
            name=name,
            avatar=avatar,
            field_links=field_links,
            login=login,
            first_name=first_name,
            last_name=last_name,
            email=email,
            admin=admin,
            status=status,
            language=language,
            identity_url=identity_url,
            created_at=created_at,
            updated_at=updated_at,
        )

        watchers_model_embedded_elements_item.additional_properties = d
        return watchers_model_embedded_elements_item

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
