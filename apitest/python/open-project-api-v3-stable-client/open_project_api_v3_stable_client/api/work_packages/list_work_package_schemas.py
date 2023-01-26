from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.work_package_schemas_model import WorkPackageSchemasModel
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    filters: str,
) -> Dict[str, Any]:
    url = "{}/api/v3/work_packages/schemas".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["filters"] = filters

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, WorkPackageSchemasModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = WorkPackageSchemasModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ErrorResponse, WorkPackageSchemasModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    filters: str,
) -> Response[Union[Any, ErrorResponse, WorkPackageSchemasModel]]:
    """List Work Package Schemas

     List work package schemas.

    Args:
        filters (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackageSchemasModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        filters=filters,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    filters: str,
) -> Optional[Union[Any, ErrorResponse, WorkPackageSchemasModel]]:
    """List Work Package Schemas

     List work package schemas.

    Args:
        filters (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackageSchemasModel]]
    """

    return sync_detailed(
        client=client,
        filters=filters,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    filters: str,
) -> Response[Union[Any, ErrorResponse, WorkPackageSchemasModel]]:
    """List Work Package Schemas

     List work package schemas.

    Args:
        filters (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackageSchemasModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        filters=filters,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    filters: str,
) -> Optional[Union[Any, ErrorResponse, WorkPackageSchemasModel]]:
    """List Work Package Schemas

     List work package schemas.

    Args:
        filters (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, WorkPackageSchemasModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            filters=filters,
        )
    ).parsed
