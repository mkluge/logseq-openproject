from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.work_package_model_links_add_attachment import WorkPackageModelLinksAddAttachment
    from ..models.work_package_model_links_add_comment import WorkPackageModelLinksAddComment
    from ..models.work_package_model_links_add_file_link import WorkPackageModelLinksAddFileLink
    from ..models.work_package_model_links_add_relation import WorkPackageModelLinksAddRelation
    from ..models.work_package_model_links_add_watcher import WorkPackageModelLinksAddWatcher
    from ..models.work_package_model_links_ancestors_item import WorkPackageModelLinksAncestorsItem
    from ..models.work_package_model_links_assignee import WorkPackageModelLinksAssignee
    from ..models.work_package_model_links_attachments import WorkPackageModelLinksAttachments
    from ..models.work_package_model_links_author import WorkPackageModelLinksAuthor
    from ..models.work_package_model_links_available_watchers import WorkPackageModelLinksAvailableWatchers
    from ..models.work_package_model_links_budget import WorkPackageModelLinksBudget
    from ..models.work_package_model_links_category import WorkPackageModelLinksCategory
    from ..models.work_package_model_links_children_item import WorkPackageModelLinksChildrenItem
    from ..models.work_package_model_links_custom_actions_item import WorkPackageModelLinksCustomActionsItem
    from ..models.work_package_model_links_file_links import WorkPackageModelLinksFileLinks
    from ..models.work_package_model_links_parent import WorkPackageModelLinksParent
    from ..models.work_package_model_links_preview_markup import WorkPackageModelLinksPreviewMarkup
    from ..models.work_package_model_links_priority import WorkPackageModelLinksPriority
    from ..models.work_package_model_links_project import WorkPackageModelLinksProject
    from ..models.work_package_model_links_relations import WorkPackageModelLinksRelations
    from ..models.work_package_model_links_remove_watcher import WorkPackageModelLinksRemoveWatcher
    from ..models.work_package_model_links_responsible import WorkPackageModelLinksResponsible
    from ..models.work_package_model_links_revisions import WorkPackageModelLinksRevisions
    from ..models.work_package_model_links_schema import WorkPackageModelLinksSchema
    from ..models.work_package_model_links_self import WorkPackageModelLinksSelf
    from ..models.work_package_model_links_status import WorkPackageModelLinksStatus
    from ..models.work_package_model_links_time_entries import WorkPackageModelLinksTimeEntries
    from ..models.work_package_model_links_type import WorkPackageModelLinksType
    from ..models.work_package_model_links_unwatch import WorkPackageModelLinksUnwatch
    from ..models.work_package_model_links_update import WorkPackageModelLinksUpdate
    from ..models.work_package_model_links_update_immediately import WorkPackageModelLinksUpdateImmediately
    from ..models.work_package_model_links_version import WorkPackageModelLinksVersion
    from ..models.work_package_model_links_watch import WorkPackageModelLinksWatch
    from ..models.work_package_model_links_watchers import WorkPackageModelLinksWatchers


T = TypeVar("T", bound="WorkPackageModelLinks")


@attr.s(auto_attribs=True)
class WorkPackageModelLinks:
    """
    Attributes:
        self_ (WorkPackageModelLinksSelf):
        schema (WorkPackageModelLinksSchema):
        ancestors (List['WorkPackageModelLinksAncestorsItem']):
        attachments (WorkPackageModelLinksAttachments):
        author (WorkPackageModelLinksAuthor):
        children (List['WorkPackageModelLinksChildrenItem']):
        priority (WorkPackageModelLinksPriority):
        project (WorkPackageModelLinksProject):
        status (WorkPackageModelLinksStatus):
        type (WorkPackageModelLinksType):
        add_attachment (Union[Unset, WorkPackageModelLinksAddAttachment]):
        add_comment (Union[Unset, WorkPackageModelLinksAddComment]):
        add_relation (Union[Unset, WorkPackageModelLinksAddRelation]):
        add_watcher (Union[Unset, WorkPackageModelLinksAddWatcher]):
        custom_actions (Union[Unset, List['WorkPackageModelLinksCustomActionsItem']]):
        preview_markup (Union[Unset, WorkPackageModelLinksPreviewMarkup]):
        remove_watcher (Union[Unset, WorkPackageModelLinksRemoveWatcher]):
        unwatch (Union[Unset, WorkPackageModelLinksUnwatch]):
        update (Union[Unset, WorkPackageModelLinksUpdate]):
        update_immediately (Union[Unset, WorkPackageModelLinksUpdateImmediately]):
        watch (Union[Unset, WorkPackageModelLinksWatch]):
        assignee (Union[Unset, WorkPackageModelLinksAssignee]):
        available_watchers (Union[Unset, WorkPackageModelLinksAvailableWatchers]):
        budget (Union[Unset, WorkPackageModelLinksBudget]):
        category (Union[Unset, WorkPackageModelLinksCategory]):
        add_file_link (Union[Unset, WorkPackageModelLinksAddFileLink]):
        file_links (Union[Unset, WorkPackageModelLinksFileLinks]):
        parent (Union[Unset, WorkPackageModelLinksParent]):
        responsible (Union[Unset, WorkPackageModelLinksResponsible]):
        relations (Union[Unset, WorkPackageModelLinksRelations]):
        revisions (Union[Unset, WorkPackageModelLinksRevisions]):
        time_entries (Union[Unset, WorkPackageModelLinksTimeEntries]):
        version (Union[Unset, WorkPackageModelLinksVersion]):
        watchers (Union[Unset, WorkPackageModelLinksWatchers]):
    """

    self_: "WorkPackageModelLinksSelf"
    schema: "WorkPackageModelLinksSchema"
    ancestors: List["WorkPackageModelLinksAncestorsItem"]
    attachments: "WorkPackageModelLinksAttachments"
    author: "WorkPackageModelLinksAuthor"
    children: List["WorkPackageModelLinksChildrenItem"]
    priority: "WorkPackageModelLinksPriority"
    project: "WorkPackageModelLinksProject"
    status: "WorkPackageModelLinksStatus"
    type: "WorkPackageModelLinksType"
    add_attachment: Union[Unset, "WorkPackageModelLinksAddAttachment"] = UNSET
    add_comment: Union[Unset, "WorkPackageModelLinksAddComment"] = UNSET
    add_relation: Union[Unset, "WorkPackageModelLinksAddRelation"] = UNSET
    add_watcher: Union[Unset, "WorkPackageModelLinksAddWatcher"] = UNSET
    custom_actions: Union[Unset, List["WorkPackageModelLinksCustomActionsItem"]] = UNSET
    preview_markup: Union[Unset, "WorkPackageModelLinksPreviewMarkup"] = UNSET
    remove_watcher: Union[Unset, "WorkPackageModelLinksRemoveWatcher"] = UNSET
    unwatch: Union[Unset, "WorkPackageModelLinksUnwatch"] = UNSET
    update: Union[Unset, "WorkPackageModelLinksUpdate"] = UNSET
    update_immediately: Union[Unset, "WorkPackageModelLinksUpdateImmediately"] = UNSET
    watch: Union[Unset, "WorkPackageModelLinksWatch"] = UNSET
    assignee: Union[Unset, "WorkPackageModelLinksAssignee"] = UNSET
    available_watchers: Union[Unset, "WorkPackageModelLinksAvailableWatchers"] = UNSET
    budget: Union[Unset, "WorkPackageModelLinksBudget"] = UNSET
    category: Union[Unset, "WorkPackageModelLinksCategory"] = UNSET
    add_file_link: Union[Unset, "WorkPackageModelLinksAddFileLink"] = UNSET
    file_links: Union[Unset, "WorkPackageModelLinksFileLinks"] = UNSET
    parent: Union[Unset, "WorkPackageModelLinksParent"] = UNSET
    responsible: Union[Unset, "WorkPackageModelLinksResponsible"] = UNSET
    relations: Union[Unset, "WorkPackageModelLinksRelations"] = UNSET
    revisions: Union[Unset, "WorkPackageModelLinksRevisions"] = UNSET
    time_entries: Union[Unset, "WorkPackageModelLinksTimeEntries"] = UNSET
    version: Union[Unset, "WorkPackageModelLinksVersion"] = UNSET
    watchers: Union[Unset, "WorkPackageModelLinksWatchers"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        schema = self.schema.to_dict()

        ancestors = []
        for ancestors_item_data in self.ancestors:
            ancestors_item = ancestors_item_data.to_dict()

            ancestors.append(ancestors_item)

        attachments = self.attachments.to_dict()

        author = self.author.to_dict()

        children = []
        for children_item_data in self.children:
            children_item = children_item_data.to_dict()

            children.append(children_item)

        priority = self.priority.to_dict()

        project = self.project.to_dict()

        status = self.status.to_dict()

        type = self.type.to_dict()

        add_attachment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.add_attachment, Unset):
            add_attachment = self.add_attachment.to_dict()

        add_comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.add_comment, Unset):
            add_comment = self.add_comment.to_dict()

        add_relation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.add_relation, Unset):
            add_relation = self.add_relation.to_dict()

        add_watcher: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.add_watcher, Unset):
            add_watcher = self.add_watcher.to_dict()

        custom_actions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_actions, Unset):
            custom_actions = []
            for custom_actions_item_data in self.custom_actions:
                custom_actions_item = custom_actions_item_data.to_dict()

                custom_actions.append(custom_actions_item)

        preview_markup: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preview_markup, Unset):
            preview_markup = self.preview_markup.to_dict()

        remove_watcher: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remove_watcher, Unset):
            remove_watcher = self.remove_watcher.to_dict()

        unwatch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unwatch, Unset):
            unwatch = self.unwatch.to_dict()

        update: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.to_dict()

        update_immediately: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.update_immediately, Unset):
            update_immediately = self.update_immediately.to_dict()

        watch: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.watch, Unset):
            watch = self.watch.to_dict()

        assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        available_watchers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.available_watchers, Unset):
            available_watchers = self.available_watchers.to_dict()

        budget: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.budget, Unset):
            budget = self.budget.to_dict()

        category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        add_file_link: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.add_file_link, Unset):
            add_file_link = self.add_file_link.to_dict()

        file_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file_links, Unset):
            file_links = self.file_links.to_dict()

        parent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        responsible: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.responsible, Unset):
            responsible = self.responsible.to_dict()

        relations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relations, Unset):
            relations = self.relations.to_dict()

        revisions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.revisions, Unset):
            revisions = self.revisions.to_dict()

        time_entries: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.time_entries, Unset):
            time_entries = self.time_entries.to_dict()

        version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        watchers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.watchers, Unset):
            watchers = self.watchers.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "schema": schema,
                "ancestors": ancestors,
                "attachments": attachments,
                "author": author,
                "children": children,
                "priority": priority,
                "project": project,
                "status": status,
                "type": type,
            }
        )
        if add_attachment is not UNSET:
            field_dict["addAttachment"] = add_attachment
        if add_comment is not UNSET:
            field_dict["addComment"] = add_comment
        if add_relation is not UNSET:
            field_dict["addRelation"] = add_relation
        if add_watcher is not UNSET:
            field_dict["addWatcher"] = add_watcher
        if custom_actions is not UNSET:
            field_dict["customActions"] = custom_actions
        if preview_markup is not UNSET:
            field_dict["previewMarkup"] = preview_markup
        if remove_watcher is not UNSET:
            field_dict["removeWatcher"] = remove_watcher
        if unwatch is not UNSET:
            field_dict["unwatch"] = unwatch
        if update is not UNSET:
            field_dict["update"] = update
        if update_immediately is not UNSET:
            field_dict["updateImmediately"] = update_immediately
        if watch is not UNSET:
            field_dict["watch"] = watch
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if available_watchers is not UNSET:
            field_dict["availableWatchers"] = available_watchers
        if budget is not UNSET:
            field_dict["budget"] = budget
        if category is not UNSET:
            field_dict["category"] = category
        if add_file_link is not UNSET:
            field_dict["addFileLink"] = add_file_link
        if file_links is not UNSET:
            field_dict["fileLinks"] = file_links
        if parent is not UNSET:
            field_dict["parent"] = parent
        if responsible is not UNSET:
            field_dict["responsible"] = responsible
        if relations is not UNSET:
            field_dict["relations"] = relations
        if revisions is not UNSET:
            field_dict["revisions"] = revisions
        if time_entries is not UNSET:
            field_dict["timeEntries"] = time_entries
        if version is not UNSET:
            field_dict["version"] = version
        if watchers is not UNSET:
            field_dict["watchers"] = watchers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.work_package_model_links_add_attachment import WorkPackageModelLinksAddAttachment
        from ..models.work_package_model_links_add_comment import WorkPackageModelLinksAddComment
        from ..models.work_package_model_links_add_file_link import WorkPackageModelLinksAddFileLink
        from ..models.work_package_model_links_add_relation import WorkPackageModelLinksAddRelation
        from ..models.work_package_model_links_add_watcher import WorkPackageModelLinksAddWatcher
        from ..models.work_package_model_links_ancestors_item import WorkPackageModelLinksAncestorsItem
        from ..models.work_package_model_links_assignee import WorkPackageModelLinksAssignee
        from ..models.work_package_model_links_attachments import WorkPackageModelLinksAttachments
        from ..models.work_package_model_links_author import WorkPackageModelLinksAuthor
        from ..models.work_package_model_links_available_watchers import WorkPackageModelLinksAvailableWatchers
        from ..models.work_package_model_links_budget import WorkPackageModelLinksBudget
        from ..models.work_package_model_links_category import WorkPackageModelLinksCategory
        from ..models.work_package_model_links_children_item import WorkPackageModelLinksChildrenItem
        from ..models.work_package_model_links_custom_actions_item import WorkPackageModelLinksCustomActionsItem
        from ..models.work_package_model_links_file_links import WorkPackageModelLinksFileLinks
        from ..models.work_package_model_links_parent import WorkPackageModelLinksParent
        from ..models.work_package_model_links_preview_markup import WorkPackageModelLinksPreviewMarkup
        from ..models.work_package_model_links_priority import WorkPackageModelLinksPriority
        from ..models.work_package_model_links_project import WorkPackageModelLinksProject
        from ..models.work_package_model_links_relations import WorkPackageModelLinksRelations
        from ..models.work_package_model_links_remove_watcher import WorkPackageModelLinksRemoveWatcher
        from ..models.work_package_model_links_responsible import WorkPackageModelLinksResponsible
        from ..models.work_package_model_links_revisions import WorkPackageModelLinksRevisions
        from ..models.work_package_model_links_schema import WorkPackageModelLinksSchema
        from ..models.work_package_model_links_self import WorkPackageModelLinksSelf
        from ..models.work_package_model_links_status import WorkPackageModelLinksStatus
        from ..models.work_package_model_links_time_entries import WorkPackageModelLinksTimeEntries
        from ..models.work_package_model_links_type import WorkPackageModelLinksType
        from ..models.work_package_model_links_unwatch import WorkPackageModelLinksUnwatch
        from ..models.work_package_model_links_update import WorkPackageModelLinksUpdate
        from ..models.work_package_model_links_update_immediately import WorkPackageModelLinksUpdateImmediately
        from ..models.work_package_model_links_version import WorkPackageModelLinksVersion
        from ..models.work_package_model_links_watch import WorkPackageModelLinksWatch
        from ..models.work_package_model_links_watchers import WorkPackageModelLinksWatchers

        d = src_dict.copy()
        self_ = WorkPackageModelLinksSelf.from_dict(d.pop("self"))

        schema = WorkPackageModelLinksSchema.from_dict(d.pop("schema"))

        ancestors = []
        _ancestors = d.pop("ancestors")
        for ancestors_item_data in _ancestors:
            ancestors_item = WorkPackageModelLinksAncestorsItem.from_dict(ancestors_item_data)

            ancestors.append(ancestors_item)

        attachments = WorkPackageModelLinksAttachments.from_dict(d.pop("attachments"))

        author = WorkPackageModelLinksAuthor.from_dict(d.pop("author"))

        children = []
        _children = d.pop("children")
        for children_item_data in _children:
            children_item = WorkPackageModelLinksChildrenItem.from_dict(children_item_data)

            children.append(children_item)

        priority = WorkPackageModelLinksPriority.from_dict(d.pop("priority"))

        project = WorkPackageModelLinksProject.from_dict(d.pop("project"))

        status = WorkPackageModelLinksStatus.from_dict(d.pop("status"))

        type = WorkPackageModelLinksType.from_dict(d.pop("type"))

        _add_attachment = d.pop("addAttachment", UNSET)
        add_attachment: Union[Unset, WorkPackageModelLinksAddAttachment]
        if isinstance(_add_attachment, Unset):
            add_attachment = UNSET
        else:
            add_attachment = WorkPackageModelLinksAddAttachment.from_dict(_add_attachment)

        _add_comment = d.pop("addComment", UNSET)
        add_comment: Union[Unset, WorkPackageModelLinksAddComment]
        if isinstance(_add_comment, Unset):
            add_comment = UNSET
        else:
            add_comment = WorkPackageModelLinksAddComment.from_dict(_add_comment)

        _add_relation = d.pop("addRelation", UNSET)
        add_relation: Union[Unset, WorkPackageModelLinksAddRelation]
        if isinstance(_add_relation, Unset):
            add_relation = UNSET
        else:
            add_relation = WorkPackageModelLinksAddRelation.from_dict(_add_relation)

        _add_watcher = d.pop("addWatcher", UNSET)
        add_watcher: Union[Unset, WorkPackageModelLinksAddWatcher]
        if isinstance(_add_watcher, Unset):
            add_watcher = UNSET
        else:
            add_watcher = WorkPackageModelLinksAddWatcher.from_dict(_add_watcher)

        custom_actions = []
        _custom_actions = d.pop("customActions", UNSET)
        for custom_actions_item_data in _custom_actions or []:
            custom_actions_item = WorkPackageModelLinksCustomActionsItem.from_dict(custom_actions_item_data)

            custom_actions.append(custom_actions_item)

        _preview_markup = d.pop("previewMarkup", UNSET)
        preview_markup: Union[Unset, WorkPackageModelLinksPreviewMarkup]
        if isinstance(_preview_markup, Unset):
            preview_markup = UNSET
        else:
            preview_markup = WorkPackageModelLinksPreviewMarkup.from_dict(_preview_markup)

        _remove_watcher = d.pop("removeWatcher", UNSET)
        remove_watcher: Union[Unset, WorkPackageModelLinksRemoveWatcher]
        if isinstance(_remove_watcher, Unset):
            remove_watcher = UNSET
        else:
            remove_watcher = WorkPackageModelLinksRemoveWatcher.from_dict(_remove_watcher)

        _unwatch = d.pop("unwatch", UNSET)
        unwatch: Union[Unset, WorkPackageModelLinksUnwatch]
        if isinstance(_unwatch, Unset):
            unwatch = UNSET
        else:
            unwatch = WorkPackageModelLinksUnwatch.from_dict(_unwatch)

        _update = d.pop("update", UNSET)
        update: Union[Unset, WorkPackageModelLinksUpdate]
        if isinstance(_update, Unset):
            update = UNSET
        else:
            update = WorkPackageModelLinksUpdate.from_dict(_update)

        _update_immediately = d.pop("updateImmediately", UNSET)
        update_immediately: Union[Unset, WorkPackageModelLinksUpdateImmediately]
        if isinstance(_update_immediately, Unset):
            update_immediately = UNSET
        else:
            update_immediately = WorkPackageModelLinksUpdateImmediately.from_dict(_update_immediately)

        _watch = d.pop("watch", UNSET)
        watch: Union[Unset, WorkPackageModelLinksWatch]
        if isinstance(_watch, Unset):
            watch = UNSET
        else:
            watch = WorkPackageModelLinksWatch.from_dict(_watch)

        _assignee = d.pop("assignee", UNSET)
        assignee: Union[Unset, WorkPackageModelLinksAssignee]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = WorkPackageModelLinksAssignee.from_dict(_assignee)

        _available_watchers = d.pop("availableWatchers", UNSET)
        available_watchers: Union[Unset, WorkPackageModelLinksAvailableWatchers]
        if isinstance(_available_watchers, Unset):
            available_watchers = UNSET
        else:
            available_watchers = WorkPackageModelLinksAvailableWatchers.from_dict(_available_watchers)

        _budget = d.pop("budget", UNSET)
        budget: Union[Unset, WorkPackageModelLinksBudget]
        if isinstance(_budget, Unset):
            budget = UNSET
        else:
            budget = WorkPackageModelLinksBudget.from_dict(_budget)

        _category = d.pop("category", UNSET)
        category: Union[Unset, WorkPackageModelLinksCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = WorkPackageModelLinksCategory.from_dict(_category)

        _add_file_link = d.pop("addFileLink", UNSET)
        add_file_link: Union[Unset, WorkPackageModelLinksAddFileLink]
        if isinstance(_add_file_link, Unset):
            add_file_link = UNSET
        else:
            add_file_link = WorkPackageModelLinksAddFileLink.from_dict(_add_file_link)

        _file_links = d.pop("fileLinks", UNSET)
        file_links: Union[Unset, WorkPackageModelLinksFileLinks]
        if isinstance(_file_links, Unset):
            file_links = UNSET
        else:
            file_links = WorkPackageModelLinksFileLinks.from_dict(_file_links)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, WorkPackageModelLinksParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = WorkPackageModelLinksParent.from_dict(_parent)

        _responsible = d.pop("responsible", UNSET)
        responsible: Union[Unset, WorkPackageModelLinksResponsible]
        if isinstance(_responsible, Unset):
            responsible = UNSET
        else:
            responsible = WorkPackageModelLinksResponsible.from_dict(_responsible)

        _relations = d.pop("relations", UNSET)
        relations: Union[Unset, WorkPackageModelLinksRelations]
        if isinstance(_relations, Unset):
            relations = UNSET
        else:
            relations = WorkPackageModelLinksRelations.from_dict(_relations)

        _revisions = d.pop("revisions", UNSET)
        revisions: Union[Unset, WorkPackageModelLinksRevisions]
        if isinstance(_revisions, Unset):
            revisions = UNSET
        else:
            revisions = WorkPackageModelLinksRevisions.from_dict(_revisions)

        _time_entries = d.pop("timeEntries", UNSET)
        time_entries: Union[Unset, WorkPackageModelLinksTimeEntries]
        if isinstance(_time_entries, Unset):
            time_entries = UNSET
        else:
            time_entries = WorkPackageModelLinksTimeEntries.from_dict(_time_entries)

        _version = d.pop("version", UNSET)
        version: Union[Unset, WorkPackageModelLinksVersion]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = WorkPackageModelLinksVersion.from_dict(_version)

        _watchers = d.pop("watchers", UNSET)
        watchers: Union[Unset, WorkPackageModelLinksWatchers]
        if isinstance(_watchers, Unset):
            watchers = UNSET
        else:
            watchers = WorkPackageModelLinksWatchers.from_dict(_watchers)

        work_package_model_links = cls(
            self_=self_,
            schema=schema,
            ancestors=ancestors,
            attachments=attachments,
            author=author,
            children=children,
            priority=priority,
            project=project,
            status=status,
            type=type,
            add_attachment=add_attachment,
            add_comment=add_comment,
            add_relation=add_relation,
            add_watcher=add_watcher,
            custom_actions=custom_actions,
            preview_markup=preview_markup,
            remove_watcher=remove_watcher,
            unwatch=unwatch,
            update=update,
            update_immediately=update_immediately,
            watch=watch,
            assignee=assignee,
            available_watchers=available_watchers,
            budget=budget,
            category=category,
            add_file_link=add_file_link,
            file_links=file_links,
            parent=parent,
            responsible=responsible,
            relations=relations,
            revisions=revisions,
            time_entries=time_entries,
            version=version,
            watchers=watchers,
        )

        work_package_model_links.additional_properties = d
        return work_package_model_links

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
