import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.day_model import DayModel
from ...types import Response


def _get_kwargs(
    date: datetime.date,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v3/days/{date}".format(client.base_url, date=date)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, DayModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DayModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, DayModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    date: datetime.date,
    *,
    client: Client,
) -> Response[Union[Any, DayModel]]:
    """View day

     View the day information for a given date.

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DayModel]]
    """

    kwargs = _get_kwargs(
        date=date,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    date: datetime.date,
    *,
    client: Client,
) -> Optional[Union[Any, DayModel]]:
    """View day

     View the day information for a given date.

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DayModel]]
    """

    return sync_detailed(
        date=date,
        client=client,
    ).parsed


async def asyncio_detailed(
    date: datetime.date,
    *,
    client: Client,
) -> Response[Union[Any, DayModel]]:
    """View day

     View the day information for a given date.

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DayModel]]
    """

    kwargs = _get_kwargs(
        date=date,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    date: datetime.date,
    *,
    client: Client,
) -> Optional[Union[Any, DayModel]]:
    """View day

     View the day information for a given date.

    Args:
        date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DayModel]]
    """

    return (
        await asyncio_detailed(
            date=date,
            client=client,
        )
    ).parsed
