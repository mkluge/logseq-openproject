from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.storage_model import StorageModel
    from ..models.work_package_model import WorkPackageModel


T = TypeVar("T", bound="FileLinkReadModelEmbedded")


@attr.s(auto_attribs=True)
class FileLinkReadModelEmbedded:
    """
    Attributes:
        storage (StorageModel):  Example: {'id': 1337, '_type': 'Storage', 'name': "It's no moon", 'createdAt':
            '2021-12-20T13:37:00.211Z', 'updatedAt': '2021-12-20T13:37:00.211Z', '_links': {'self': {'href':
            '/api/v3/storages/1337', 'title': "It's no moon"}, 'type': {'href': 'urn:openproject-
            org:api:v3:storages:nextcloud', 'title': 'Nextcloud'}, 'origin': {'href': 'https://nextcloud.deathstar.rocks/'},
            'open': {'href': 'https://nextcloud.deathstar.rocks/apps/files'}, 'authorizationState': {'href':
            'urn:openproject-org:api:v3:storages:authorization:FailedAuthorization', 'title': 'Failed Authorization'},
            'authorize': {'href': 'https://nextcloud.deathstar.rocks/authorize/', 'title': 'Authorize'}}}.
        container (WorkPackageModel):  Example: {'_type': 'WorkPackage', '_links': {'self': {'href':
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
    """

    storage: "StorageModel"
    container: "WorkPackageModel"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        storage = self.storage.to_dict()

        container = self.container.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "storage": storage,
                "container": container,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.storage_model import StorageModel
        from ..models.work_package_model import WorkPackageModel

        d = src_dict.copy()
        storage = StorageModel.from_dict(d.pop("storage"))

        container = WorkPackageModel.from_dict(d.pop("container"))

        file_link_read_model_embedded = cls(
            storage=storage,
            container=container,
        )

        file_link_read_model_embedded.additional_properties = d
        return file_link_read_model_embedded

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
