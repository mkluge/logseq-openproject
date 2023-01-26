from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.queries_model import QueriesModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v3/queries".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorResponse, QueriesModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = QueriesModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorResponse, QueriesModel]]:
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
) -> Response[Union[ErrorResponse, QueriesModel]]:
    """List queries

     Returns a collection of queries. The collection can be filtered via query parameters similar to how
    work packages are filtered. Please note however, that the filters are applied to the queries and not
    to the work packages the queries in turn might return.

    Args:
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, QueriesModel]]
    """

    kwargs = _get_kwargs(
        client=client,
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
    filters: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, QueriesModel]]:
    """List queries

     Returns a collection of queries. The collection can be filtered via query parameters similar to how
    work packages are filtered. Please note however, that the filters are applied to the queries and not
    to the work packages the queries in turn might return.

    Args:
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, QueriesModel]]
    """

    return sync_detailed(
        client=client,
        filters=filters,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, QueriesModel]]:
    """List queries

     Returns a collection of queries. The collection can be filtered via query parameters similar to how
    work packages are filtered. Please note however, that the filters are applied to the queries and not
    to the work packages the queries in turn might return.

    Args:
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, QueriesModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        filters=filters,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, QueriesModel]]:
    """List queries

     Returns a collection of queries. The collection can be filtered via query parameters similar to how
    work packages are filtered. Please note however, that the filters are applied to the queries and not
    to the work packages the queries in turn might return.

    Args:
        filters (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, QueriesModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            filters=filters,
        )
    ).parsed
