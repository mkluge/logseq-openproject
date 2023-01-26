from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.relation_schema_model import RelationSchemaModel
from ...types import Response


def _get_kwargs(
    type: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v3/relations/schema/{type}".format(client.base_url, type=type)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorResponse, RelationSchemaModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RelationSchemaModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorResponse, RelationSchemaModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type: str,
    *,
    client: Client,
) -> Response[Union[ErrorResponse, RelationSchemaModel]]:
    """View relation schema for type

    Args:
        type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RelationSchemaModel]]
    """

    kwargs = _get_kwargs(
        type=type,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type: str,
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, RelationSchemaModel]]:
    """View relation schema for type

    Args:
        type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RelationSchemaModel]]
    """

    return sync_detailed(
        type=type,
        client=client,
    ).parsed


async def asyncio_detailed(
    type: str,
    *,
    client: Client,
) -> Response[Union[ErrorResponse, RelationSchemaModel]]:
    """View relation schema for type

    Args:
        type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RelationSchemaModel]]
    """

    kwargs = _get_kwargs(
        type=type,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type: str,
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, RelationSchemaModel]]:
    """View relation schema for type

    Args:
        type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, RelationSchemaModel]]
    """

    return (
        await asyncio_detailed(
            type=type,
            client=client,
        )
    ).parsed
