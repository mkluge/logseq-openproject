from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_model_links_categories import ProjectModelLinksCategories
    from ..models.project_model_links_create_work_package import ProjectModelLinksCreateWorkPackage
    from ..models.project_model_links_create_work_package_immediately import (
        ProjectModelLinksCreateWorkPackageImmediately,
    )
    from ..models.project_model_links_delete import ProjectModelLinksDelete
    from ..models.project_model_links_memberships import ProjectModelLinksMemberships
    from ..models.project_model_links_parent import ProjectModelLinksParent
    from ..models.project_model_links_self import ProjectModelLinksSelf
    from ..models.project_model_links_status import ProjectModelLinksStatus
    from ..models.project_model_links_storages_item import ProjectModelLinksStoragesItem
    from ..models.project_model_links_types import ProjectModelLinksTypes
    from ..models.project_model_links_update import ProjectModelLinksUpdate
    from ..models.project_model_links_update_immediately import ProjectModelLinksUpdateImmediately
    from ..models.project_model_links_versions import ProjectModelLinksVersions
    from ..models.project_model_links_work_packages import ProjectModelLinksWorkPackages


T = TypeVar("T", bound="ProjectModelLinks")


@attr.s(auto_attribs=True)
class ProjectModelLinks:
    """
    Attributes:
        self_ (ProjectModelLinksSelf):
        categories (ProjectModelLinksCategories):
        types (ProjectModelLinksTypes):
        versions (ProjectModelLinksVersions):
        memberships (ProjectModelLinksMemberships):
        work_packages (ProjectModelLinksWorkPackages):
        update (Union[Unset, ProjectModelLinksUpdate]):
        update_immediately (Union[Unset, ProjectModelLinksUpdateImmediately]):
        delete (Union[Unset, ProjectModelLinksDelete]):
        create_work_package (Union[Unset, ProjectModelLinksCreateWorkPackage]):
        create_work_package_immediately (Union[Unset, ProjectModelLinksCreateWorkPackageImmediately]):
        parent (Union[Unset, ProjectModelLinksParent]):
        status (Union[Unset, ProjectModelLinksStatus]):
        storages (Union[Unset, List['ProjectModelLinksStoragesItem']]):
    """

    self_: "ProjectModelLinksSelf"
    categories: "ProjectModelLinksCategories"
    types: "ProjectModelLinksTypes"
    versions: "ProjectModelLinksVersions"
    memberships: "ProjectModelLinksMemberships"
    work_packages: "ProjectModelLinksWorkPackages"
    update: Union[Unset, "ProjectModelLinksUpdate"] = UNSET
    update_immediately: Union[Unset, "ProjectModelLinksUpdateImmediately"] = UNSET
    delete: Union[Unset, "ProjectModelLinksDelete"] = UNSET
    create_work_package: Union[Unset, "ProjectModelLinksCreateWorkPackage"] = UNSET
    create_work_package_immediately: Union[Unset, "ProjectModelLinksCreateWorkPackageImmediately"] = UNSET
    parent: Union[Unset, "ProjectModelLinksParent"] = UNSET
    status: Union[Unset, "ProjectModelLinksStatus"] = UNSET
    storages: Union[Unset, List["ProjectModelLinksStoragesItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        categories = self.categories.to_dict()

        types = self.types.to_dict()

        versions = self.versions.to_dict()

        memberships = self.memberships.to_dict()

        work_packages = self.work_packages.to_dict()

        update: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.to_dict()

        update_immediately: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_immediately, Unset):
            update_immediately = self.update_immediately.to_dict()

        delete: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delete, Unset):
            delete = self.delete.to_dict()

        create_work_package: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.create_work_package, Unset):
            create_work_package = self.create_work_package.to_dict()

        create_work_package_immediately: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.create_work_package_immediately, Unset):
            create_work_package_immediately = self.create_work_package_immediately.to_dict()

        parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        storages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.storages, Unset):
            storages = []
            for storages_item_data in self.storages:
                storages_item = storages_item_data.to_dict()

                storages.append(storages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "categories": categories,
                "types": types,
                "versions": versions,
                "memberships": memberships,
                "workPackages": work_packages,
            }
        )
        if update is not UNSET:
            field_dict["update"] = update
        if update_immediately is not UNSET:
            field_dict["updateImmediately"] = update_immediately
        if delete is not UNSET:
            field_dict["delete"] = delete
        if create_work_package is not UNSET:
            field_dict["createWorkPackage"] = create_work_package
        if create_work_package_immediately is not UNSET:
            field_dict["createWorkPackageImmediately"] = create_work_package_immediately
        if parent is not UNSET:
            field_dict["parent"] = parent
        if status is not UNSET:
            field_dict["status"] = status
        if storages is not UNSET:
            field_dict["storages"] = storages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_model_links_categories import ProjectModelLinksCategories
        from ..models.project_model_links_create_work_package import ProjectModelLinksCreateWorkPackage
        from ..models.project_model_links_create_work_package_immediately import (
            ProjectModelLinksCreateWorkPackageImmediately,
        )
        from ..models.project_model_links_delete import ProjectModelLinksDelete
        from ..models.project_model_links_memberships import ProjectModelLinksMemberships
        from ..models.project_model_links_parent import ProjectModelLinksParent
        from ..models.project_model_links_self import ProjectModelLinksSelf
        from ..models.project_model_links_status import ProjectModelLinksStatus
        from ..models.project_model_links_storages_item import ProjectModelLinksStoragesItem
        from ..models.project_model_links_types import ProjectModelLinksTypes
        from ..models.project_model_links_update import ProjectModelLinksUpdate
        from ..models.project_model_links_update_immediately import ProjectModelLinksUpdateImmediately
        from ..models.project_model_links_versions import ProjectModelLinksVersions
        from ..models.project_model_links_work_packages import ProjectModelLinksWorkPackages

        d = src_dict.copy()
        self_ = ProjectModelLinksSelf.from_dict(d.pop("self"))

        categories = ProjectModelLinksCategories.from_dict(d.pop("categories"))

        types = ProjectModelLinksTypes.from_dict(d.pop("types"))

        versions = ProjectModelLinksVersions.from_dict(d.pop("versions"))

        memberships = ProjectModelLinksMemberships.from_dict(d.pop("memberships"))

        work_packages = ProjectModelLinksWorkPackages.from_dict(d.pop("workPackages"))

        _update = d.pop("update", UNSET)
        update: Union[Unset, ProjectModelLinksUpdate]
        if isinstance(_update, Unset):
            update = UNSET
        else:
            update = ProjectModelLinksUpdate.from_dict(_update)

        _update_immediately = d.pop("updateImmediately", UNSET)
        update_immediately: Union[Unset, ProjectModelLinksUpdateImmediately]
        if isinstance(_update_immediately, Unset):
            update_immediately = UNSET
        else:
            update_immediately = ProjectModelLinksUpdateImmediately.from_dict(_update_immediately)

        _delete = d.pop("delete", UNSET)
        delete: Union[Unset, ProjectModelLinksDelete]
        if isinstance(_delete, Unset):
            delete = UNSET
        else:
            delete = ProjectModelLinksDelete.from_dict(_delete)

        _create_work_package = d.pop("createWorkPackage", UNSET)
        create_work_package: Union[Unset, ProjectModelLinksCreateWorkPackage]
        if isinstance(_create_work_package, Unset):
            create_work_package = UNSET
        else:
            create_work_package = ProjectModelLinksCreateWorkPackage.from_dict(_create_work_package)

        _create_work_package_immediately = d.pop("createWorkPackageImmediately", UNSET)
        create_work_package_immediately: Union[Unset, ProjectModelLinksCreateWorkPackageImmediately]
        if isinstance(_create_work_package_immediately, Unset):
            create_work_package_immediately = UNSET
        else:
            create_work_package_immediately = ProjectModelLinksCreateWorkPackageImmediately.from_dict(
                _create_work_package_immediately
            )

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, ProjectModelLinksParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = ProjectModelLinksParent.from_dict(_parent)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ProjectModelLinksStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProjectModelLinksStatus.from_dict(_status)

        storages = []
        _storages = d.pop("storages", UNSET)
        for storages_item_data in _storages or []:
            storages_item = ProjectModelLinksStoragesItem.from_dict(storages_item_data)

            storages.append(storages_item)

        project_model_links = cls(
            self_=self_,
            categories=categories,
            types=types,
            versions=versions,
            memberships=memberships,
            work_packages=work_packages,
            update=update,
            update_immediately=update_immediately,
            delete=delete,
            create_work_package=create_work_package,
            create_work_package_immediately=create_work_package_immediately,
            parent=parent,
            status=status,
            storages=storages,
        )

        project_model_links.additional_properties = d
        return project_model_links

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
