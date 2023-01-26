from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.comment_work_package_json_body import CommentWorkPackageJsonBody
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    json_body: CommentWorkPackageJsonBody,
    notify: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/api/v3/work_packages/{id}/activities".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["notify"] = notify

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = cast(Any, None)
        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
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
    json_body: CommentWorkPackageJsonBody,
    notify: Union[Unset, None, bool] = True,
) -> Response[Union[Any, ErrorResponse]]:
    """Comment work package

     Creates an activity for the selected work package and, on success, returns the
    updated activity.

    Args:
        id (int):
        notify (Union[Unset, None, bool]):  Default: True.
        json_body (CommentWorkPackageJsonBody):  Example: {'comment': {'raw': 'I think this is
            awesome!'}}.

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
        notify=notify,
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
    json_body: CommentWorkPackageJsonBody,
    notify: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, ErrorResponse]]:
    """Comment work package

     Creates an activity for the selected work package and, on success, returns the
    updated activity.

    Args:
        id (int):
        notify (Union[Unset, None, bool]):  Default: True.
        json_body (CommentWorkPackageJsonBody):  Example: {'comment': {'raw': 'I think this is
            awesome!'}}.

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
        notify=notify,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    json_body: CommentWorkPackageJsonBody,
    notify: Union[Unset, None, bool] = True,
) -> Response[Union[Any, ErrorResponse]]:
    """Comment work package

     Creates an activity for the selected work package and, on success, returns the
    updated activity.

    Args:
        id (int):
        notify (Union[Unset, None, bool]):  Default: True.
        json_body (CommentWorkPackageJsonBody):  Example: {'comment': {'raw': 'I think this is
            awesome!'}}.

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
        notify=notify,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    json_body: CommentWorkPackageJsonBody,
    notify: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, ErrorResponse]]:
    """Comment work package

     Creates an activity for the selected work package and, on success, returns the
    updated activity.

    Args:
        id (int):
        notify (Union[Unset, None, bool]):  Default: True.
        json_body (CommentWorkPackageJsonBody):  Example: {'comment': {'raw': 'I think this is
            awesome!'}}.

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
            notify=notify,
        )
    ).parsed
