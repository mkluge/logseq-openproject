from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.file_collection_model import FileCollectionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    parent: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v3/storages/{id}/files".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["parent"] = parent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorResponse, FileCollectionModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FileCollectionModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorResponse, FileCollectionModel]]:
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
    parent: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, FileCollectionModel]]:
    """Gets files of a storage.

     Gets a collection of files from a storage.

    If no `parent` context is given, the result is the content of the document root. With `parent`
    context given, the
    result contains the collections of files/directories from within the given parent file id.

    If given `parent` context is no directory, `400 Bad Request` is returned.

    Args:
        id (int):
        parent (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FileCollectionModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        parent=parent,
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
    parent: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, FileCollectionModel]]:
    """Gets files of a storage.

     Gets a collection of files from a storage.

    If no `parent` context is given, the result is the content of the document root. With `parent`
    context given, the
    result contains the collections of files/directories from within the given parent file id.

    If given `parent` context is no directory, `400 Bad Request` is returned.

    Args:
        id (int):
        parent (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FileCollectionModel]]
    """

    return sync_detailed(
        id=id,
        client=client,
        parent=parent,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    parent: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, FileCollectionModel]]:
    """Gets files of a storage.

     Gets a collection of files from a storage.

    If no `parent` context is given, the result is the content of the document root. With `parent`
    context given, the
    result contains the collections of files/directories from within the given parent file id.

    If given `parent` context is no directory, `400 Bad Request` is returned.

    Args:
        id (int):
        parent (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FileCollectionModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        parent=parent,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    parent: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, FileCollectionModel]]:
    """Gets files of a storage.

     Gets a collection of files from a storage.

    If no `parent` context is given, the result is the content of the document root. With `parent`
    context given, the
    result contains the collections of files/directories from within the given parent file id.

    If given `parent` context is no directory, `400 Bad Request` is returned.

    Args:
        id (int):
        parent (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FileCollectionModel]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            parent=parent,
        )
    ).parsed
