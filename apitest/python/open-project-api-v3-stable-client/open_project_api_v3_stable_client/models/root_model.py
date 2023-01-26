from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.root_model_type import RootModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_model_links import RootModelLinks


T = TypeVar("T", bound="RootModel")


@attr.s(auto_attribs=True)
class RootModel:
    """
    Example:
        {'_type': 'Root', 'instanceName': 'OpenProject', 'coreVersion': '12.1.0', '_links': {'self': {'href':
            '/api/v3'}, 'configuration': {'href': '/api/v3/configuration'}, 'memberships': {'href': '/api/v3/memberships'},
            'priorities': {'href': '/api/v3/priorities'}, 'relations': {'href': '/api/v3/relations'}, 'statuses': {'href':
            '/api/v3/statuses'}, 'time_entries': {'href': '/api/v3/time_entries'}, 'types': {'href': '/api/v3/types'},
            'user': {'href': '/api/v3/users/3', 'title': 'Anakin Skywalker'}, 'userPreferences': {'href':
            '/api/v3/users/3/preferences'}, 'workPackages': {'href': '/api/v3/work_packages'}}}

    Attributes:
        field_type (RootModelType):
        instance_name (str): The name of the OpenProject instance
        field_links (RootModelLinks):
        core_version (Union[Unset, str]): The OpenProject core version number for the instance

            # Conditions

            **Permission** requires admin privileges
    """

    field_type: RootModelType
    instance_name: str
    field_links: "RootModelLinks"
    core_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type = self.field_type.value

        instance_name = self.instance_name
        field_links = self.field_links.to_dict()

        core_version = self.core_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_type": field_type,
                "instanceName": instance_name,
                "_links": field_links,
            }
        )
        if core_version is not UNSET:
            field_dict["coreVersion"] = core_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_model_links import RootModelLinks

        d = src_dict.copy()
        field_type = RootModelType(d.pop("_type"))

        instance_name = d.pop("instanceName")

        field_links = RootModelLinks.from_dict(d.pop("_links"))

        core_version = d.pop("coreVersion", UNSET)

        root_model = cls(
            field_type=field_type,
            instance_name=instance_name,
            field_links=field_links,
            core_version=core_version,
        )

        root_model.additional_properties = d
        return root_model

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
