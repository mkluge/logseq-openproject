from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_model_links_default_assignee import CategoryModelLinksDefaultAssignee
    from ..models.category_model_links_project import CategoryModelLinksProject
    from ..models.category_model_links_self import CategoryModelLinksSelf


T = TypeVar("T", bound="CategoryModelLinks")


@attr.s(auto_attribs=True)
class CategoryModelLinks:
    """
    Attributes:
        self_ (CategoryModelLinksSelf):
        project (CategoryModelLinksProject):
        default_assignee (Union[Unset, CategoryModelLinksDefaultAssignee]):
    """

    self_: "CategoryModelLinksSelf"
    project: "CategoryModelLinksProject"
    default_assignee: Union[Unset, "CategoryModelLinksDefaultAssignee"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        project = self.project.to_dict()

        default_assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_assignee, Unset):
            default_assignee = self.default_assignee.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "project": project,
            }
        )
        if default_assignee is not UNSET:
            field_dict["defaultAssignee"] = default_assignee

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.category_model_links_default_assignee import CategoryModelLinksDefaultAssignee
        from ..models.category_model_links_project import CategoryModelLinksProject
        from ..models.category_model_links_self import CategoryModelLinksSelf

        d = src_dict.copy()
        self_ = CategoryModelLinksSelf.from_dict(d.pop("self"))

        project = CategoryModelLinksProject.from_dict(d.pop("project"))

        _default_assignee = d.pop("defaultAssignee", UNSET)
        default_assignee: Union[Unset, CategoryModelLinksDefaultAssignee]
        if isinstance(_default_assignee, Unset):
            default_assignee = UNSET
        else:
            default_assignee = CategoryModelLinksDefaultAssignee.from_dict(_default_assignee)

        category_model_links = cls(
            self_=self_,
            project=project,
            default_assignee=default_assignee,
        )

        category_model_links.additional_properties = d
        return category_model_links

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
