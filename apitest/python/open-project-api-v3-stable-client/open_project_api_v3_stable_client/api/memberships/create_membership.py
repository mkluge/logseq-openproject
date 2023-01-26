from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.view_membership_model import ViewMembershipModel
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v3/memberships".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, ViewMembershipModel]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ViewMembershipModel.from_dict(response.json())

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
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ErrorResponse, ViewMembershipModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, ErrorResponse, ViewMembershipModel]]:
    """Create membership

     Creates a new membership applying the attributes provided in the body.

    You can use the form and schema to retrieve the valid attribute values and by that be guided towards
    successful creation.

    By providing a `notificationMessage` within the `_meta` block of the payload, the client can include
    a customized message to the user
    of the newly created membership. In case of a group, the message will be sent to every user
    belonging to the group.

    By including `{ \"sendNotifications\": false }` within the `_meta` block of the payload, no
    notifications is send out at all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ViewMembershipModel]]
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
) -> Optional[Union[Any, ErrorResponse, ViewMembershipModel]]:
    """Create membership

     Creates a new membership applying the attributes provided in the body.

    You can use the form and schema to retrieve the valid attribute values and by that be guided towards
    successful creation.

    By providing a `notificationMessage` within the `_meta` block of the payload, the client can include
    a customized message to the user
    of the newly created membership. In case of a group, the message will be sent to every user
    belonging to the group.

    By including `{ \"sendNotifications\": false }` within the `_meta` block of the payload, no
    notifications is send out at all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ViewMembershipModel]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, ErrorResponse, ViewMembershipModel]]:
    """Create membership

     Creates a new membership applying the attributes provided in the body.

    You can use the form and schema to retrieve the valid attribute values and by that be guided towards
    successful creation.

    By providing a `notificationMessage` within the `_meta` block of the payload, the client can include
    a customized message to the user
    of the newly created membership. In case of a group, the message will be sent to every user
    belonging to the group.

    By including `{ \"sendNotifications\": false }` within the `_meta` block of the payload, no
    notifications is send out at all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ViewMembershipModel]]
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
) -> Optional[Union[Any, ErrorResponse, ViewMembershipModel]]:
    """Create membership

     Creates a new membership applying the attributes provided in the body.

    You can use the form and schema to retrieve the valid attribute values and by that be guided towards
    successful creation.

    By providing a `notificationMessage` within the `_meta` block of the payload, the client can include
    a customized message to the user
    of the newly created membership. In case of a group, the message will be sent to every user
    belonging to the group.

    By including `{ \"sendNotifications\": false }` within the `_meta` block of the payload, no
    notifications is send out at all.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ViewMembershipModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
