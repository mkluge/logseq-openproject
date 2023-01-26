from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.time_entry_activity_model_links_projects import TimeEntryActivityModelLinksProjects
    from ..models.time_entry_activity_model_links_self import TimeEntryActivityModelLinksSelf


T = TypeVar("T", bound="TimeEntryActivityModelLinks")


@attr.s(auto_attribs=True)
class TimeEntryActivityModelLinks:
    """
    Attributes:
        self_ (TimeEntryActivityModelLinksSelf):
        projects (TimeEntryActivityModelLinksProjects):
    """

    self_: "TimeEntryActivityModelLinksSelf"
    projects: "TimeEntryActivityModelLinksProjects"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        projects = self.projects.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "projects": projects,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.time_entry_activity_model_links_projects import TimeEntryActivityModelLinksProjects
        from ..models.time_entry_activity_model_links_self import TimeEntryActivityModelLinksSelf

        d = src_dict.copy()
        self_ = TimeEntryActivityModelLinksSelf.from_dict(d.pop("self"))

        projects = TimeEntryActivityModelLinksProjects.from_dict(d.pop("projects"))

        time_entry_activity_model_links = cls(
            self_=self_,
            projects=projects,
        )

        time_entry_activity_model_links.additional_properties = d
        return time_entry_activity_model_links

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
