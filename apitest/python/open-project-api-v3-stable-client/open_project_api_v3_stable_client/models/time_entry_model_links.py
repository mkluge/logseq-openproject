from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_entry_model_links_activity import TimeEntryModelLinksActivity
    from ..models.time_entry_model_links_delete import TimeEntryModelLinksDelete
    from ..models.time_entry_model_links_project import TimeEntryModelLinksProject
    from ..models.time_entry_model_links_self import TimeEntryModelLinksSelf
    from ..models.time_entry_model_links_update import TimeEntryModelLinksUpdate
    from ..models.time_entry_model_links_update_immediately import TimeEntryModelLinksUpdateImmediately
    from ..models.time_entry_model_links_user import TimeEntryModelLinksUser
    from ..models.time_entry_model_links_work_package import TimeEntryModelLinksWorkPackage


T = TypeVar("T", bound="TimeEntryModelLinks")


@attr.s(auto_attribs=True)
class TimeEntryModelLinks:
    """
    Attributes:
        self_ (TimeEntryModelLinksSelf):
        project (TimeEntryModelLinksProject):
        user (TimeEntryModelLinksUser):
        activity (TimeEntryModelLinksActivity):
        update_immediately (Union[Unset, TimeEntryModelLinksUpdateImmediately]):
        update (Union[Unset, TimeEntryModelLinksUpdate]):
        delete (Union[Unset, TimeEntryModelLinksDelete]):
        work_package (Union[Unset, TimeEntryModelLinksWorkPackage]):
    """

    self_: "TimeEntryModelLinksSelf"
    project: "TimeEntryModelLinksProject"
    user: "TimeEntryModelLinksUser"
    activity: "TimeEntryModelLinksActivity"
    update_immediately: Union[Unset, "TimeEntryModelLinksUpdateImmediately"] = UNSET
    update: Union[Unset, "TimeEntryModelLinksUpdate"] = UNSET
    delete: Union[Unset, "TimeEntryModelLinksDelete"] = UNSET
    work_package: Union[Unset, "TimeEntryModelLinksWorkPackage"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        project = self.project.to_dict()

        user = self.user.to_dict()

        activity = self.activity.to_dict()

        update_immediately: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_immediately, Unset):
            update_immediately = self.update_immediately.to_dict()

        update: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.to_dict()

        delete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delete, Unset):
            delete = self.delete.to_dict()

        work_package: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.work_package, Unset):
            work_package = self.work_package.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "project": project,
                "user": user,
                "activity": activity,
            }
        )
        if update_immediately is not UNSET:
            field_dict["updateImmediately"] = update_immediately
        if update is not UNSET:
            field_dict["update"] = update
        if delete is not UNSET:
            field_dict["delete"] = delete
        if work_package is not UNSET:
            field_dict["workPackage"] = work_package

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.time_entry_model_links_activity import TimeEntryModelLinksActivity
        from ..models.time_entry_model_links_delete import TimeEntryModelLinksDelete
        from ..models.time_entry_model_links_project import TimeEntryModelLinksProject
        from ..models.time_entry_model_links_self import TimeEntryModelLinksSelf
        from ..models.time_entry_model_links_update import TimeEntryModelLinksUpdate
        from ..models.time_entry_model_links_update_immediately import TimeEntryModelLinksUpdateImmediately
        from ..models.time_entry_model_links_user import TimeEntryModelLinksUser
        from ..models.time_entry_model_links_work_package import TimeEntryModelLinksWorkPackage

        d = src_dict.copy()
        self_ = TimeEntryModelLinksSelf.from_dict(d.pop("self"))

        project = TimeEntryModelLinksProject.from_dict(d.pop("project"))

        user = TimeEntryModelLinksUser.from_dict(d.pop("user"))

        activity = TimeEntryModelLinksActivity.from_dict(d.pop("activity"))

        _update_immediately = d.pop("updateImmediately", UNSET)
        update_immediately: Union[Unset, TimeEntryModelLinksUpdateImmediately]
        if isinstance(_update_immediately, Unset):
            update_immediately = UNSET
        else:
            update_immediately = TimeEntryModelLinksUpdateImmediately.from_dict(_update_immediately)

        _update = d.pop("update", UNSET)
        update: Union[Unset, TimeEntryModelLinksUpdate]
        if isinstance(_update, Unset):
            update = UNSET
        else:
            update = TimeEntryModelLinksUpdate.from_dict(_update)

        _delete = d.pop("delete", UNSET)
        delete: Union[Unset, TimeEntryModelLinksDelete]
        if isinstance(_delete, Unset):
            delete = UNSET
        else:
            delete = TimeEntryModelLinksDelete.from_dict(_delete)

        _work_package = d.pop("workPackage", UNSET)
        work_package: Union[Unset, TimeEntryModelLinksWorkPackage]
        if isinstance(_work_package, Unset):
            work_package = UNSET
        else:
            work_package = TimeEntryModelLinksWorkPackage.from_dict(_work_package)

        time_entry_model_links = cls(
            self_=self_,
            project=project,
            user=user,
            activity=activity,
            update_immediately=update_immediately,
            update=update,
            delete=delete,
            work_package=work_package,
        )

        time_entry_model_links.additional_properties = d
        return time_entry_model_links

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
