from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.root_model_links_configuration import RootModelLinksConfiguration
    from ..models.root_model_links_memberships import RootModelLinksMemberships
    from ..models.root_model_links_priorities import RootModelLinksPriorities
    from ..models.root_model_links_relations import RootModelLinksRelations
    from ..models.root_model_links_self import RootModelLinksSelf
    from ..models.root_model_links_statuses import RootModelLinksStatuses
    from ..models.root_model_links_time_entries import RootModelLinksTimeEntries
    from ..models.root_model_links_types import RootModelLinksTypes
    from ..models.root_model_links_user import RootModelLinksUser
    from ..models.root_model_links_user_preferences import RootModelLinksUserPreferences
    from ..models.root_model_links_work_packages import RootModelLinksWorkPackages


T = TypeVar("T", bound="RootModelLinks")


@attr.s(auto_attribs=True)
class RootModelLinks:
    """
    Attributes:
        self_ (RootModelLinksSelf):
        configuration (RootModelLinksConfiguration):
        memberships (RootModelLinksMemberships):
        priorities (RootModelLinksPriorities):
        relations (RootModelLinksRelations):
        statuses (RootModelLinksStatuses):
        time_entries (RootModelLinksTimeEntries):
        types (RootModelLinksTypes):
        user (RootModelLinksUser):
        user_preferences (RootModelLinksUserPreferences):
        work_packages (RootModelLinksWorkPackages):
    """

    self_: "RootModelLinksSelf"
    configuration: "RootModelLinksConfiguration"
    memberships: "RootModelLinksMemberships"
    priorities: "RootModelLinksPriorities"
    relations: "RootModelLinksRelations"
    statuses: "RootModelLinksStatuses"
    time_entries: "RootModelLinksTimeEntries"
    types: "RootModelLinksTypes"
    user: "RootModelLinksUser"
    user_preferences: "RootModelLinksUserPreferences"
    work_packages: "RootModelLinksWorkPackages"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        configuration = self.configuration.to_dict()

        memberships = self.memberships.to_dict()

        priorities = self.priorities.to_dict()

        relations = self.relations.to_dict()

        statuses = self.statuses.to_dict()

        time_entries = self.time_entries.to_dict()

        types = self.types.to_dict()

        user = self.user.to_dict()

        user_preferences = self.user_preferences.to_dict()

        work_packages = self.work_packages.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "configuration": configuration,
                "memberships": memberships,
                "priorities": priorities,
                "relations": relations,
                "statuses": statuses,
                "time_entries": time_entries,
                "types": types,
                "user": user,
                "userPreferences": user_preferences,
                "workPackages": work_packages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.root_model_links_configuration import RootModelLinksConfiguration
        from ..models.root_model_links_memberships import RootModelLinksMemberships
        from ..models.root_model_links_priorities import RootModelLinksPriorities
        from ..models.root_model_links_relations import RootModelLinksRelations
        from ..models.root_model_links_self import RootModelLinksSelf
        from ..models.root_model_links_statuses import RootModelLinksStatuses
        from ..models.root_model_links_time_entries import RootModelLinksTimeEntries
        from ..models.root_model_links_types import RootModelLinksTypes
        from ..models.root_model_links_user import RootModelLinksUser
        from ..models.root_model_links_user_preferences import RootModelLinksUserPreferences
        from ..models.root_model_links_work_packages import RootModelLinksWorkPackages

        d = src_dict.copy()
        self_ = RootModelLinksSelf.from_dict(d.pop("self"))

        configuration = RootModelLinksConfiguration.from_dict(d.pop("configuration"))

        memberships = RootModelLinksMemberships.from_dict(d.pop("memberships"))

        priorities = RootModelLinksPriorities.from_dict(d.pop("priorities"))

        relations = RootModelLinksRelations.from_dict(d.pop("relations"))

        statuses = RootModelLinksStatuses.from_dict(d.pop("statuses"))

        time_entries = RootModelLinksTimeEntries.from_dict(d.pop("time_entries"))

        types = RootModelLinksTypes.from_dict(d.pop("types"))

        user = RootModelLinksUser.from_dict(d.pop("user"))

        user_preferences = RootModelLinksUserPreferences.from_dict(d.pop("userPreferences"))

        work_packages = RootModelLinksWorkPackages.from_dict(d.pop("workPackages"))

        root_model_links = cls(
            self_=self_,
            configuration=configuration,
            memberships=memberships,
            priorities=priorities,
            relations=relations,
            statuses=statuses,
            time_entries=time_entries,
            types=types,
            user=user,
            user_preferences=user_preferences,
            work_packages=work_packages,
        )

        root_model_links.additional_properties = d
        return root_model_links

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
