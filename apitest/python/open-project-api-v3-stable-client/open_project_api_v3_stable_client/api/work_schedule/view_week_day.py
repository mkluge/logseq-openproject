from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.week_day_model import WeekDayModel
from ...types import Response


def _get_kwargs(
    day: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v3/days/week/{day}".format(client.base_url, day=day)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, WeekDayModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WeekDayModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ErrorResponse, WeekDayModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    day: int,
    *,
    client: Client,
) -> Response[Union[Any, ErrorResponse, WeekDayModel]]:
    """View a week day

     View a week day and its attributes.

    Args:
        day (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WeekDayModel]]
    """

    kwargs = _get_kwargs(
        day=day,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    day: int,
    *,
    client: Client,
) -> Optional[Union[Any, ErrorResponse, WeekDayModel]]:
    """View a week day

     View a week day and its attributes.

    Args:
        day (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WeekDayModel]]
    """

    return sync_detailed(
        day=day,
        client=client,
    ).parsed


async def asyncio_detailed(
    day: int,
    *,
    client: Client,
) -> Response[Union[Any, ErrorResponse, WeekDayModel]]:
    """View a week day

     View a week day and its attributes.

    Args:
        day (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WeekDayModel]]
    """

    kwargs = _get_kwargs(
        day=day,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    day: int,
    *,
    client: Client,
) -> Optional[Union[Any, ErrorResponse, WeekDayModel]]:
    """View a week day

     View a week day and its attributes.

    Args:
        day (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WeekDayModel]]
    """

    return (
        await asyncio_detailed(
            day=day,
            client=client,
        )
    ).parsed
