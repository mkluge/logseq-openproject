from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.file_link_collection_read_model import FileLinkCollectionReadModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v3/work_packages/{id}/file_links".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["filters"] = filters

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ErrorResponse, FileLinkCollectionReadModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FileLinkCollectionReadModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ErrorResponse, FileLinkCollectionReadModel]]:
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
    filters: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, FileLinkCollectionReadModel]]:
    """Gets all file links of a work package

     Gets all file links of a work package.

    As a side effect, for every file link a request is sent to the storage's origin to fetch live data
    and patch
    the file link's data before returning, as well as retrieving permissions of the user on this origin
    file.

    Args:
        id (int):
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FileLinkCollectionReadModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        filters=filters,
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
    filters: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, FileLinkCollectionReadModel]]:
    """Gets all file links of a work package

     Gets all file links of a work package.

    As a side effect, for every file link a request is sent to the storage's origin to fetch live data
    and patch
    the file link's data before returning, as well as retrieving permissions of the user on this origin
    file.

    Args:
        id (int):
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FileLinkCollectionReadModel]]
    """

    return sync_detailed(
        id=id,
        client=client,
        filters=filters,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, FileLinkCollectionReadModel]]:
    """Gets all file links of a work package

     Gets all file links of a work package.

    As a side effect, for every file link a request is sent to the storage's origin to fetch live data
    and patch
    the file link's data before returning, as well as retrieving permissions of the user on this origin
    file.

    Args:
        id (int):
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FileLinkCollectionReadModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        filters=filters,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, FileLinkCollectionReadModel]]:
    """Gets all file links of a work package

     Gets all file links of a work package.

    As a side effect, for every file link a request is sent to the storage's origin to fetch live data
    and patch
    the file link's data before returning, as well as retrieving permissions of the user on this origin
    file.

    Args:
        id (int):
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, FileLinkCollectionReadModel]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            filters=filters,
        )
    ).parsed
