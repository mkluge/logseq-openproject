from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.available_assignees_model import AvailableAssigneesModel
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v3/projects/{id}/available_assignees".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[AvailableAssigneesModel, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AvailableAssigneesModel.from_dict(response.json())

        return response_200
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
) -> Response[Union[AvailableAssigneesModel, ErrorResponse]]:
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
) -> Response[Union[AvailableAssigneesModel, ErrorResponse]]:
    """Available assignees

     Gets a list of users that can be assigned to work packages in the given project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvailableAssigneesModel, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
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
) -> Optional[Union[AvailableAssigneesModel, ErrorResponse]]:
    """Available assignees

     Gets a list of users that can be assigned to work packages in the given project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvailableAssigneesModel, ErrorResponse]]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
) -> Response[Union[AvailableAssigneesModel, ErrorResponse]]:
    """Available assignees

     Gets a list of users that can be assigned to work packages in the given project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvailableAssigneesModel, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
) -> Optional[Union[AvailableAssigneesModel, ErrorResponse]]:
    """Available assignees

     Gets a list of users that can be assigned to work packages in the given project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvailableAssigneesModel, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
