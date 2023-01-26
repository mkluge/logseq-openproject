from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.relation_model import RelationModel
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v3/relations/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, RelationModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RelationModel.from_dict(response.json())

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
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ErrorResponse, RelationModel]]:
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
) -> Response[Union[Any, ErrorResponse, RelationModel]]:
    """Edit Relation

     When calling this endpoint the client provides a single object, containing the properties and links
    that it wants to change, in the body.
    It is only allowed to provide properties or links supporting the **write** operation.

    Note that changing the `type` of a relation invariably also changes the respective `reverseType` as
    well as the \"name\" of it.
    The returned Relation object will reflect that change. For instance if you change a Relation's
    `type` to \"follows\" then the `reverseType` will be changed to `precedes`.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, RelationModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
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
) -> Optional[Union[Any, ErrorResponse, RelationModel]]:
    """Edit Relation

     When calling this endpoint the client provides a single object, containing the properties and links
    that it wants to change, in the body.
    It is only allowed to provide properties or links supporting the **write** operation.

    Note that changing the `type` of a relation invariably also changes the respective `reverseType` as
    well as the \"name\" of it.
    The returned Relation object will reflect that change. For instance if you change a Relation's
    `type` to \"follows\" then the `reverseType` will be changed to `precedes`.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, RelationModel]]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
) -> Response[Union[Any, ErrorResponse, RelationModel]]:
    """Edit Relation

     When calling this endpoint the client provides a single object, containing the properties and links
    that it wants to change, in the body.
    It is only allowed to provide properties or links supporting the **write** operation.

    Note that changing the `type` of a relation invariably also changes the respective `reverseType` as
    well as the \"name\" of it.
    The returned Relation object will reflect that change. For instance if you change a Relation's
    `type` to \"follows\" then the `reverseType` will be changed to `precedes`.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, RelationModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
) -> Optional[Union[Any, ErrorResponse, RelationModel]]:
    """Edit Relation

     When calling this endpoint the client provides a single object, containing the properties and links
    that it wants to change, in the body.
    It is only allowed to provide properties or links supporting the **write** operation.

    Note that changing the `type` of a relation invariably also changes the respective `reverseType` as
    well as the \"name\" of it.
    The returned Relation object will reflect that change. For instance if you change a Relation's
    `type` to \"follows\" then the `reverseType` will be changed to `precedes`.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, RelationModel]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
