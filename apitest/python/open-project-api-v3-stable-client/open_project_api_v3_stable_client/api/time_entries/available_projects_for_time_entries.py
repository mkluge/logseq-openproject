from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.available_projects_for_time_entries_model import AvailableProjectsForTimeEntriesModel
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v3/time_entries/available_projects".format(client.base_url)

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
) -> Optional[Union[AvailableProjectsForTimeEntriesModel, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AvailableProjectsForTimeEntriesModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[AvailableProjectsForTimeEntriesModel, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[AvailableProjectsForTimeEntriesModel, ErrorResponse]]:
    """Available projects for time entries

     Gets a list of projects in which a time entry can be created in or be assigned to on update. The
    list contains all projects in which the user issuing the request has the necessary permissions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvailableProjectsForTimeEntriesModel, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[AvailableProjectsForTimeEntriesModel, ErrorResponse]]:
    """Available projects for time entries

     Gets a list of projects in which a time entry can be created in or be assigned to on update. The
    list contains all projects in which the user issuing the request has the necessary permissions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvailableProjectsForTimeEntriesModel, ErrorResponse]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[AvailableProjectsForTimeEntriesModel, ErrorResponse]]:
    """Available projects for time entries

     Gets a list of projects in which a time entry can be created in or be assigned to on update. The
    list contains all projects in which the user issuing the request has the necessary permissions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvailableProjectsForTimeEntriesModel, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[AvailableProjectsForTimeEntriesModel, ErrorResponse]]:
    """Available projects for time entries

     Gets a list of projects in which a time entry can be created in or be assigned to on update. The
    list contains all projects in which the user issuing the request has the necessary permissions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AvailableProjectsForTimeEntriesModel, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
