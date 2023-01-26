from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.membership_model_links_principal import MembershipModelLinksPrincipal
    from ..models.membership_model_links_project import MembershipModelLinksProject
    from ..models.membership_model_links_roles import MembershipModelLinksRoles
    from ..models.membership_model_links_self import MembershipModelLinksSelf


T = TypeVar("T", bound="MembershipModelLinks")


@attr.s(auto_attribs=True)
class MembershipModelLinks:
    """
    Attributes:
        self_ (MembershipModelLinksSelf):
        roles (MembershipModelLinksRoles):
        principal (MembershipModelLinksPrincipal):
        project (Union[Unset, MembershipModelLinksProject]):
    """

    self_: "MembershipModelLinksSelf"
    roles: "MembershipModelLinksRoles"
    principal: "MembershipModelLinksPrincipal"
    project: Union[Unset, "MembershipModelLinksProject"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        roles = self.roles.to_dict()

        principal = self.principal.to_dict()

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "roles": roles,
                "principal": principal,
            }
        )
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.membership_model_links_principal import MembershipModelLinksPrincipal
        from ..models.membership_model_links_project import MembershipModelLinksProject
        from ..models.membership_model_links_roles import MembershipModelLinksRoles
        from ..models.membership_model_links_self import MembershipModelLinksSelf

        d = src_dict.copy()
        self_ = MembershipModelLinksSelf.from_dict(d.pop("self"))

        roles = MembershipModelLinksRoles.from_dict(d.pop("roles"))

        principal = MembershipModelLinksPrincipal.from_dict(d.pop("principal"))

        _project = d.pop("project", UNSET)
        project: Union[Unset, MembershipModelLinksProject]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = MembershipModelLinksProject.from_dict(_project)

        membership_model_links = cls(
            self_=self_,
            roles=roles,
            principal=principal,
            project=project,
        )

        membership_model_links.additional_properties = d
        return membership_model_links

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
