from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.list_groups_model import ListGroupsModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    select: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v3/groups".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["sortBy"] = sort_by

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorResponse, ListGroupsModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListGroupsModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorResponse, ListGroupsModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    select: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, ListGroupsModel]]:
    """List groups

     Returns a collection of groups. The client can choose to filter the groups similar to how work
    packages are filtered. In addition to the provided filters, the server will reduce the result set to
    only contain groups, for which the requesting client has sufficient permissions (*view_members*,
    *manage_members*).

    Args:
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListGroupsModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        sort_by=sort_by,
        select=select,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    select: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, ListGroupsModel]]:
    """List groups

     Returns a collection of groups. The client can choose to filter the groups similar to how work
    packages are filtered. In addition to the provided filters, the server will reduce the result set to
    only contain groups, for which the requesting client has sufficient permissions (*view_members*,
    *manage_members*).

    Args:
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListGroupsModel]]
    """

    return sync_detailed(
        client=client,
        sort_by=sort_by,
        select=select,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    select: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, ListGroupsModel]]:
    """List groups

     Returns a collection of groups. The client can choose to filter the groups similar to how work
    packages are filtered. In addition to the provided filters, the server will reduce the result set to
    only contain groups, for which the requesting client has sufficient permissions (*view_members*,
    *manage_members*).

    Args:
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListGroupsModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        sort_by=sort_by,
        select=select,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    select: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, ListGroupsModel]]:
    """List groups

     Returns a collection of groups. The client can choose to filter the groups similar to how work
    packages are filtered. In addition to the provided filters, the server will reduce the result set to
    only contain groups, for which the requesting client has sufficient permissions (*view_members*,
    *manage_members*).

    Args:
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListGroupsModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            sort_by=sort_by,
            select=select,
        )
    ).parsed
