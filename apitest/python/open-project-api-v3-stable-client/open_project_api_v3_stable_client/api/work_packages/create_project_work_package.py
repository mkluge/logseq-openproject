from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.work_package_model import WorkPackageModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: Client,
    notify: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/api/v3/projects/{id}/work_packages".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["notify"] = notify

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, WorkPackageModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WorkPackageModel.from_dict(response.json())

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


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ErrorResponse, WorkPackageModel]]:
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
    notify: Union[Unset, None, bool] = True,
) -> Response[Union[Any, ErrorResponse, WorkPackageModel]]:
    """Create work package in project

     When calling this endpoint the client provides a single object, containing at least the properties
    and links that
    are required, in the body. The required fields of a WorkPackage can be found in its schema, which is
    embedded in
    the respective form. Note that it is only allowed to provide properties or links supporting the
    write operation.

    Args:
        id (int):
        notify (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackageModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
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
    notify: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, ErrorResponse, WorkPackageModel]]:
    """Create work package in project

     When calling this endpoint the client provides a single object, containing at least the properties
    and links that
    are required, in the body. The required fields of a WorkPackage can be found in its schema, which is
    embedded in
    the respective form. Note that it is only allowed to provide properties or links supporting the
    write operation.

    Args:
        id (int):
        notify (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackageModel]]
    """

    return sync_detailed(
        id=id,
        client=client,
        notify=notify,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    notify: Union[Unset, None, bool] = True,
) -> Response[Union[Any, ErrorResponse, WorkPackageModel]]:
    """Create work package in project

     When calling this endpoint the client provides a single object, containing at least the properties
    and links that
    are required, in the body. The required fields of a WorkPackage can be found in its schema, which is
    embedded in
    the respective form. Note that it is only allowed to provide properties or links supporting the
    write operation.

    Args:
        id (int):
        notify (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackageModel]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        notify=notify,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    notify: Union[Unset, None, bool] = True,
) -> Optional[Union[Any, ErrorResponse, WorkPackageModel]]:
    """Create work package in project

     When calling this endpoint the client provides a single object, containing at least the properties
    and links that
    are required, in the body. The required fields of a WorkPackage can be found in its schema, which is
    embedded in
    the respective form. Note that it is only allowed to provide properties or links supporting the
    write operation.

    Args:
        id (int):
        notify (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackageModel]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            notify=notify,
        )
    ).parsed
