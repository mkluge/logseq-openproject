from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.user_create_model import UserCreateModel
from ...models.user_model import UserModel
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: UserCreateModel,
) -> Dict[str, Any]:
    url = "{}/api/v3/users".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, UserModel]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = UserModel.from_dict(response.json())

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


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ErrorResponse, UserModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: UserCreateModel,
) -> Response[Union[Any, ErrorResponse, UserModel]]:
    """Create User

     Creates a new user. Only administrators and users with manage_user global permission are allowed to
    do so.
    When calling this endpoint the client provides a single object, containing at least the properties
    and links that are required, in the body.

    Valid values for `status`:

    1) \"active\" - In this case a password has to be provided in addition to the other attributes.

    2) \"invited\" - In this case nothing but the email address is required. The rest is optional. An
    invitation will be sent to the user.

    Args:
        json_body (UserCreateModel):  Example: {'login': 'j.sheppard', 'password':
            'idestroyedsouvereign', 'firstName': 'John', 'lastName': 'Sheppard', 'email':
            'shep@mail.com', 'admin': True, 'status': 'active', 'language': 'en'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, UserModel]]
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
    json_body: UserCreateModel,
) -> Optional[Union[Any, ErrorResponse, UserModel]]:
    """Create User

     Creates a new user. Only administrators and users with manage_user global permission are allowed to
    do so.
    When calling this endpoint the client provides a single object, containing at least the properties
    and links that are required, in the body.

    Valid values for `status`:

    1) \"active\" - In this case a password has to be provided in addition to the other attributes.

    2) \"invited\" - In this case nothing but the email address is required. The rest is optional. An
    invitation will be sent to the user.

    Args:
        json_body (UserCreateModel):  Example: {'login': 'j.sheppard', 'password':
            'idestroyedsouvereign', 'firstName': 'John', 'lastName': 'Sheppard', 'email':
            'shep@mail.com', 'admin': True, 'status': 'active', 'language': 'en'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, UserModel]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: UserCreateModel,
) -> Response[Union[Any, ErrorResponse, UserModel]]:
    """Create User

     Creates a new user. Only administrators and users with manage_user global permission are allowed to
    do so.
    When calling this endpoint the client provides a single object, containing at least the properties
    and links that are required, in the body.

    Valid values for `status`:

    1) \"active\" - In this case a password has to be provided in addition to the other attributes.

    2) \"invited\" - In this case nothing but the email address is required. The rest is optional. An
    invitation will be sent to the user.

    Args:
        json_body (UserCreateModel):  Example: {'login': 'j.sheppard', 'password':
            'idestroyedsouvereign', 'firstName': 'John', 'lastName': 'Sheppard', 'email':
            'shep@mail.com', 'admin': True, 'status': 'active', 'language': 'en'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, UserModel]]
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
    json_body: UserCreateModel,
) -> Optional[Union[Any, ErrorResponse, UserModel]]:
    """Create User

     Creates a new user. Only administrators and users with manage_user global permission are allowed to
    do so.
    When calling this endpoint the client provides a single object, containing at least the properties
    and links that are required, in the body.

    Valid values for `status`:

    1) \"active\" - In this case a password has to be provided in addition to the other attributes.

    2) \"invited\" - In this case nothing but the email address is required. The rest is optional. An
    invitation will be sent to the user.

    Args:
        json_body (UserCreateModel):  Example: {'login': 'j.sheppard', 'password':
            'idestroyedsouvereign', 'firstName': 'John', 'lastName': 'Sheppard', 'email':
            'shep@mail.com', 'admin': True, 'status': 'active', 'language': 'en'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, UserModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
