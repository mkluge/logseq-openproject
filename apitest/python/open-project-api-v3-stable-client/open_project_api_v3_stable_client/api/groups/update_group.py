from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.update_group_json_body import UpdateGroupJsonBody
from ...models.view_group_model import ViewGroupModel
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: Client,
    json_body: UpdateGroupJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v3/groups/{id}".format(client.base_url, id=id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, ViewGroupModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ViewGroupModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
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
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ErrorResponse, ViewGroupModel]]:
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
    json_body: UpdateGroupJsonBody,
) -> Response[Union[Any, ErrorResponse, ViewGroupModel]]:
    """Update group

     Updates the given group by applying the attributes provided in the
    body.

    Please note that the `members` array provided will override the existing set of members (similar to
    a PUT). A client thus
    has to provide the complete list of members the group is to have after the PATCH even if only one
    member is to be added.

    Args:
        id (int):
        json_body (UpdateGroupJsonBody):  Example: {'_links': {'members': [{'href':
            '/api/v3/users/363'}, {'href': '/api/v3/users/60'}]}, 'name': 'The group'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ViewGroupModel]]
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
    json_body: UpdateGroupJsonBody,
) -> Optional[Union[Any, ErrorResponse, ViewGroupModel]]:
    """Update group

     Updates the given group by applying the attributes provided in the
    body.

    Please note that the `members` array provided will override the existing set of members (similar to
    a PUT). A client thus
    has to provide the complete list of members the group is to have after the PATCH even if only one
    member is to be added.

    Args:
        id (int):
        json_body (UpdateGroupJsonBody):  Example: {'_links': {'members': [{'href':
            '/api/v3/users/363'}, {'href': '/api/v3/users/60'}]}, 'name': 'The group'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ViewGroupModel]]
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
    json_body: UpdateGroupJsonBody,
) -> Response[Union[Any, ErrorResponse, ViewGroupModel]]:
    """Update group

     Updates the given group by applying the attributes provided in the
    body.

    Please note that the `members` array provided will override the existing set of members (similar to
    a PUT). A client thus
    has to provide the complete list of members the group is to have after the PATCH even if only one
    member is to be added.

    Args:
        id (int):
        json_body (UpdateGroupJsonBody):  Example: {'_links': {'members': [{'href':
            '/api/v3/users/363'}, {'href': '/api/v3/users/60'}]}, 'name': 'The group'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ViewGroupModel]]
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
    json_body: UpdateGroupJsonBody,
) -> Optional[Union[Any, ErrorResponse, ViewGroupModel]]:
    """Update group

     Updates the given group by applying the attributes provided in the
    body.

    Please note that the `members` array provided will override the existing set of members (similar to
    a PUT). A client thus
    has to provide the complete list of members the group is to have after the PATCH even if only one
    member is to be added.

    Args:
        id (int):
        json_body (UpdateGroupJsonBody):  Example: {'_links': {'members': [{'href':
            '/api/v3/users/363'}, {'href': '/api/v3/users/60'}]}, 'name': 'The group'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ViewGroupModel]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
