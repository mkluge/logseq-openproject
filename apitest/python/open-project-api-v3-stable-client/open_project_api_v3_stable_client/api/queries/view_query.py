from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.query_model import QueryModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    columns: Union[Unset, None, str] = "['type', 'priority']",
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    timeline_visible: Union[Unset, None, bool] = False,
    timeline_labels: Union[Unset, None, str] = "{}",
    highlighting_mode: Union[Unset, None, str] = "inline",
    highlighted_attributes: Union[Unset, None, str] = "['type', 'priority']",
    show_hierarchies: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/api/v3/queries/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["filters"] = filters

    params["offset"] = offset

    params["pageSize"] = page_size

    params["columns"] = columns

    params["sortBy"] = sort_by

    params["groupBy"] = group_by

    params["showSums"] = show_sums

    params["timelineVisible"] = timeline_visible

    params["timelineLabels"] = timeline_labels

    params["highlightingMode"] = highlighting_mode

    params["highlightedAttributes"] = highlighted_attributes

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorResponse, QueryModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QueryModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorResponse, QueryModel]]:
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
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    columns: Union[Unset, None, str] = "['type', 'priority']",
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    timeline_visible: Union[Unset, None, bool] = False,
    timeline_labels: Union[Unset, None, str] = "{}",
    highlighting_mode: Union[Unset, None, str] = "inline",
    highlighted_attributes: Union[Unset, None, str] = "['type', 'priority']",
    show_hierarchies: Union[Unset, None, bool] = True,
) -> Response[Union[ErrorResponse, QueryModel]]:
    """View query

     Retrieve an individual query as identified by the id parameter. Then end point accepts a number of
    parameters that can be used to override the resources' persisted parameters.

    Args:
        id (int):
        filters (Union[Unset, None, str]):  Default: '[{ \\"status_id\\": { \\"operator\\":
            \\"o\\", \\"values\\": null }}]'.
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        columns (Union[Unset, None, str]):  Default: "['type', 'priority']".
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        group_by (Union[Unset, None, str]):
        show_sums (Union[Unset, None, bool]):
        timeline_visible (Union[Unset, None, bool]):
        timeline_labels (Union[Unset, None, str]):  Default: '{}'.
        highlighting_mode (Union[Unset, None, str]):  Default: 'inline'.
        highlighted_attributes (Union[Unset, None, str]):  Default: "['type', 'priority']".
        show_hierarchies (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, QueryModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        filters=filters,
        offset=offset,
        page_size=page_size,
        columns=columns,
        sort_by=sort_by,
        group_by=group_by,
        show_sums=show_sums,
        timeline_visible=timeline_visible,
        timeline_labels=timeline_labels,
        highlighting_mode=highlighting_mode,
        highlighted_attributes=highlighted_attributes,
        show_hierarchies=show_hierarchies,
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
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    columns: Union[Unset, None, str] = "['type', 'priority']",
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    timeline_visible: Union[Unset, None, bool] = False,
    timeline_labels: Union[Unset, None, str] = "{}",
    highlighting_mode: Union[Unset, None, str] = "inline",
    highlighted_attributes: Union[Unset, None, str] = "['type', 'priority']",
    show_hierarchies: Union[Unset, None, bool] = True,
) -> Optional[Union[ErrorResponse, QueryModel]]:
    """View query

     Retrieve an individual query as identified by the id parameter. Then end point accepts a number of
    parameters that can be used to override the resources' persisted parameters.

    Args:
        id (int):
        filters (Union[Unset, None, str]):  Default: '[{ \\"status_id\\": { \\"operator\\":
            \\"o\\", \\"values\\": null }}]'.
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        columns (Union[Unset, None, str]):  Default: "['type', 'priority']".
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        group_by (Union[Unset, None, str]):
        show_sums (Union[Unset, None, bool]):
        timeline_visible (Union[Unset, None, bool]):
        timeline_labels (Union[Unset, None, str]):  Default: '{}'.
        highlighting_mode (Union[Unset, None, str]):  Default: 'inline'.
        highlighted_attributes (Union[Unset, None, str]):  Default: "['type', 'priority']".
        show_hierarchies (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, QueryModel]]
    """

    return sync_detailed(
        id=id,
        client=client,
        filters=filters,
        offset=offset,
        page_size=page_size,
        columns=columns,
        sort_by=sort_by,
        group_by=group_by,
        show_sums=show_sums,
        timeline_visible=timeline_visible,
        timeline_labels=timeline_labels,
        highlighting_mode=highlighting_mode,
        highlighted_attributes=highlighted_attributes,
        show_hierarchies=show_hierarchies,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    columns: Union[Unset, None, str] = "['type', 'priority']",
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    timeline_visible: Union[Unset, None, bool] = False,
    timeline_labels: Union[Unset, None, str] = "{}",
    highlighting_mode: Union[Unset, None, str] = "inline",
    highlighted_attributes: Union[Unset, None, str] = "['type', 'priority']",
    show_hierarchies: Union[Unset, None, bool] = True,
) -> Response[Union[ErrorResponse, QueryModel]]:
    """View query

     Retrieve an individual query as identified by the id parameter. Then end point accepts a number of
    parameters that can be used to override the resources' persisted parameters.

    Args:
        id (int):
        filters (Union[Unset, None, str]):  Default: '[{ \\"status_id\\": { \\"operator\\":
            \\"o\\", \\"values\\": null }}]'.
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        columns (Union[Unset, None, str]):  Default: "['type', 'priority']".
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        group_by (Union[Unset, None, str]):
        show_sums (Union[Unset, None, bool]):
        timeline_visible (Union[Unset, None, bool]):
        timeline_labels (Union[Unset, None, str]):  Default: '{}'.
        highlighting_mode (Union[Unset, None, str]):  Default: 'inline'.
        highlighted_attributes (Union[Unset, None, str]):  Default: "['type', 'priority']".
        show_hierarchies (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, QueryModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        filters=filters,
        offset=offset,
        page_size=page_size,
        columns=columns,
        sort_by=sort_by,
        group_by=group_by,
        show_sums=show_sums,
        timeline_visible=timeline_visible,
        timeline_labels=timeline_labels,
        highlighting_mode=highlighting_mode,
        highlighted_attributes=highlighted_attributes,
        show_hierarchies=show_hierarchies,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    filters: Union[Unset, None, str] = '[{ \\"status_id\\": { \\"operator\\": \\"o\\", \\"values\\": null }}]',
    offset: Union[Unset, None, int] = 1,
    page_size: Union[Unset, None, int] = UNSET,
    columns: Union[Unset, None, str] = "['type', 'priority']",
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
    group_by: Union[Unset, None, str] = UNSET,
    show_sums: Union[Unset, None, bool] = False,
    timeline_visible: Union[Unset, None, bool] = False,
    timeline_labels: Union[Unset, None, str] = "{}",
    highlighting_mode: Union[Unset, None, str] = "inline",
    highlighted_attributes: Union[Unset, None, str] = "['type', 'priority']",
    show_hierarchies: Union[Unset, None, bool] = True,
) -> Optional[Union[ErrorResponse, QueryModel]]:
    """View query

     Retrieve an individual query as identified by the id parameter. Then end point accepts a number of
    parameters that can be used to override the resources' persisted parameters.

    Args:
        id (int):
        filters (Union[Unset, None, str]):  Default: '[{ \\"status_id\\": { \\"operator\\":
            \\"o\\", \\"values\\": null }}]'.
        offset (Union[Unset, None, int]):  Default: 1.
        page_size (Union[Unset, None, int]):
        columns (Union[Unset, None, str]):  Default: "['type', 'priority']".
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.
        group_by (Union[Unset, None, str]):
        show_sums (Union[Unset, None, bool]):
        timeline_visible (Union[Unset, None, bool]):
        timeline_labels (Union[Unset, None, str]):  Default: '{}'.
        highlighting_mode (Union[Unset, None, str]):  Default: 'inline'.
        highlighted_attributes (Union[Unset, None, str]):  Default: "['type', 'priority']".
        show_hierarchies (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, QueryModel]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            filters=filters,
            offset=offset,
            page_size=page_size,
            columns=columns,
            sort_by=sort_by,
            group_by=group_by,
            show_sums=show_sums,
            timeline_visible=timeline_visible,
            timeline_labels=timeline_labels,
            highlighting_mode=highlighting_mode,
            highlighted_attributes=highlighted_attributes,
            show_hierarchies=show_hierarchies,
        )
    ).parsed
