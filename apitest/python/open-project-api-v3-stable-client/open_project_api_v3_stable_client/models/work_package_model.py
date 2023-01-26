import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.work_package_model_type import WorkPackageModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.work_package_model_description import WorkPackageModelDescription
    from ..models.work_package_model_links import WorkPackageModelLinks


T = TypeVar("T", bound="WorkPackageModel")


@attr.s(auto_attribs=True)
class WorkPackageModel:
    """
    Example:
        {'_type': 'WorkPackage', '_links': {'self': {'href': '/api/v3/work_packages/1528', 'title': 'Develop API'},
            'schema': {'href': '/api/v3/work_packages/schemas/11-2'}, 'update': {'href': '/api/v3/work_packages/1528',
            'method': 'patch', 'title': 'Update Develop API'}, 'delete': {'href': '/work_packages/bulk?ids=1528', 'method':
            'delete', 'title': 'Delete Develop API'}, 'logTime': {'href': '/work_packages/1528/time_entries/new', 'type':
            'text/html', 'title': 'Log time on Develop API'}, 'move': {'href': '/work_packages/1528/move/new', 'type':
            'text/html', 'title': 'Move Develop API'}, 'attachments': {'href': '/api/v3/work_packages/1528/attachments'},
            'addAttachment': {'href': '/api/v3/work_packages/1528/attachments', 'method': 'post'}, 'author': {'href':
            '/api/v3/users/1', 'title': 'OpenProject Admin - admin'}, 'customActions': [{'href':
            '/api/v3/work_packages/1528/custom_actions/153/execute', 'method': 'post', 'title': 'Reset'}, {'href':
            '/api/v3/work_packages/1528/custom_actions/94/execute', 'method': 'post', 'title': 'Forward to accounting'}],
            'responsible': {'href': '/api/v3/users/23', 'title': 'Laron Leuschke - Alaina5788'}, 'relations': {'href':
            '/api/v3/work_packages/1528/relations', 'title': 'Show relations'}, 'revisions': {'href':
            '/api/v3/work_packages/1528/revisions'}, 'assignee': {'href': '/api/v3/users/11', 'title': 'Emmie Okuneva -
            Adele5450'}, 'priority': {'href': '/api/v3/priorities/2', 'title': 'Normal'}, 'project': {'href':
            '/api/v3/projects/1', 'title': 'A Test Project'}, 'status': {'href': '/api/v3/statuses/1', 'title': 'New'},
            'type': {'href': '/api/v3/types/1', 'title': 'A Type'}, 'version': {'href': '/api/v3/versions/1', 'title':
            'Version 1'}, 'availableWatchers': {'href': '/api/v3/work_packages/1528/available_watchers'}, 'watch': {'href':
            '/api/v3/work_packages/1528/watchers', 'method': 'post', 'payload': {'user': {'href': '/api/v3/users/1'}}},
            'addWatcher': {'href': '/api/v3/work_packages/1528/watchers', 'method': 'post', 'payload': {'user': {'href':
            '/api/v3/users/{user_id}'}}, 'templated': True}, 'removeWatcher': {'href':
            '/api/v3/work_packages/1528/watchers/{user_id}', 'method': 'delete', 'templated': True}, 'addRelation': {'href':
            '/api/v3/relations', 'method': 'post', 'title': 'Add relation'}, 'changeParent': {'href':
            '/api/v3/work_packages/694', 'method': 'patch', 'title': 'Change parent of Bug in OpenProject'}, 'addComment':
            {'href': '/api/v3/work_packages/1528/activities', 'method': 'post', 'title': 'Add comment'}, 'parent': {'href':
            '/api/v3/work_packages/1298', 'title': 'nisi eligendi officiis eos delectus quis voluptas dolores'}, 'category':
            {'href': '/api/v3/categories/1298', 'title': 'eligend isi'}, 'children': [{'href': '/api/v3/work_packages/1529',
            'title': 'Write API documentation'}], 'ancestors': [{'href': '/api/v3/work_packages/1290', 'title': 'Root node
            of hierarchy'}, {'href': '/api/v3/work_packages/1291', 'title': 'Intermediate node of hierarchy'}, {'href':
            '/api/v3/work_packages/1298', 'title': 'nisi eligendi officiis eos delectus quis voluptas dolores'}],
            'timeEntries': {'href': '/work_packages/1528/time_entries', 'type': 'text/html', 'title': 'Time entries'},
            'watchers': {'href': '/api/v3/work_packages/1528/watchers'}, 'customField3': {'href': 'api/v3/users/14'}}, 'id':
            1528, 'subject': 'Develop API', 'description': {'format': 'markdown', 'raw': 'Develop super cool OpenProject
            API.', 'html': '<p>Develop super cool OpenProject API.</p>'}, 'scheduleManually': False, 'readonly': False,
            'startDate': None, 'dueDate': None, 'derivedStartDate': None, 'derivedDueDate': None, 'estimatedTime': 'PT2H',
            'derivedEstimatedTime': 'PT10H', 'percentageDone': 0, 'customField1': 'Foo', 'customField2': 42, 'createdAt':
            '2014-08-29T12:40:53Z', 'updatedAt': '2014-08-29T12:44:41Z'}

    Attributes:
        subject (str): Work package subject
        field_links (WorkPackageModelLinks):
        id (Union[Unset, int]): Work package id
        lock_version (Union[Unset, int]): The version of the item as used for optimistic locking
        field_type (Union[Unset, WorkPackageModelType]):
        description (Union[Unset, WorkPackageModelDescription]):
        schedule_manually (Union[Unset, bool]): If false (default) schedule automatically.
        readonly (Union[Unset, bool]): If true, the work package is in a readonly status so with the exception of the
            status, no other property can be altered.
        start_date (Union[Unset, datetime.date]): Scheduled beginning of a work package
        due_date (Union[Unset, datetime.date]): Scheduled end of a work package
        date (Union[Unset, datetime.date]): Date on which a milestone is achieved
        derived_start_date (Union[Unset, datetime.date]): Similar to start date but is not set by a client but rather
            deduced by the work packages' descendants. If manual scheduleManually is active, the two dates can deviate.
        derived_due_date (Union[Unset, datetime.date]): Similar to due date but is not set by a client but rather
            deduced by the work packages' descendants. If manual scheduleManually is active, the two dates can deviate.
        duration (Union[Unset, str]): **(NOT IMPLEMENTED)** The amount of time in hours the work package needs to be
            completed.
            Not available for milestone type of work packages.
        estimated_time (Union[Unset, str]): Time a work package likely needs to be completed excluding its descendants
        derived_estimated_time (Union[Unset, str]): Time a work package likely needs to be completed including its
            descendants
        ignore_non_working_days (Union[Unset, bool]): **(NOT IMPLEMENTED)** When scheduling, whether or not to ignore
            the non working days being defined.
            A work package with the flag set to true will be allowed to be scheduled to a non working day.
        spent_time (Union[Unset, str]): The time booked for this work package by users working on it

            # Conditions

            **Permission** view time entries
        percentage_done (Union[Unset, int]): Amount of total completion for a work package
        created_at (Union[Unset, datetime.datetime]): Time of creation
        updated_at (Union[Unset, datetime.datetime]): Time of the most recent change to the work package
    """

    subject: str
    field_links: "WorkPackageModelLinks"
    id: Union[Unset, int] = UNSET
    lock_version: Union[Unset, int] = UNSET
    field_type: Union[Unset, WorkPackageModelType] = UNSET
    description: Union[Unset, "WorkPackageModelDescription"] = UNSET
    schedule_manually: Union[Unset, bool] = UNSET
    readonly: Union[Unset, bool] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    derived_start_date: Union[Unset, datetime.date] = UNSET
    derived_due_date: Union[Unset, datetime.date] = UNSET
    duration: Union[Unset, str] = UNSET
    estimated_time: Union[Unset, str] = UNSET
    derived_estimated_time: Union[Unset, str] = UNSET
    ignore_non_working_days: Union[Unset, bool] = UNSET
    spent_time: Union[Unset, str] = UNSET
    percentage_done: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        field_links = self.field_links.to_dict()

        id = self.id
        lock_version = self.lock_version
        field_type: Union[Unset, str] = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value

        description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

        schedule_manually = self.schedule_manually
        readonly = self.readonly
        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        derived_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.derived_start_date, Unset):
            derived_start_date = self.derived_start_date.isoformat()

        derived_due_date: Union[Unset, str] = UNSET
        if not isinstance(self.derived_due_date, Unset):
            derived_due_date = self.derived_due_date.isoformat()

        duration = self.duration
        estimated_time = self.estimated_time
        derived_estimated_time = self.derived_estimated_time
        ignore_non_working_days = self.ignore_non_working_days
        spent_time = self.spent_time
        percentage_done = self.percentage_done
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject": subject,
                "_links": field_links,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if lock_version is not UNSET:
            field_dict["lockVersion"] = lock_version
        if field_type is not UNSET:
            field_dict["_type"] = field_type
        if description is not UNSET:
            field_dict["description"] = description
        if schedule_manually is not UNSET:
            field_dict["scheduleManually"] = schedule_manually
        if readonly is not UNSET:
            field_dict["readonly"] = readonly
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if date is not UNSET:
            field_dict["date"] = date
        if derived_start_date is not UNSET:
            field_dict["derivedStartDate"] = derived_start_date
        if derived_due_date is not UNSET:
            field_dict["derivedDueDate"] = derived_due_date
        if duration is not UNSET:
            field_dict["duration"] = duration
        if estimated_time is not UNSET:
            field_dict["estimatedTime"] = estimated_time
        if derived_estimated_time is not UNSET:
            field_dict["derivedEstimatedTime"] = derived_estimated_time
        if ignore_non_working_days is not UNSET:
            field_dict["ignoreNonWorkingDays"] = ignore_non_working_days
        if spent_time is not UNSET:
            field_dict["spentTime"] = spent_time
        if percentage_done is not UNSET:
            field_dict["percentageDone"] = percentage_done
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.work_package_model_description import WorkPackageModelDescription
        from ..models.work_package_model_links import WorkPackageModelLinks

        d = src_dict.copy()
        subject = d.pop("subject")

        field_links = WorkPackageModelLinks.from_dict(d.pop("_links"))

        id = d.pop("id", UNSET)

        lock_version = d.pop("lockVersion", UNSET)

        _field_type = d.pop("_type", UNSET)
        field_type: Union[Unset, WorkPackageModelType]
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = WorkPackageModelType(_field_type)

        _description = d.pop("description", UNSET)
        description: Union[Unset, WorkPackageModelDescription]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = WorkPackageModelDescription.from_dict(_description)

        schedule_manually = d.pop("scheduleManually", UNSET)

        readonly = d.pop("readonly", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.date]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        _derived_start_date = d.pop("derivedStartDate", UNSET)
        derived_start_date: Union[Unset, datetime.date]
        if isinstance(_derived_start_date, Unset):
            derived_start_date = UNSET
        else:
            derived_start_date = isoparse(_derived_start_date).date()

        _derived_due_date = d.pop("derivedDueDate", UNSET)
        derived_due_date: Union[Unset, datetime.date]
        if isinstance(_derived_due_date, Unset):
            derived_due_date = UNSET
        else:
            derived_due_date = isoparse(_derived_due_date).date()

        duration = d.pop("duration", UNSET)

        estimated_time = d.pop("estimatedTime", UNSET)

        derived_estimated_time = d.pop("derivedEstimatedTime", UNSET)

        ignore_non_working_days = d.pop("ignoreNonWorkingDays", UNSET)

        spent_time = d.pop("spentTime", UNSET)

        percentage_done = d.pop("percentageDone", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        work_package_model = cls(
            subject=subject,
            field_links=field_links,
            id=id,
            lock_version=lock_version,
            field_type=field_type,
            description=description,
            schedule_manually=schedule_manually,
            readonly=readonly,
            start_date=start_date,
            due_date=due_date,
            date=date,
            derived_start_date=derived_start_date,
            derived_due_date=derived_due_date,
            duration=duration,
            estimated_time=estimated_time,
            derived_estimated_time=derived_estimated_time,
            ignore_non_working_days=ignore_non_working_days,
            spent_time=spent_time,
            percentage_done=percentage_done,
            created_at=created_at,
            updated_at=updated_at,
        )

        work_package_model.additional_properties = d
        return work_package_model

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
