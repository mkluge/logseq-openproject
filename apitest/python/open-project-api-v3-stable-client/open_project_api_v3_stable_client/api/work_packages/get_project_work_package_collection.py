from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.work_packages_model import WorkPackagesModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    select: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v3/projects/{id}/work_packages".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["offset"] = offset

    params["pageSize"] = page_size

    params["filters"] = filters

    params["sortBy"] = sort_by

    params["groupBy"] = group_by

    params["showSums"] = show_sums

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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, WorkPackagesModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WorkPackagesModel.from_dict(response.json())

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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ErrorResponse, WorkPackagesModel]]:
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
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    select: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, WorkPackagesModel]]:
    """Get work packages of project

     Returns the collection of work packages that are related to the given project.

    Args:
        id (int):
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        filters (Union[Unset, None, str]):  Default: '[{ \\"status_id\\": { \\"operator\\":
            \\"o\\", \\"values\\": null }}]'.
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        group_by (Union[Unset, None, str]):
        show_sums (Union[Unset, None, bool]):
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackagesModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        offset=offset,
        page_size=page_size,
        filters=filters,
        sort_by=sort_by,
        group_by=group_by,
        show_sums=show_sums,
        select=select,
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
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    select: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, WorkPackagesModel]]:
    """Get work packages of project

     Returns the collection of work packages that are related to the given project.

    Args:
        id (int):
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        filters (Union[Unset, None, str]):  Default: '[{ \\"status_id\\": { \\"operator\\":
            \\"o\\", \\"values\\": null }}]'.
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        group_by (Union[Unset, None, str]):
        show_sums (Union[Unset, None, bool]):
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackagesModel]]
    """

    return sync_detailed(
        id=id,
        client=client,
        offset=offset,
        page_size=page_size,
        filters=filters,
        sort_by=sort_by,
        group_by=group_by,
        show_sums=show_sums,
        select=select,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    select: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, WorkPackagesModel]]:
    """Get work packages of project

     Returns the collection of work packages that are related to the given project.

    Args:
        id (int):
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        filters (Union[Unset, None, str]):  Default: '[{ \\"status_id\\": { \\"operator\\":
            \\"o\\", \\"values\\": null }}]'.
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        group_by (Union[Unset, None, str]):
        show_sums (Union[Unset, None, bool]):
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackagesModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        offset=offset,
        page_size=page_size,
        filters=filters,
        sort_by=sort_by,
        group_by=group_by,
        show_sums=show_sums,
        select=select,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    select: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, WorkPackagesModel]]:
    """Get work packages of project

     Returns the collection of work packages that are related to the given project.

    Args:
        id (int):
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        filters (Union[Unset, None, str]):  Default: '[{ \\"status_id\\": { \\"operator\\":
            \\"o\\", \\"values\\": null }}]'.
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        group_by (Union[Unset, None, str]):
        show_sums (Union[Unset, None, bool]):
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackagesModel]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            offset=offset,
            page_size=page_size,
            filters=filters,
            sort_by=sort_by,
            group_by=group_by,
            show_sums=show_sums,
            select=select,
        )
    ).parsed
