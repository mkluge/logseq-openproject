from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.list_of_news_model import ListOfNewsModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    filters: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v3/news".format(client.base_url)

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
) -> Optional[Union[Any, ErrorResponse, ListOfNewsModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListOfNewsModel.from_dict(response.json())

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
) -> Response[Union[Any, ErrorResponse, ListOfNewsModel]]:
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
    sort_by: Union[Unset, None, str] = UNSET,
    filters: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListOfNewsModel]]:
    """List News

     Lists news. The news returned depend on the provided parameters and also on the requesting user's
    permissions.

    Args:
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListOfNewsModel]]
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
    sort_by: Union[Unset, None, str] = UNSET,
    filters: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListOfNewsModel]]:
    """List News

     Lists news. The news returned depend on the provided parameters and also on the requesting user's
    permissions.

    Args:
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListOfNewsModel]]
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
    sort_by: Union[Unset, None, str] = UNSET,
    filters: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListOfNewsModel]]:
    """List News

     Lists news. The news returned depend on the provided parameters and also on the requesting user's
    permissions.

    Args:
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListOfNewsModel]]
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
    sort_by: Union[Unset, None, str] = UNSET,
    filters: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListOfNewsModel]]:
    """List News

     Lists news. The news returned depend on the provided parameters and also on the requesting user's
    permissions.

    Args:
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ListOfNewsModel]]
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
