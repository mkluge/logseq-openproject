from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.list_projects_model import ListProjectsModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    select: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v3/projects".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["filters"] = filters

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ListProjectsModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListProjectsModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ListProjectsModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    select: Union[Unset, None, str] = UNSET,
) -> Response[ListProjectsModel]:
    """List projects

     Returns a collection of projects. The collection can be filtered via query parameters similar to how
    work packages are filtered. In addition to the provided filter, the result set is always limited to
    only contain projects the client is allowed to see.

    Args:
        filters (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListProjectsModel]
    """

    kwargs = _get_kwargs(
        client=client,
        filters=filters,
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
    filters: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    select: Union[Unset, None, str] = UNSET,
) -> Optional[ListProjectsModel]:
    """List projects

     Returns a collection of projects. The collection can be filtered via query parameters similar to how
    work packages are filtered. In addition to the provided filter, the result set is always limited to
    only contain projects the client is allowed to see.

    Args:
        filters (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListProjectsModel]
    """

    return sync_detailed(
        client=client,
        filters=filters,
        sort_by=sort_by,
        select=select,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    select: Union[Unset, None, str] = UNSET,
) -> Response[ListProjectsModel]:
    """List projects

     Returns a collection of projects. The collection can be filtered via query parameters similar to how
    work packages are filtered. In addition to the provided filter, the result set is always limited to
    only contain projects the client is allowed to see.

    Args:
        filters (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListProjectsModel]
    """

    kwargs = _get_kwargs(
        client=client,
        filters=filters,
        sort_by=sort_by,
        select=select,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
    select: Union[Unset, None, str] = UNSET,
) -> Optional[ListProjectsModel]:
    """List projects

     Returns a collection of projects. The collection can be filtered via query parameters similar to how
    work packages are filtered. In addition to the provided filter, the result set is always limited to
    only contain projects the client is allowed to see.

    Args:
        filters (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListProjectsModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            filters=filters,
            sort_by=sort_by,
            select=select,
        )
    ).parsed
