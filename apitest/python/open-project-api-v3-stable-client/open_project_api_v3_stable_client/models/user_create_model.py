from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserCreateModel")


@attr.s(auto_attribs=True)
class UserCreateModel:
    """
    Example:
        {'login': 'j.sheppard', 'password': 'idestroyedsouvereign', 'firstName': 'John', 'lastName': 'Sheppard',
            'email': 'shep@mail.com', 'admin': True, 'status': 'active', 'language': 'en'}

    Attributes:
        admin (bool):
        email (str):
        login (str):
        first_name (str):
        last_name (str):
        language (str):
        password (Union[Unset, str]): The users password.

            *Conditions:*

            Only writable on creation, not on update.
        status (Union[Unset, str]): The current activation status of the user.

            *Conditions:*

            Only writable on creation, not on update.
    """

    admin: bool
    email: str
    login: str
    first_name: str
    last_name: str
    language: str
    password: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        admin = self.admin
        email = self.email
        login = self.login
        first_name = self.first_name
        last_name = self.last_name
        language = self.language
        password = self.password
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "admin": admin,
                "email": email,
                "login": login,
                "firstName": first_name,
                "lastName": last_name,
                "language": language,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        admin = d.pop("admin")

        email = d.pop("email")

        login = d.pop("login")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        language = d.pop("language")

        password = d.pop("password", UNSET)

        status = d.pop("status", UNSET)

        user_create_model = cls(
            admin=admin,
            email=email,
            login=login,
            first_name=first_name,
            last_name=last_name,
            language=language,
            password=password,
            status=status,
        )

        user_create_model.additional_properties = d
        return user_create_model

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
