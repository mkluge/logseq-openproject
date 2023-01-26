from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.list_time_entries_model import ListTimeEntriesModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = '[\\"spent_on\\", \\"asc\\"]',
    filters: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v3/time_entries".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["offset"] = offset

    params["pageSize"] = page_size

    params["sortBy"] = sort_by

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
) -> Optional[Union[Any, ErrorResponse, ListTimeEntriesModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListTimeEntriesModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ErrorResponse, ListTimeEntriesModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = '[\\"spent_on\\", \\"asc\\"]',
    filters: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListTimeEntriesModel]]:
    """List time entries

     Lists time entries. The time entries returned depend on the filters provided and also on the
    permission of the requesting user.

    Args:
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):  Default: '[\\"spent_on\\", \\"asc\\"]'.
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListTimeEntriesModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        offset=offset,
        page_size=page_size,
        sort_by=sort_by,
        filters=filters,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = '[\\"spent_on\\", \\"asc\\"]',
    filters: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListTimeEntriesModel]]:
    """List time entries

     Lists time entries. The time entries returned depend on the filters provided and also on the
    permission of the requesting user.

    Args:
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):  Default: '[\\"spent_on\\", \\"asc\\"]'.
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListTimeEntriesModel]]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        page_size=page_size,
        sort_by=sort_by,
        filters=filters,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = '[\\"spent_on\\", \\"asc\\"]',
    filters: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListTimeEntriesModel]]:
    """List time entries

     Lists time entries. The time entries returned depend on the filters provided and also on the
    permission of the requesting user.

    Args:
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):  Default: '[\\"spent_on\\", \\"asc\\"]'.
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListTimeEntriesModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        offset=offset,
        page_size=page_size,
        sort_by=sort_by,
        filters=filters,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = '[\\"spent_on\\", \\"asc\\"]',
    filters: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListTimeEntriesModel]]:
    """List time entries

     Lists time entries. The time entries returned depend on the filters provided and also on the
    permission of the requesting user.

    Args:
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):  Default: '[\\"spent_on\\", \\"asc\\"]'.
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListTimeEntriesModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            page_size=page_size,
            sort_by=sort_by,
            filters=filters,
        )
    ).parsed
