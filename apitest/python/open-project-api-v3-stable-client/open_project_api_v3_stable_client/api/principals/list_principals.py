from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.principals_model import PrincipalsModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
    select: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v3/principals".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["filters"] = filters

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PrincipalsModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PrincipalsModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PrincipalsModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
    select: Union[Unset, None, str] = UNSET,
) -> Response[PrincipalsModel]:
    """List principals

     List all principals. The client can choose to filter the principals similar to how work packages are
    filtered. In addition to the provided filters, the server will reduce the result set to only contain
    principals who are members in projects the client is allowed to see.

    Args:
        filters (Union[Unset, None, str]):
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PrincipalsModel]
    """

    kwargs = _get_kwargs(
        client=client,
        filters=filters,
        select=select,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
    select: Union[Unset, None, str] = UNSET,
) -> Optional[PrincipalsModel]:
    """List principals

     List all principals. The client can choose to filter the principals similar to how work packages are
    filtered. In addition to the provided filters, the server will reduce the result set to only contain
    principals who are members in projects the client is allowed to see.

    Args:
        filters (Union[Unset, None, str]):
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PrincipalsModel]
    """

    return sync_detailed(
        client=client,
        filters=filters,
        select=select,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
    select: Union[Unset, None, str] = UNSET,
) -> Response[PrincipalsModel]:
    """List principals

     List all principals. The client can choose to filter the principals similar to how work packages are
    filtered. In addition to the provided filters, the server will reduce the result set to only contain
    principals who are members in projects the client is allowed to see.

    Args:
        filters (Union[Unset, None, str]):
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PrincipalsModel]
    """

    kwargs = _get_kwargs(
        client=client,
        filters=filters,
        select=select,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
    select: Union[Unset, None, str] = UNSET,
) -> Optional[PrincipalsModel]:
    """List principals

     List all principals. The client can choose to filter the principals similar to how work packages are
    filtered. In addition to the provided filters, the server will reduce the result set to only contain
    principals who are members in projects the client is allowed to see.

    Args:
        filters (Union[Unset, None, str]):
        select (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PrincipalsModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            filters=filters,
            select=select,
        )
    ).parsed
