from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.default_query_model import DefaultQueryModel
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    timeline_visible: Union[Unset, None, bool] = False,
    timeline_zoom_level: Union[Unset, None, str] = "days",
    show_hierarchies: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/api/v3/queries/default".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["filters"] = filters

    params["offset"] = offset

    params["pageSize"] = page_size

    params["sortBy"] = sort_by

    params["groupBy"] = group_by

    params["showSums"] = show_sums

    params["timelineVisible"] = timeline_visible

    params["timelineZoomLevel"] = timeline_zoom_level

    params["showHierarchies"] = show_hierarchies

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[DefaultQueryModel, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DefaultQueryModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[DefaultQueryModel, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    timeline_visible: Union[Unset, None, bool] = False,
    timeline_zoom_level: Union[Unset, None, str] = "days",
    show_hierarchies: Union[Unset, None, bool] = True,
) -> Response[Union[DefaultQueryModel, ErrorResponse]]:
    """View default query

     Same as [viewing an existing, persisted
    Query](https://www.openproject.org/docs/api/endpoints/queries/#list-queries) in its response, this
    resource returns an unpersisted query and by that allows to get the default query configuration. The
    client may also provide additional parameters which will modify the default query.

    Args:
        filters (Union[Unset, None, str]):  Default: '[{ \\"status_id\\": { \\"operator\\":
            \\"o\\", \\"values\\": null }}]'.
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        group_by (Union[Unset, None, str]):
        show_sums (Union[Unset, None, bool]):
        timeline_visible (Union[Unset, None, bool]):
        timeline_zoom_level (Union[Unset, None, str]):  Default: 'days'.
        show_hierarchies (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultQueryModel, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        filters=filters,
        offset=offset,
        page_size=page_size,
        sort_by=sort_by,
        group_by=group_by,
        show_sums=show_sums,
        timeline_visible=timeline_visible,
        timeline_zoom_level=timeline_zoom_level,
        show_hierarchies=show_hierarchies,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    timeline_visible: Union[Unset, None, bool] = False,
    timeline_zoom_level: Union[Unset, None, str] = "days",
    show_hierarchies: Union[Unset, None, bool] = True,
) -> Optional[Union[DefaultQueryModel, ErrorResponse]]:
    """View default query

     Same as [viewing an existing, persisted
    Query](https://www.openproject.org/docs/api/endpoints/queries/#list-queries) in its response, this
    resource returns an unpersisted query and by that allows to get the default query configuration. The
    client may also provide additional parameters which will modify the default query.

    Args:
        filters (Union[Unset, None, str]):  Default: '[{ \\"status_id\\": { \\"operator\\":
            \\"o\\", \\"values\\": null }}]'.
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        group_by (Union[Unset, None, str]):
        show_sums (Union[Unset, None, bool]):
        timeline_visible (Union[Unset, None, bool]):
        timeline_zoom_level (Union[Unset, None, str]):  Default: 'days'.
        show_hierarchies (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultQueryModel, ErrorResponse]]
    """

    return sync_detailed(
        client=client,
        filters=filters,
        offset=offset,
        page_size=page_size,
        sort_by=sort_by,
        group_by=group_by,
        show_sums=show_sums,
        timeline_visible=timeline_visible,
        timeline_zoom_level=timeline_zoom_level,
        show_hierarchies=show_hierarchies,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    timeline_visible: Union[Unset, None, bool] = False,
    timeline_zoom_level: Union[Unset, None, str] = "days",
    show_hierarchies: Union[Unset, None, bool] = True,
) -> Response[Union[DefaultQueryModel, ErrorResponse]]:
    """View default query

     Same as [viewing an existing, persisted
    Query](https://www.openproject.org/docs/api/endpoints/queries/#list-queries) in its response, this
    resource returns an unpersisted query and by that allows to get the default query configuration. The
    client may also provide additional parameters which will modify the default query.

    Args:
        filters (Union[Unset, None, str]):  Default: '[{ \\"status_id\\": { \\"operator\\":
            \\"o\\", \\"values\\": null }}]'.
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        group_by (Union[Unset, None, str]):
        show_sums (Union[Unset, None, bool]):
        timeline_visible (Union[Unset, None, bool]):
        timeline_zoom_level (Union[Unset, None, str]):  Default: 'days'.
        show_hierarchies (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultQueryModel, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        filters=filters,
        offset=offset,
        page_size=page_size,
        sort_by=sort_by,
        group_by=group_by,
        show_sums=show_sums,
        timeline_visible=timeline_visible,
        timeline_zoom_level=timeline_zoom_level,
        show_hierarchies=show_hierarchies,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    timeline_visible: Union[Unset, None, bool] = False,
    timeline_zoom_level: Union[Unset, None, str] = "days",
    show_hierarchies: Union[Unset, None, bool] = True,
) -> Optional[Union[DefaultQueryModel, ErrorResponse]]:
    """View default query

     Same as [viewing an existing, persisted
    Query](https://www.openproject.org/docs/api/endpoints/queries/#list-queries) in its response, this
    resource returns an unpersisted query and by that allows to get the default query configuration. The
    client may also provide additional parameters which will modify the default query.

    Args:
        filters (Union[Unset, None, str]):  Default: '[{ \\"status_id\\": { \\"operator\\":
            \\"o\\", \\"values\\": null }}]'.
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        group_by (Union[Unset, None, str]):
        show_sums (Union[Unset, None, bool]):
        timeline_visible (Union[Unset, None, bool]):
        timeline_zoom_level (Union[Unset, None, str]):  Default: 'days'.
        show_hierarchies (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DefaultQueryModel, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            filters=filters,
            offset=offset,
            page_size=page_size,
            sort_by=sort_by,
            group_by=group_by,
            show_sums=show_sums,
            timeline_visible=timeline_visible,
            timeline_zoom_level=timeline_zoom_level,
            show_hierarchies=show_hierarchies,
        )
    ).parsed
