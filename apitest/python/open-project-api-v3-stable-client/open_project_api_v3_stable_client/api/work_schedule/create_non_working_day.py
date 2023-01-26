from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.non_working_day_model import NonWorkingDayModel
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: NonWorkingDayModel,
) -> Dict[str, Any]:
    url = "{}/api/v3/days/non_working".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, NonWorkingDayModel]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = NonWorkingDayModel.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = cast(Any, None)
        return response_406
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = cast(Any, None)
        return response_415
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ErrorResponse, NonWorkingDayModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: NonWorkingDayModel,
) -> Response[Union[Any, ErrorResponse, NonWorkingDayModel]]:
    """Creates a non-working day (NOT IMPLEMENTED)

     **(NOT IMPLEMENTED)**
    Marks a day as being a non-working day.

    Note: creating a non-working day will not affect the start and finish dates
    of work packages but will affect their duration.

    Args:
        json_body (NonWorkingDayModel):  Example: {'_type': 'NonWorkingDay', 'date': '2022-12-25',
            'name': 'Christmas', '_links': {'self': {'href': '/api/v3/days/non_working/2022-12-25',
            'title': 'Christmas'}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, NonWorkingDayModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: NonWorkingDayModel,
) -> Optional[Union[Any, ErrorResponse, NonWorkingDayModel]]:
    """Creates a non-working day (NOT IMPLEMENTED)

     **(NOT IMPLEMENTED)**
    Marks a day as being a non-working day.

    Note: creating a non-working day will not affect the start and finish dates
    of work packages but will affect their duration.

    Args:
        json_body (NonWorkingDayModel):  Example: {'_type': 'NonWorkingDay', 'date': '2022-12-25',
            'name': 'Christmas', '_links': {'self': {'href': '/api/v3/days/non_working/2022-12-25',
            'title': 'Christmas'}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, NonWorkingDayModel]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: NonWorkingDayModel,
) -> Response[Union[Any, ErrorResponse, NonWorkingDayModel]]:
    """Creates a non-working day (NOT IMPLEMENTED)

     **(NOT IMPLEMENTED)**
    Marks a day as being a non-working day.

    Note: creating a non-working day will not affect the start and finish dates
    of work packages but will affect their duration.

    Args:
        json_body (NonWorkingDayModel):  Example: {'_type': 'NonWorkingDay', 'date': '2022-12-25',
            'name': 'Christmas', '_links': {'self': {'href': '/api/v3/days/non_working/2022-12-25',
            'title': 'Christmas'}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, NonWorkingDayModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: NonWorkingDayModel,
) -> Optional[Union[Any, ErrorResponse, NonWorkingDayModel]]:
    """Creates a non-working day (NOT IMPLEMENTED)

     **(NOT IMPLEMENTED)**
    Marks a day as being a non-working day.

    Note: creating a non-working day will not affect the start and finish dates
    of work packages but will affect their duration.

    Args:
        json_body (NonWorkingDayModel):  Example: {'_type': 'NonWorkingDay', 'date': '2022-12-25',
            'name': 'Christmas', '_links': {'self': {'href': '/api/v3/days/non_working/2022-12-25',
            'title': 'Christmas'}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, NonWorkingDayModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
