from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_model import ActivityModel
    from ..models.project_model import ProjectModel
    from ..models.user_model import UserModel
    from ..models.work_package_model import WorkPackageModel


T = TypeVar("T", bound="NotificationModelEmbedded")


@attr.s(auto_attribs=True)
class NotificationModelEmbedded:
    """
    Attributes:
        project (ProjectModel):
        resource (WorkPackageModel):  Example: {'_type': 'WorkPackage', '_links': {'self': {'href':
            '/api/v3/work_packages/1528', 'title': 'Develop API'}, 'schema': {'href': '/api/v3/work_packages/schemas/11-2'},
            'update': {'href': '/api/v3/work_packages/1528', 'method': 'patch', 'title': 'Update Develop API'}, 'delete':
            {'href': '/work_packages/bulk?ids=1528', 'method': 'delete', 'title': 'Delete Develop API'}, 'logTime': {'href':
            '/work_packages/1528/time_entries/new', 'type': 'text/html', 'title': 'Log time on Develop API'}, 'move':
            {'href': '/work_packages/1528/move/new', 'type': 'text/html', 'title': 'Move Develop API'}, 'attachments':
            {'href': '/api/v3/work_packages/1528/attachments'}, 'addAttachment': {'href':
            '/api/v3/work_packages/1528/attachments', 'method': 'post'}, 'author': {'href': '/api/v3/users/1', 'title':
            'OpenProject Admin - admin'}, 'customActions': [{'href':
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
            '2014-08-29T12:40:53Z', 'updatedAt': '2014-08-29T12:44:41Z'}.
        actor (Union[Unset, UserModel]):  Example: {'_type': 'User', 'id': 1, 'name': 'John Sheppard', 'login':
            'j.sheppard', 'firstName': 'John', 'lastName': 'Sheppard', 'email': 'shep@mail.com', 'admin': True, 'avatar':
            'https://example.org/users/1/avatar', 'status': 'active', 'identityUrl': 'null,', 'language': 'en', 'createdAt':
            '2014-05-21T08:51:20Z', 'updatedAt': '2014-05-21T08:51:20Z', '_links': {'self': {'href': '/api/v3/users/1',
            'title': 'John Sheppard'}, 'memberships': {'href': '/api/v3/memberships?filters=%5B%7B%22principal%22%3A%7B%22op
            erator%22%3A%22%3D%22%2C%22values%22%3A%5B%221%22%5D%7D%7D%5D,', 'title': 'Members'}, 'showUser': {'href':
            '/users/1', 'type': 'text/html'}, 'lock': {'href': '/api/v3/users/1/lock', 'title': 'Set lock on John Sheppard',
            'method': 'post'}, 'updateImmediately': {'href': '/api/v3/users/1', 'title': 'update John Sheppard', 'method':
            'patch'}, 'delete': {'href': '/api/v3/users/1', 'title': 'delete John Sheppard'}, 'method': 'delete'}}.
        activity (Union[Unset, ActivityModel]):  Example: {'_type': 'Activity::Comment', '_links': {'self': {'href':
            '/api/v3/activity/1', 'title': 'Priority changed from High to Low'}, 'workPackage': {'href':
            '/api/v3/work_packages/1', 'title': 'quis numquam qui voluptatum quia praesentium blanditiis nisi'}, 'user':
            {'href': '/api/v3/users/1', 'title': 'John Sheppard - admin'}}, 'id': 1, 'details': [{'format': 'markdown',
            'raw': 'Lorem ipsum dolor sit amet.', 'html': '<p>Lorem ipsum dolor sit amet.</p>'}], 'comment': {'format':
            'markdown', 'raw': 'Lorem ipsum dolor sit amet.', 'html': '<p>Lorem ipsum dolor sit amet.</p>'}, 'createdAt':
            '2014-05-21T08:51:20Z', 'updatedAt': '2014-05-21T09:14:02Z', 'version': 31}.
    """

    project: "ProjectModel"
    resource: "WorkPackageModel"
    actor: Union[Unset, "UserModel"] = UNSET
    activity: Union[Unset, "ActivityModel"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project = self.project.to_dict()

        resource = self.resource.to_dict()

        actor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actor, Unset):
            actor = self.actor.to_dict()

        activity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.activity, Unset):
            activity = self.activity.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project": project,
                "resource": resource,
            }
        )
        if actor is not UNSET:
            field_dict["actor"] = actor
        if activity is not UNSET:
            field_dict["activity"] = activity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.activity_model import ActivityModel
        from ..models.project_model import ProjectModel
        from ..models.user_model import UserModel
        from ..models.work_package_model import WorkPackageModel

        d = src_dict.copy()
        project = ProjectModel.from_dict(d.pop("project"))

        resource = WorkPackageModel.from_dict(d.pop("resource"))

        _actor = d.pop("actor", UNSET)
        actor: Union[Unset, UserModel]
        if isinstance(_actor, Unset):
            actor = UNSET
        else:
            actor = UserModel.from_dict(_actor)

        _activity = d.pop("activity", UNSET)
        activity: Union[Unset, ActivityModel]
        if isinstance(_activity, Unset):
            activity = UNSET
        else:
            activity = ActivityModel.from_dict(_activity)

        notification_model_embedded = cls(
            project=project,
            resource=resource,
            actor=actor,
            activity=activity,
        )

        notification_model_embedded.additional_properties = d
        return notification_model_embedded

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
