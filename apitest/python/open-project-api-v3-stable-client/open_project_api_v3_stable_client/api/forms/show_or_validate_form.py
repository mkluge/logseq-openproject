from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.example_form_model import ExampleFormModel
from ...models.show_or_validate_form_json_body import ShowOrValidateFormJsonBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: ShowOrValidateFormJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v3/example/form".format(client.base_url)

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


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ErrorResponse, ExampleFormModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ExampleFormModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_ACCEPTABLE:
        response_406 = cast(Any, None)
        return response_406
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE:
        response_415 = cast(Any, None)
        return response_415
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ErrorResponse, ExampleFormModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ShowOrValidateFormJsonBody,
) -> Response[Union[Any, ErrorResponse, ExampleFormModel]]:
    """show or validate form

     This is an example of how a form might look like. Note that this endpoint does not exist in the
    actual implementation.

    Args:
        json_body (ShowOrValidateFormJsonBody):  Example: {'_type': 'Example', 'lockVersion': 5,
            'subject': 'An example title'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ExampleFormModel]]
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
    json_body: ShowOrValidateFormJsonBody,
) -> Optional[Union[Any, ErrorResponse, ExampleFormModel]]:
    """show or validate form

     This is an example of how a form might look like. Note that this endpoint does not exist in the
    actual implementation.

    Args:
        json_body (ShowOrValidateFormJsonBody):  Example: {'_type': 'Example', 'lockVersion': 5,
            'subject': 'An example title'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ExampleFormModel]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: ShowOrValidateFormJsonBody,
) -> Response[Union[Any, ErrorResponse, ExampleFormModel]]:
    """show or validate form

     This is an example of how a form might look like. Note that this endpoint does not exist in the
    actual implementation.

    Args:
        json_body (ShowOrValidateFormJsonBody):  Example: {'_type': 'Example', 'lockVersion': 5,
            'subject': 'An example title'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ExampleFormModel]]
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
    json_body: ShowOrValidateFormJsonBody,
) -> Optional[Union[Any, ErrorResponse, ExampleFormModel]]:
    """show or validate form

     This is an example of how a form might look like. Note that this endpoint does not exist in the
    actual implementation.

    Args:
        json_body (ShowOrValidateFormJsonBody):  Example: {'_type': 'Example', 'lockVersion': 5,
            'subject': 'An example title'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse, ExampleFormModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
