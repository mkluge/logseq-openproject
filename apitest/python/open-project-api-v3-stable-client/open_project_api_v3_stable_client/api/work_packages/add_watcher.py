from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.add_watcher_json_body import AddWatcherJsonBody
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: Client,
    json_body: AddWatcherJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v3/work_packages/{id}/watchers".format(client.base_url, id=id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == HTTPStatus.CREATED:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = cast(Any, None)
        return response_406
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = cast(Any, None)
        return response_415
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ErrorResponse]]:
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
    json_body: AddWatcherJsonBody,
) -> Response[Union[Any, ErrorResponse]]:
    """Add watcher

     Adds a watcher to the specified work package.

    The request is expected to contain a single JSON object, that contains a link object under the
    `user` key.

    The response will be user added as watcher.
    In case the user was already watching the work package an `HTTP 200` is returned, an
    `HTTP 201` if the user was added as a new watcher.

    Args:
        id (int):
        json_body (AddWatcherJsonBody):  Example: {'user': {'href': '/api/v3/users/1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
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
    json_body: AddWatcherJsonBody,
) -> Optional[Union[Any, ErrorResponse]]:
    """Add watcher

     Adds a watcher to the specified work package.

    The request is expected to contain a single JSON object, that contains a link object under the
    `user` key.

    The response will be user added as watcher.
    In case the user was already watching the work package an `HTTP 200` is returned, an
    `HTTP 201` if the user was added as a new watcher.

    Args:
        id (int):
        json_body (AddWatcherJsonBody):  Example: {'user': {'href': '/api/v3/users/1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    json_body: AddWatcherJsonBody,
) -> Response[Union[Any, ErrorResponse]]:
    """Add watcher

     Adds a watcher to the specified work package.

    The request is expected to contain a single JSON object, that contains a link object under the
    `user` key.

    The response will be user added as watcher.
    In case the user was already watching the work package an `HTTP 200` is returned, an
    `HTTP 201` if the user was added as a new watcher.

    Args:
        id (int):
        json_body (AddWatcherJsonBody):  Example: {'user': {'href': '/api/v3/users/1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    json_body: AddWatcherJsonBody,
) -> Optional[Union[Any, ErrorResponse]]:
    """Add watcher

     Adds a watcher to the specified work package.

    The request is expected to contain a single JSON object, that contains a link object under the
    `user` key.

    The response will be user added as watcher.
    In case the user was already watching the work package an `HTTP 200` is returned, an
    `HTTP 201` if the user was added as a new watcher.

    Args:
        id (int):
        json_body (AddWatcherJsonBody):  Example: {'user': {'href': '/api/v3/users/1'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
