from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.available_relation_candidates_model import AvailableRelationCandidatesModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    page_size: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
) -> Dict[str, Any]:
    url = "{}/api/v3/work_packages/{id}/available_relation_candidates".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["pageSize"] = page_size

    params["filters"] = filters

    params["query"] = query

    params["type"] = type

    params["sortBy"] = sort_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[AvailableRelationCandidatesModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AvailableRelationCandidatesModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[AvailableRelationCandidatesModel]:
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
    page_size: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
) -> Response[AvailableRelationCandidatesModel]:
    """Available relation candidates

    Args:
        id (int):
        page_size (Union[Unset, None, int]):
        filters (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableRelationCandidatesModel]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        page_size=page_size,
        filters=filters,
        query=query,
        type=type,
        sort_by=sort_by,
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
    page_size: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
) -> Optional[AvailableRelationCandidatesModel]:
    """Available relation candidates

    Args:
        id (int):
        page_size (Union[Unset, None, int]):
        filters (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableRelationCandidatesModel]
    """

    return sync_detailed(
        id=id,
        client=client,
        page_size=page_size,
        filters=filters,
        query=query,
        type=type,
        sort_by=sort_by,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    page_size: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
) -> Response[AvailableRelationCandidatesModel]:
    """Available relation candidates

    Args:
        id (int):
        page_size (Union[Unset, None, int]):
        filters (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableRelationCandidatesModel]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        page_size=page_size,
        filters=filters,
        query=query,
        type=type,
        sort_by=sort_by,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    page_size: Union[Unset, None, int] = UNSET,
    filters: Union[Unset, None, str] = UNSET,
    query: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = '[[\\"id\\", \\"asc\\"]]',
) -> Optional[AvailableRelationCandidatesModel]:
    """Available relation candidates

    Args:
        id (int):
        page_size (Union[Unset, None, int]):
        filters (Union[Unset, None, str]):
        query (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):  Default: '[[\\"id\\", \\"asc\\"]]'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableRelationCandidatesModel]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            page_size=page_size,
            filters=filters,
            query=query,
            type=type,
            sort_by=sort_by,
        )
    ).parsed
