from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.work_package_model import WorkPackageModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: WorkPackageModel,
    notify: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/api/v3/work_packages".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["notify"] = notify

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, WorkPackageModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WorkPackageModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = cast(Any, None)
        return response_406
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = cast(Any, None)
        return response_415
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ErrorResponse, WorkPackageModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: WorkPackageModel,
    notify: Union[Unset, None, bool] = True,
) -> Response[Union[Any, ErrorResponse, WorkPackageModel]]:
    """Create Work Package

     When calling this endpoint the client provides a single object, containing at least the properties
    and links that are required, in the body.
    The required fields of a WorkPackage can be found in its schema, which is embedded in the respective
    form.
    Note that it is only allowed to provide properties or links supporting the write operation.

    A project link must be set when creating work packages through this route.

    When setting start date, finish date, and duration together, their correctness will be checked and a
    422 error will be returned if one value does not match with the two others. You can make the server
    compute a value: set only two values in the request and the third one will be computed and returned
    in the response. For instance, when sending `{ \"startDate\": \"2022-08-23\", duration: \"P2D\" }`,
    the response will include `{ \"dueDate\": \"2022-08-24\" }`.

    Args:
        notify (Union[Unset, None, bool]):  Default: True.
        json_body (WorkPackageModel):  Example: {'_type': 'WorkPackage', '_links': {'self':
            {'href': '/api/v3/work_packages/1528', 'title': 'Develop API'}, 'schema': {'href':
            '/api/v3/work_packages/schemas/11-2'}, 'update': {'href': '/api/v3/work_packages/1528',
            'method': 'patch', 'title': 'Update Develop API'}, 'delete': {'href':
            '/work_packages/bulk?ids=1528', 'method': 'delete', 'title': 'Delete Develop API'},
            'logTime': {'href': '/work_packages/1528/time_entries/new', 'type': 'text/html', 'title':
            'Log time on Develop API'}, 'move': {'href': '/work_packages/1528/move/new', 'type':
            'text/html', 'title': 'Move Develop API'}, 'attachments': {'href':
            '/api/v3/work_packages/1528/attachments'}, 'addAttachment': {'href':
            '/api/v3/work_packages/1528/attachments', 'method': 'post'}, 'author': {'href':
            '/api/v3/users/1', 'title': 'OpenProject Admin - admin'}, 'customActions': [{'href':
            '/api/v3/work_packages/1528/custom_actions/153/execute', 'method': 'post', 'title':
            'Reset'}, {'href': '/api/v3/work_packages/1528/custom_actions/94/execute', 'method':
            'post', 'title': 'Forward to accounting'}], 'responsible': {'href': '/api/v3/users/23',
            'title': 'Laron Leuschke - Alaina5788'}, 'relations': {'href':
            '/api/v3/work_packages/1528/relations', 'title': 'Show relations'}, 'revisions': {'href':
            '/api/v3/work_packages/1528/revisions'}, 'assignee': {'href': '/api/v3/users/11', 'title':
            'Emmie Okuneva - Adele5450'}, 'priority': {'href': '/api/v3/priorities/2', 'title':
            'Normal'}, 'project': {'href': '/api/v3/projects/1', 'title': 'A Test Project'}, 'status':
            {'href': '/api/v3/statuses/1', 'title': 'New'}, 'type': {'href': '/api/v3/types/1',
            'title': 'A Type'}, 'version': {'href': '/api/v3/versions/1', 'title': 'Version 1'},
            'availableWatchers': {'href': '/api/v3/work_packages/1528/available_watchers'}, 'watch':
            {'href': '/api/v3/work_packages/1528/watchers', 'method': 'post', 'payload': {'user':
            {'href': '/api/v3/users/1'}}}, 'addWatcher': {'href':
            '/api/v3/work_packages/1528/watchers', 'method': 'post', 'payload': {'user': {'href':
            '/api/v3/users/{user_id}'}}, 'templated': True}, 'removeWatcher': {'href':
            '/api/v3/work_packages/1528/watchers/{user_id}', 'method': 'delete', 'templated': True},
            'addRelation': {'href': '/api/v3/relations', 'method': 'post', 'title': 'Add relation'},
            'changeParent': {'href': '/api/v3/work_packages/694', 'method': 'patch', 'title': 'Change
            parent of Bug in OpenProject'}, 'addComment': {'href':
            '/api/v3/work_packages/1528/activities', 'method': 'post', 'title': 'Add comment'},
            'parent': {'href': '/api/v3/work_packages/1298', 'title': 'nisi eligendi officiis eos
            delectus quis voluptas dolores'}, 'category': {'href': '/api/v3/categories/1298', 'title':
            'eligend isi'}, 'children': [{'href': '/api/v3/work_packages/1529', 'title': 'Write API
            documentation'}], 'ancestors': [{'href': '/api/v3/work_packages/1290', 'title': 'Root node
            of hierarchy'}, {'href': '/api/v3/work_packages/1291', 'title': 'Intermediate node of
            hierarchy'}, {'href': '/api/v3/work_packages/1298', 'title': 'nisi eligendi officiis eos
            delectus quis voluptas dolores'}], 'timeEntries': {'href':
            '/work_packages/1528/time_entries', 'type': 'text/html', 'title': 'Time entries'},
            'watchers': {'href': '/api/v3/work_packages/1528/watchers'}, 'customField3': {'href':
            'api/v3/users/14'}}, 'id': 1528, 'subject': 'Develop API', 'description': {'format':
            'markdown', 'raw': 'Develop super cool OpenProject API.', 'html': '<p>Develop super cool
            OpenProject API.</p>'}, 'scheduleManually': False, 'readonly': False, 'startDate': None,
            'dueDate': None, 'derivedStartDate': None, 'derivedDueDate': None, 'estimatedTime':
            'PT2H', 'derivedEstimatedTime': 'PT10H', 'percentageDone': 0, 'customField1': 'Foo',
            'customField2': 42, 'createdAt': '2014-08-29T12:40:53Z', 'updatedAt':
            '2014-08-29T12:44:41Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackageModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        notify=notify,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: WorkPackageModel,
    notify: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, ErrorResponse, WorkPackageModel]]:
    """Create Work Package

     When calling this endpoint the client provides a single object, containing at least the properties
    and links that are required, in the body.
    The required fields of a WorkPackage can be found in its schema, which is embedded in the respective
    form.
    Note that it is only allowed to provide properties or links supporting the write operation.

    A project link must be set when creating work packages through this route.

    When setting start date, finish date, and duration together, their correctness will be checked and a
    422 error will be returned if one value does not match with the two others. You can make the server
    compute a value: set only two values in the request and the third one will be computed and returned
    in the response. For instance, when sending `{ \"startDate\": \"2022-08-23\", duration: \"P2D\" }`,
    the response will include `{ \"dueDate\": \"2022-08-24\" }`.

    Args:
        notify (Union[Unset, None, bool]):  Default: True.
        json_body (WorkPackageModel):  Example: {'_type': 'WorkPackage', '_links': {'self':
            {'href': '/api/v3/work_packages/1528', 'title': 'Develop API'}, 'schema': {'href':
            '/api/v3/work_packages/schemas/11-2'}, 'update': {'href': '/api/v3/work_packages/1528',
            'method': 'patch', 'title': 'Update Develop API'}, 'delete': {'href':
            '/work_packages/bulk?ids=1528', 'method': 'delete', 'title': 'Delete Develop API'},
            'logTime': {'href': '/work_packages/1528/time_entries/new', 'type': 'text/html', 'title':
            'Log time on Develop API'}, 'move': {'href': '/work_packages/1528/move/new', 'type':
            'text/html', 'title': 'Move Develop API'}, 'attachments': {'href':
            '/api/v3/work_packages/1528/attachments'}, 'addAttachment': {'href':
            '/api/v3/work_packages/1528/attachments', 'method': 'post'}, 'author': {'href':
            '/api/v3/users/1', 'title': 'OpenProject Admin - admin'}, 'customActions': [{'href':
            '/api/v3/work_packages/1528/custom_actions/153/execute', 'method': 'post', 'title':
            'Reset'}, {'href': '/api/v3/work_packages/1528/custom_actions/94/execute', 'method':
            'post', 'title': 'Forward to accounting'}], 'responsible': {'href': '/api/v3/users/23',
            'title': 'Laron Leuschke - Alaina5788'}, 'relations': {'href':
            '/api/v3/work_packages/1528/relations', 'title': 'Show relations'}, 'revisions': {'href':
            '/api/v3/work_packages/1528/revisions'}, 'assignee': {'href': '/api/v3/users/11', 'title':
            'Emmie Okuneva - Adele5450'}, 'priority': {'href': '/api/v3/priorities/2', 'title':
            'Normal'}, 'project': {'href': '/api/v3/projects/1', 'title': 'A Test Project'}, 'status':
            {'href': '/api/v3/statuses/1', 'title': 'New'}, 'type': {'href': '/api/v3/types/1',
            'title': 'A Type'}, 'version': {'href': '/api/v3/versions/1', 'title': 'Version 1'},
            'availableWatchers': {'href': '/api/v3/work_packages/1528/available_watchers'}, 'watch':
            {'href': '/api/v3/work_packages/1528/watchers', 'method': 'post', 'payload': {'user':
            {'href': '/api/v3/users/1'}}}, 'addWatcher': {'href':
            '/api/v3/work_packages/1528/watchers', 'method': 'post', 'payload': {'user': {'href':
            '/api/v3/users/{user_id}'}}, 'templated': True}, 'removeWatcher': {'href':
            '/api/v3/work_packages/1528/watchers/{user_id}', 'method': 'delete', 'templated': True},
            'addRelation': {'href': '/api/v3/relations', 'method': 'post', 'title': 'Add relation'},
            'changeParent': {'href': '/api/v3/work_packages/694', 'method': 'patch', 'title': 'Change
            parent of Bug in OpenProject'}, 'addComment': {'href':
            '/api/v3/work_packages/1528/activities', 'method': 'post', 'title': 'Add comment'},
            'parent': {'href': '/api/v3/work_packages/1298', 'title': 'nisi eligendi officiis eos
            delectus quis voluptas dolores'}, 'category': {'href': '/api/v3/categories/1298', 'title':
            'eligend isi'}, 'children': [{'href': '/api/v3/work_packages/1529', 'title': 'Write API
            documentation'}], 'ancestors': [{'href': '/api/v3/work_packages/1290', 'title': 'Root node
            of hierarchy'}, {'href': '/api/v3/work_packages/1291', 'title': 'Intermediate node of
            hierarchy'}, {'href': '/api/v3/work_packages/1298', 'title': 'nisi eligendi officiis eos
            delectus quis voluptas dolores'}], 'timeEntries': {'href':
            '/work_packages/1528/time_entries', 'type': 'text/html', 'title': 'Time entries'},
            'watchers': {'href': '/api/v3/work_packages/1528/watchers'}, 'customField3': {'href':
            'api/v3/users/14'}}, 'id': 1528, 'subject': 'Develop API', 'description': {'format':
            'markdown', 'raw': 'Develop super cool OpenProject API.', 'html': '<p>Develop super cool
            OpenProject API.</p>'}, 'scheduleManually': False, 'readonly': False, 'startDate': None,
            'dueDate': None, 'derivedStartDate': None, 'derivedDueDate': None, 'estimatedTime':
            'PT2H', 'derivedEstimatedTime': 'PT10H', 'percentageDone': 0, 'customField1': 'Foo',
            'customField2': 42, 'createdAt': '2014-08-29T12:40:53Z', 'updatedAt':
            '2014-08-29T12:44:41Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackageModel]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        notify=notify,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: WorkPackageModel,
    notify: Union[Unset, None, bool] = True,
) -> Response[Union[Any, ErrorResponse, WorkPackageModel]]:
    """Create Work Package

     When calling this endpoint the client provides a single object, containing at least the properties
    and links that are required, in the body.
    The required fields of a WorkPackage can be found in its schema, which is embedded in the respective
    form.
    Note that it is only allowed to provide properties or links supporting the write operation.

    A project link must be set when creating work packages through this route.

    When setting start date, finish date, and duration together, their correctness will be checked and a
    422 error will be returned if one value does not match with the two others. You can make the server
    compute a value: set only two values in the request and the third one will be computed and returned
    in the response. For instance, when sending `{ \"startDate\": \"2022-08-23\", duration: \"P2D\" }`,
    the response will include `{ \"dueDate\": \"2022-08-24\" }`.

    Args:
        notify (Union[Unset, None, bool]):  Default: True.
        json_body (WorkPackageModel):  Example: {'_type': 'WorkPackage', '_links': {'self':
            {'href': '/api/v3/work_packages/1528', 'title': 'Develop API'}, 'schema': {'href':
            '/api/v3/work_packages/schemas/11-2'}, 'update': {'href': '/api/v3/work_packages/1528',
            'method': 'patch', 'title': 'Update Develop API'}, 'delete': {'href':
            '/work_packages/bulk?ids=1528', 'method': 'delete', 'title': 'Delete Develop API'},
            'logTime': {'href': '/work_packages/1528/time_entries/new', 'type': 'text/html', 'title':
            'Log time on Develop API'}, 'move': {'href': '/work_packages/1528/move/new', 'type':
            'text/html', 'title': 'Move Develop API'}, 'attachments': {'href':
            '/api/v3/work_packages/1528/attachments'}, 'addAttachment': {'href':
            '/api/v3/work_packages/1528/attachments', 'method': 'post'}, 'author': {'href':
            '/api/v3/users/1', 'title': 'OpenProject Admin - admin'}, 'customActions': [{'href':
            '/api/v3/work_packages/1528/custom_actions/153/execute', 'method': 'post', 'title':
            'Reset'}, {'href': '/api/v3/work_packages/1528/custom_actions/94/execute', 'method':
            'post', 'title': 'Forward to accounting'}], 'responsible': {'href': '/api/v3/users/23',
            'title': 'Laron Leuschke - Alaina5788'}, 'relations': {'href':
            '/api/v3/work_packages/1528/relations', 'title': 'Show relations'}, 'revisions': {'href':
            '/api/v3/work_packages/1528/revisions'}, 'assignee': {'href': '/api/v3/users/11', 'title':
            'Emmie Okuneva - Adele5450'}, 'priority': {'href': '/api/v3/priorities/2', 'title':
            'Normal'}, 'project': {'href': '/api/v3/projects/1', 'title': 'A Test Project'}, 'status':
            {'href': '/api/v3/statuses/1', 'title': 'New'}, 'type': {'href': '/api/v3/types/1',
            'title': 'A Type'}, 'version': {'href': '/api/v3/versions/1', 'title': 'Version 1'},
            'availableWatchers': {'href': '/api/v3/work_packages/1528/available_watchers'}, 'watch':
            {'href': '/api/v3/work_packages/1528/watchers', 'method': 'post', 'payload': {'user':
            {'href': '/api/v3/users/1'}}}, 'addWatcher': {'href':
            '/api/v3/work_packages/1528/watchers', 'method': 'post', 'payload': {'user': {'href':
            '/api/v3/users/{user_id}'}}, 'templated': True}, 'removeWatcher': {'href':
            '/api/v3/work_packages/1528/watchers/{user_id}', 'method': 'delete', 'templated': True},
            'addRelation': {'href': '/api/v3/relations', 'method': 'post', 'title': 'Add relation'},
            'changeParent': {'href': '/api/v3/work_packages/694', 'method': 'patch', 'title': 'Change
            parent of Bug in OpenProject'}, 'addComment': {'href':
            '/api/v3/work_packages/1528/activities', 'method': 'post', 'title': 'Add comment'},
            'parent': {'href': '/api/v3/work_packages/1298', 'title': 'nisi eligendi officiis eos
            delectus quis voluptas dolores'}, 'category': {'href': '/api/v3/categories/1298', 'title':
            'eligend isi'}, 'children': [{'href': '/api/v3/work_packages/1529', 'title': 'Write API
            documentation'}], 'ancestors': [{'href': '/api/v3/work_packages/1290', 'title': 'Root node
            of hierarchy'}, {'href': '/api/v3/work_packages/1291', 'title': 'Intermediate node of
            hierarchy'}, {'href': '/api/v3/work_packages/1298', 'title': 'nisi eligendi officiis eos
            delectus quis voluptas dolores'}], 'timeEntries': {'href':
            '/work_packages/1528/time_entries', 'type': 'text/html', 'title': 'Time entries'},
            'watchers': {'href': '/api/v3/work_packages/1528/watchers'}, 'customField3': {'href':
            'api/v3/users/14'}}, 'id': 1528, 'subject': 'Develop API', 'description': {'format':
            'markdown', 'raw': 'Develop super cool OpenProject API.', 'html': '<p>Develop super cool
            OpenProject API.</p>'}, 'scheduleManually': False, 'readonly': False, 'startDate': None,
            'dueDate': None, 'derivedStartDate': None, 'derivedDueDate': None, 'estimatedTime':
            'PT2H', 'derivedEstimatedTime': 'PT10H', 'percentageDone': 0, 'customField1': 'Foo',
            'customField2': 42, 'createdAt': '2014-08-29T12:40:53Z', 'updatedAt':
            '2014-08-29T12:44:41Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackageModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        notify=notify,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: WorkPackageModel,
    notify: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, ErrorResponse, WorkPackageModel]]:
    """Create Work Package

     When calling this endpoint the client provides a single object, containing at least the properties
    and links that are required, in the body.
    The required fields of a WorkPackage can be found in its schema, which is embedded in the respective
    form.
    Note that it is only allowed to provide properties or links supporting the write operation.

    A project link must be set when creating work packages through this route.

    When setting start date, finish date, and duration together, their correctness will be checked and a
    422 error will be returned if one value does not match with the two others. You can make the server
    compute a value: set only two values in the request and the third one will be computed and returned
    in the response. For instance, when sending `{ \"startDate\": \"2022-08-23\", duration: \"P2D\" }`,
    the response will include `{ \"dueDate\": \"2022-08-24\" }`.

    Args:
        notify (Union[Unset, None, bool]):  Default: True.
        json_body (WorkPackageModel):  Example: {'_type': 'WorkPackage', '_links': {'self':
            {'href': '/api/v3/work_packages/1528', 'title': 'Develop API'}, 'schema': {'href':
            '/api/v3/work_packages/schemas/11-2'}, 'update': {'href': '/api/v3/work_packages/1528',
            'method': 'patch', 'title': 'Update Develop API'}, 'delete': {'href':
            '/work_packages/bulk?ids=1528', 'method': 'delete', 'title': 'Delete Develop API'},
            'logTime': {'href': '/work_packages/1528/time_entries/new', 'type': 'text/html', 'title':
            'Log time on Develop API'}, 'move': {'href': '/work_packages/1528/move/new', 'type':
            'text/html', 'title': 'Move Develop API'}, 'attachments': {'href':
            '/api/v3/work_packages/1528/attachments'}, 'addAttachment': {'href':
            '/api/v3/work_packages/1528/attachments', 'method': 'post'}, 'author': {'href':
            '/api/v3/users/1', 'title': 'OpenProject Admin - admin'}, 'customActions': [{'href':
            '/api/v3/work_packages/1528/custom_actions/153/execute', 'method': 'post', 'title':
            'Reset'}, {'href': '/api/v3/work_packages/1528/custom_actions/94/execute', 'method':
            'post', 'title': 'Forward to accounting'}], 'responsible': {'href': '/api/v3/users/23',
            'title': 'Laron Leuschke - Alaina5788'}, 'relations': {'href':
            '/api/v3/work_packages/1528/relations', 'title': 'Show relations'}, 'revisions': {'href':
            '/api/v3/work_packages/1528/revisions'}, 'assignee': {'href': '/api/v3/users/11', 'title':
            'Emmie Okuneva - Adele5450'}, 'priority': {'href': '/api/v3/priorities/2', 'title':
            'Normal'}, 'project': {'href': '/api/v3/projects/1', 'title': 'A Test Project'}, 'status':
            {'href': '/api/v3/statuses/1', 'title': 'New'}, 'type': {'href': '/api/v3/types/1',
            'title': 'A Type'}, 'version': {'href': '/api/v3/versions/1', 'title': 'Version 1'},
            'availableWatchers': {'href': '/api/v3/work_packages/1528/available_watchers'}, 'watch':
            {'href': '/api/v3/work_packages/1528/watchers', 'method': 'post', 'payload': {'user':
            {'href': '/api/v3/users/1'}}}, 'addWatcher': {'href':
            '/api/v3/work_packages/1528/watchers', 'method': 'post', 'payload': {'user': {'href':
            '/api/v3/users/{user_id}'}}, 'templated': True}, 'removeWatcher': {'href':
            '/api/v3/work_packages/1528/watchers/{user_id}', 'method': 'delete', 'templated': True},
            'addRelation': {'href': '/api/v3/relations', 'method': 'post', 'title': 'Add relation'},
            'changeParent': {'href': '/api/v3/work_packages/694', 'method': 'patch', 'title': 'Change
            parent of Bug in OpenProject'}, 'addComment': {'href':
            '/api/v3/work_packages/1528/activities', 'method': 'post', 'title': 'Add comment'},
            'parent': {'href': '/api/v3/work_packages/1298', 'title': 'nisi eligendi officiis eos
            delectus quis voluptas dolores'}, 'category': {'href': '/api/v3/categories/1298', 'title':
            'eligend isi'}, 'children': [{'href': '/api/v3/work_packages/1529', 'title': 'Write API
            documentation'}], 'ancestors': [{'href': '/api/v3/work_packages/1290', 'title': 'Root node
            of hierarchy'}, {'href': '/api/v3/work_packages/1291', 'title': 'Intermediate node of
            hierarchy'}, {'href': '/api/v3/work_packages/1298', 'title': 'nisi eligendi officiis eos
            delectus quis voluptas dolores'}], 'timeEntries': {'href':
            '/work_packages/1528/time_entries', 'type': 'text/html', 'title': 'Time entries'},
            'watchers': {'href': '/api/v3/work_packages/1528/watchers'}, 'customField3': {'href':
            'api/v3/users/14'}}, 'id': 1528, 'subject': 'Develop API', 'description': {'format':
            'markdown', 'raw': 'Develop super cool OpenProject API.', 'html': '<p>Develop super cool
            OpenProject API.</p>'}, 'scheduleManually': False, 'readonly': False, 'startDate': None,
            'dueDate': None, 'derivedStartDate': None, 'derivedDueDate': None, 'estimatedTime':
            'PT2H', 'derivedEstimatedTime': 'PT10H', 'percentageDone': 0, 'customField1': 'Foo',
            'customField2': 42, 'createdAt': '2014-08-29T12:40:53Z', 'updatedAt':
            '2014-08-29T12:44:41Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackageModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            notify=notify,
        )
    ).parsed
