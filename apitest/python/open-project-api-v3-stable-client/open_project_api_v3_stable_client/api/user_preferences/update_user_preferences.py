from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.update_user_preferences_json_body import UpdateUserPreferencesJsonBody
from ...models.user_preferences_model import UserPreferencesModel
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: UpdateUserPreferencesJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v3/my_preferences".format(client.base_url)

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
) -> Optional[Union[Any, ErrorResponse, UserPreferencesModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserPreferencesModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = cast(Any, None)
        return response_406
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = cast(Any, None)
        return response_415
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ErrorResponse, UserPreferencesModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: UpdateUserPreferencesJsonBody,
) -> Response[Union[Any, ErrorResponse, UserPreferencesModel]]:
    """Update my preferences

     When calling this endpoint the client provides a single object, containing the properties that it
    wants to change, in the body.

    Args:
        json_body (UpdateUserPreferencesJsonBody):  Example: {'autoHidePopups': True, 'timeZone':
            'Europe/Paris'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, UserPreferencesModel]]
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
    json_body: UpdateUserPreferencesJsonBody,
) -> Optional[Union[Any, ErrorResponse, UserPreferencesModel]]:
    """Update my preferences

     When calling this endpoint the client provides a single object, containing the properties that it
    wants to change, in the body.

    Args:
        json_body (UpdateUserPreferencesJsonBody):  Example: {'autoHidePopups': True, 'timeZone':
            'Europe/Paris'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, UserPreferencesModel]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: UpdateUserPreferencesJsonBody,
) -> Response[Union[Any, ErrorResponse, UserPreferencesModel]]:
    """Update my preferences

     When calling this endpoint the client provides a single object, containing the properties that it
    wants to change, in the body.

    Args:
        json_body (UpdateUserPreferencesJsonBody):  Example: {'autoHidePopups': True, 'timeZone':
            'Europe/Paris'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, UserPreferencesModel]]
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
    json_body: UpdateUserPreferencesJsonBody,
) -> Optional[Union[Any, ErrorResponse, UserPreferencesModel]]:
    """Update my preferences

     When calling this endpoint the client provides a single object, containing the properties that it
    wants to change, in the body.

    Args:
        json_body (UpdateUserPreferencesJsonBody):  Example: {'autoHidePopups': True, 'timeZone':
            'Europe/Paris'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, UserPreferencesModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
