from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.version_model_links_available_in_projects import VersionModelLinksAvailableInProjects
    from ..models.version_model_links_defining_project import VersionModelLinksDefiningProject
    from ..models.version_model_links_self import VersionModelLinksSelf
    from ..models.version_model_links_update import VersionModelLinksUpdate
    from ..models.version_model_links_update_immediately import VersionModelLinksUpdateImmediately


T = TypeVar("T", bound="VersionModelLinks")


@attr.s(auto_attribs=True)
class VersionModelLinks:
    """
    Attributes:
        self_ (VersionModelLinksSelf):
        available_in_projects (VersionModelLinksAvailableInProjects):
        update (Union[Unset, VersionModelLinksUpdate]):
        update_immediately (Union[Unset, VersionModelLinksUpdateImmediately]):
        defining_project (Union[Unset, VersionModelLinksDefiningProject]):
    """

    self_: "VersionModelLinksSelf"
    available_in_projects: "VersionModelLinksAvailableInProjects"
    update: Union[Unset, "VersionModelLinksUpdate"] = UNSET
    update_immediately: Union[Unset, "VersionModelLinksUpdateImmediately"] = UNSET
    defining_project: Union[Unset, "VersionModelLinksDefiningProject"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        available_in_projects = self.available_in_projects.to_dict()

        update: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.to_dict()

        update_immediately: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_immediately, Unset):
            update_immediately = self.update_immediately.to_dict()

        defining_project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.defining_project, Unset):
            defining_project = self.defining_project.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "availableInProjects": available_in_projects,
            }
        )
        if update is not UNSET:
            field_dict["update"] = update
        if update_immediately is not UNSET:
            field_dict["updateImmediately"] = update_immediately
        if defining_project is not UNSET:
            field_dict["definingProject"] = defining_project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.version_model_links_available_in_projects import VersionModelLinksAvailableInProjects
        from ..models.version_model_links_defining_project import VersionModelLinksDefiningProject
        from ..models.version_model_links_self import VersionModelLinksSelf
        from ..models.version_model_links_update import VersionModelLinksUpdate
        from ..models.version_model_links_update_immediately import VersionModelLinksUpdateImmediately

        d = src_dict.copy()
        self_ = VersionModelLinksSelf.from_dict(d.pop("self"))

        available_in_projects = VersionModelLinksAvailableInProjects.from_dict(d.pop("availableInProjects"))

        _update = d.pop("update", UNSET)
        update: Union[Unset, VersionModelLinksUpdate]
        if isinstance(_update, Unset):
            update = UNSET
        else:
            update = VersionModelLinksUpdate.from_dict(_update)

        _update_immediately = d.pop("updateImmediately", UNSET)
        update_immediately: Union[Unset, VersionModelLinksUpdateImmediately]
        if isinstance(_update_immediately, Unset):
            update_immediately = UNSET
        else:
            update_immediately = VersionModelLinksUpdateImmediately.from_dict(_update_immediately)

        _defining_project = d.pop("definingProject", UNSET)
        defining_project: Union[Unset, VersionModelLinksDefiningProject]
        if isinstance(_defining_project, Unset):
            defining_project = UNSET
        else:
            defining_project = VersionModelLinksDefiningProject.from_dict(_defining_project)

        version_model_links = cls(
            self_=self_,
            available_in_projects=available_in_projects,
            update=update,
            update_immediately=update_immediately,
            defining_project=defining_project,
        )

        version_model_links.additional_properties = d
        return version_model_links

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
