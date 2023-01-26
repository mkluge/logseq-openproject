from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.file_link_collection_read_model import FileLinkCollectionReadModel
from ...models.file_link_collection_write_model import FileLinkCollectionWriteModel
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: Client,
    json_body: FileLinkCollectionWriteModel,
) -> Dict[str, Any]:
    url = "{}/api/v3/work_packages/{id}/file_links".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, FileLinkCollectionReadModel]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = FileLinkCollectionReadModel.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, ErrorResponse, FileLinkCollectionReadModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Client,
    json_body: FileLinkCollectionWriteModel,
) -> Response[Union[Any, ErrorResponse, FileLinkCollectionReadModel]]:
    """Creates file links.

     Creates file links on a work package.

    The request is interpreted as a bulk insert, where every element of the collection is validated
    separately. Each
    element contains the origin meta data and a link to the storage, the file link is about to point to.
    The storage
    link can be provided as a resource link with id or as the host url.

    The file's id and name are considered mandatory information. The rest of the origin meta data SHOULD
    be provided
    by the client. The _mimeType_ SHOULD be a standard mime type. An empty mime type will be handled as
    unknown. To link
    a folder, the custom mime type `application/x-op-directory` MUST be used.

    Up to 20 file links can be submitted at once.

    If any element data is invalid, no file links will be created.

    If a file link with matching origin id, work package, and storage already exists, then it will not
    create an
    additional file link or update the meta data. Instead the information from the existing file link
    will be returned.

    Args:
        id (int):
        json_body (FileLinkCollectionWriteModel):  Example: {'_embedded': {'elements':
            [{'originData': {'id': 5503, 'name': 'logo.png', 'mimeType': 'image/png', 'size': 16042,
            'createdAt': '2021-12-19T09:42:10.170Z', 'lastModifiedAt': '2021-12-20T14:00:13.987Z',
            'createdByName': 'Luke Skywalker', 'lastModifiedByName': 'Anakin Skywalker'}, '_links':
            {'storage': {'href': '/api/v3/storage/42'}}}, {'_hint': 'File Link resource shortened for
            brevity', 'id': 1338}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, FileLinkCollectionReadModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Client,
    json_body: FileLinkCollectionWriteModel,
) -> Optional[Union[Any, ErrorResponse, FileLinkCollectionReadModel]]:
    """Creates file links.

     Creates file links on a work package.

    The request is interpreted as a bulk insert, where every element of the collection is validated
    separately. Each
    element contains the origin meta data and a link to the storage, the file link is about to point to.
    The storage
    link can be provided as a resource link with id or as the host url.

    The file's id and name are considered mandatory information. The rest of the origin meta data SHOULD
    be provided
    by the client. The _mimeType_ SHOULD be a standard mime type. An empty mime type will be handled as
    unknown. To link
    a folder, the custom mime type `application/x-op-directory` MUST be used.

    Up to 20 file links can be submitted at once.

    If any element data is invalid, no file links will be created.

    If a file link with matching origin id, work package, and storage already exists, then it will not
    create an
    additional file link or update the meta data. Instead the information from the existing file link
    will be returned.

    Args:
        id (int):
        json_body (FileLinkCollectionWriteModel):  Example: {'_embedded': {'elements':
            [{'originData': {'id': 5503, 'name': 'logo.png', 'mimeType': 'image/png', 'size': 16042,
            'createdAt': '2021-12-19T09:42:10.170Z', 'lastModifiedAt': '2021-12-20T14:00:13.987Z',
            'createdByName': 'Luke Skywalker', 'lastModifiedByName': 'Anakin Skywalker'}, '_links':
            {'storage': {'href': '/api/v3/storage/42'}}}, {'_hint': 'File Link resource shortened for
            brevity', 'id': 1338}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, FileLinkCollectionReadModel]]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    json_body: FileLinkCollectionWriteModel,
) -> Response[Union[Any, ErrorResponse, FileLinkCollectionReadModel]]:
    """Creates file links.

     Creates file links on a work package.

    The request is interpreted as a bulk insert, where every element of the collection is validated
    separately. Each
    element contains the origin meta data and a link to the storage, the file link is about to point to.
    The storage
    link can be provided as a resource link with id or as the host url.

    The file's id and name are considered mandatory information. The rest of the origin meta data SHOULD
    be provided
    by the client. The _mimeType_ SHOULD be a standard mime type. An empty mime type will be handled as
    unknown. To link
    a folder, the custom mime type `application/x-op-directory` MUST be used.

    Up to 20 file links can be submitted at once.

    If any element data is invalid, no file links will be created.

    If a file link with matching origin id, work package, and storage already exists, then it will not
    create an
    additional file link or update the meta data. Instead the information from the existing file link
    will be returned.

    Args:
        id (int):
        json_body (FileLinkCollectionWriteModel):  Example: {'_embedded': {'elements':
            [{'originData': {'id': 5503, 'name': 'logo.png', 'mimeType': 'image/png', 'size': 16042,
            'createdAt': '2021-12-19T09:42:10.170Z', 'lastModifiedAt': '2021-12-20T14:00:13.987Z',
            'createdByName': 'Luke Skywalker', 'lastModifiedByName': 'Anakin Skywalker'}, '_links':
            {'storage': {'href': '/api/v3/storage/42'}}}, {'_hint': 'File Link resource shortened for
            brevity', 'id': 1338}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, FileLinkCollectionReadModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    json_body: FileLinkCollectionWriteModel,
) -> Optional[Union[Any, ErrorResponse, FileLinkCollectionReadModel]]:
    """Creates file links.

     Creates file links on a work package.

    The request is interpreted as a bulk insert, where every element of the collection is validated
    separately. Each
    element contains the origin meta data and a link to the storage, the file link is about to point to.
    The storage
    link can be provided as a resource link with id or as the host url.

    The file's id and name are considered mandatory information. The rest of the origin meta data SHOULD
    be provided
    by the client. The _mimeType_ SHOULD be a standard mime type. An empty mime type will be handled as
    unknown. To link
    a folder, the custom mime type `application/x-op-directory` MUST be used.

    Up to 20 file links can be submitted at once.

    If any element data is invalid, no file links will be created.

    If a file link with matching origin id, work package, and storage already exists, then it will not
    create an
    additional file link or update the meta data. Instead the information from the existing file link
    will be returned.

    Args:
        id (int):
        json_body (FileLinkCollectionWriteModel):  Example: {'_embedded': {'elements':
            [{'originData': {'id': 5503, 'name': 'logo.png', 'mimeType': 'image/png', 'size': 16042,
            'createdAt': '2021-12-19T09:42:10.170Z', 'lastModifiedAt': '2021-12-20T14:00:13.987Z',
            'createdByName': 'Luke Skywalker', 'lastModifiedByName': 'Anakin Skywalker'}, '_links':
            {'storage': {'href': '/api/v3/storage/42'}}}, {'_hint': 'File Link resource shortened for
            brevity', 'id': 1338}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, FileLinkCollectionReadModel]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
