from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.week_day_collection_model import WeekDayCollectionModel
from ...models.week_day_collection_write_model import WeekDayCollectionWriteModel
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: WeekDayCollectionWriteModel,
) -> Dict[str, Any]:
    url = "{}/api/v3/days/week".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, WeekDayCollectionModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WeekDayCollectionModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
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
) -> Response[Union[Any, ErrorResponse, WeekDayCollectionModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: WeekDayCollectionWriteModel,
) -> Response[Union[Any, ErrorResponse, WeekDayCollectionModel]]:
    """Update week days (NOT IMPLEMENTED)

     **(NOT IMPLEMENTED)**
    Update multiple week days with work schedule information.

    Args:
        json_body (WeekDayCollectionWriteModel):  Example: {'_type': 'Collection', '_embedded':
            {'elements': [{'_type': 'WeekDay', 'working': True, '_links': {'self': {'href':
            '/api/v3/days/week/1'}}}, {'_type': 'WeekDay', 'working': True, '_links': {'self':
            {'href': '/api/v3/days/week/2'}}}, {'_type': 'WeekDay', 'working': True, '_links':
            {'self': {'href': '/api/v3/days/week/4'}}}, {'_type': 'WeekDay', 'working': False,
            '_links': {'self': {'href': '/api/v3/days/week/6'}}}, {'_type': 'WeekDay', 'working':
            False, '_links': {'self': {'href': '/api/v3/days/week/7'}}}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WeekDayCollectionModel]]
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
    json_body: WeekDayCollectionWriteModel,
) -> Optional[Union[Any, ErrorResponse, WeekDayCollectionModel]]:
    """Update week days (NOT IMPLEMENTED)

     **(NOT IMPLEMENTED)**
    Update multiple week days with work schedule information.

    Args:
        json_body (WeekDayCollectionWriteModel):  Example: {'_type': 'Collection', '_embedded':
            {'elements': [{'_type': 'WeekDay', 'working': True, '_links': {'self': {'href':
            '/api/v3/days/week/1'}}}, {'_type': 'WeekDay', 'working': True, '_links': {'self':
            {'href': '/api/v3/days/week/2'}}}, {'_type': 'WeekDay', 'working': True, '_links':
            {'self': {'href': '/api/v3/days/week/4'}}}, {'_type': 'WeekDay', 'working': False,
            '_links': {'self': {'href': '/api/v3/days/week/6'}}}, {'_type': 'WeekDay', 'working':
            False, '_links': {'self': {'href': '/api/v3/days/week/7'}}}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WeekDayCollectionModel]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: WeekDayCollectionWriteModel,
) -> Response[Union[Any, ErrorResponse, WeekDayCollectionModel]]:
    """Update week days (NOT IMPLEMENTED)

     **(NOT IMPLEMENTED)**
    Update multiple week days with work schedule information.

    Args:
        json_body (WeekDayCollectionWriteModel):  Example: {'_type': 'Collection', '_embedded':
            {'elements': [{'_type': 'WeekDay', 'working': True, '_links': {'self': {'href':
            '/api/v3/days/week/1'}}}, {'_type': 'WeekDay', 'working': True, '_links': {'self':
            {'href': '/api/v3/days/week/2'}}}, {'_type': 'WeekDay', 'working': True, '_links':
            {'self': {'href': '/api/v3/days/week/4'}}}, {'_type': 'WeekDay', 'working': False,
            '_links': {'self': {'href': '/api/v3/days/week/6'}}}, {'_type': 'WeekDay', 'working':
            False, '_links': {'self': {'href': '/api/v3/days/week/7'}}}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WeekDayCollectionModel]]
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
    json_body: WeekDayCollectionWriteModel,
) -> Optional[Union[Any, ErrorResponse, WeekDayCollectionModel]]:
    """Update week days (NOT IMPLEMENTED)

     **(NOT IMPLEMENTED)**
    Update multiple week days with work schedule information.

    Args:
        json_body (WeekDayCollectionWriteModel):  Example: {'_type': 'Collection', '_embedded':
            {'elements': [{'_type': 'WeekDay', 'working': True, '_links': {'self': {'href':
            '/api/v3/days/week/1'}}}, {'_type': 'WeekDay', 'working': True, '_links': {'self':
            {'href': '/api/v3/days/week/2'}}}, {'_type': 'WeekDay', 'working': True, '_links':
            {'self': {'href': '/api/v3/days/week/4'}}}, {'_type': 'WeekDay', 'working': False,
            '_links': {'self': {'href': '/api/v3/days/week/6'}}}, {'_type': 'WeekDay', 'working':
            False, '_links': {'self': {'href': '/api/v3/days/week/7'}}}]}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WeekDayCollectionModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
