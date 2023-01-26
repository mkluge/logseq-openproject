from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.execute_custom_action_json_body import ExecuteCustomActionJsonBody
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: Client,
    json_body: ExecuteCustomActionJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v3/custom_actions/{id}/execute".format(client.base_url, id=id)

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
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409
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
    json_body: ExecuteCustomActionJsonBody,
) -> Response[Union[Any, ErrorResponse]]:
    """Execute custom action

     A POST to this end point executes the custom action on the work package provided in the payload. The
    altered work package will be returned. In order to avoid executing
     the custom action unbeknown to a change that has already taken place, the client has to provide the
    work package's current lockVersion.

    Args:
        id (int):
        json_body (ExecuteCustomActionJsonBody):  Example: {'_links': {'workPackage': {'href':
            '/api/v3/work_packages/42'}}, 'lockVersion': '3'}.

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
    json_body: ExecuteCustomActionJsonBody,
) -> Optional[Union[Any, ErrorResponse]]:
    """Execute custom action

     A POST to this end point executes the custom action on the work package provided in the payload. The
    altered work package will be returned. In order to avoid executing
     the custom action unbeknown to a change that has already taken place, the client has to provide the
    work package's current lockVersion.

    Args:
        id (int):
        json_body (ExecuteCustomActionJsonBody):  Example: {'_links': {'workPackage': {'href':
            '/api/v3/work_packages/42'}}, 'lockVersion': '3'}.

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
    json_body: ExecuteCustomActionJsonBody,
) -> Response[Union[Any, ErrorResponse]]:
    """Execute custom action

     A POST to this end point executes the custom action on the work package provided in the payload. The
    altered work package will be returned. In order to avoid executing
     the custom action unbeknown to a change that has already taken place, the client has to provide the
    work package's current lockVersion.

    Args:
        id (int):
        json_body (ExecuteCustomActionJsonBody):  Example: {'_links': {'workPackage': {'href':
            '/api/v3/work_packages/42'}}, 'lockVersion': '3'}.

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
    json_body: ExecuteCustomActionJsonBody,
) -> Optional[Union[Any, ErrorResponse]]:
    """Execute custom action

     A POST to this end point executes the custom action on the work package provided in the payload. The
    altered work package will be returned. In order to avoid executing
     the custom action unbeknown to a change that has already taken place, the client has to provide the
    work package's current lockVersion.

    Args:
        id (int):
        json_body (ExecuteCustomActionJsonBody):  Example: {'_links': {'workPackage': {'href':
            '/api/v3/work_packages/42'}}, 'lockVersion': '3'}.

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
