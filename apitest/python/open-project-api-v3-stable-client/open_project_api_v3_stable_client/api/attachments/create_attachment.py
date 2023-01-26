from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.attachment_model import AttachmentModel
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v3/attachments".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, AttachmentModel, ErrorResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AttachmentModel.from_dict(response.json())

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
) -> Response[Union[Any, AttachmentModel, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, AttachmentModel, ErrorResponse]]:
    """Create Attachment

     Clients can create attachments without a container first and attach them later on.
    This is useful if the container does not exist at the time the attachment is uploaded.
    After the upload, the client can then claim such containerless attachments for any resource eligible
    (e.g. WorkPackage) on subsequent requests.
    The upload and the claiming *must* be done for the same user account. Attachments uploaded by
    another user cannot be claimed and
    once claimed for a resource, they cannot be claimed by another.

    The upload request must be of type `multipart/form-data` with exactly two parts.

    The first part *must* be called `metadata`. Its content type is expected to be `application/json`,
    the body *must* be a single JSON object, containing at least the `fileName` and optionally the
    attachments `description`.

    The second part *must* be called `file`, its content type *should* match the mime type of the file.
    The body *must* be the raw content of the file.
    Note that a `filename` *must* be indicated in the `Content-Disposition` of this part, although it
    will be ignored.
    Instead the `fileName` inside the JSON of the metadata part will be used.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AttachmentModel, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[Any, AttachmentModel, ErrorResponse]]:
    """Create Attachment

     Clients can create attachments without a container first and attach them later on.
    This is useful if the container does not exist at the time the attachment is uploaded.
    After the upload, the client can then claim such containerless attachments for any resource eligible
    (e.g. WorkPackage) on subsequent requests.
    The upload and the claiming *must* be done for the same user account. Attachments uploaded by
    another user cannot be claimed and
    once claimed for a resource, they cannot be claimed by another.

    The upload request must be of type `multipart/form-data` with exactly two parts.

    The first part *must* be called `metadata`. Its content type is expected to be `application/json`,
    the body *must* be a single JSON object, containing at least the `fileName` and optionally the
    attachments `description`.

    The second part *must* be called `file`, its content type *should* match the mime type of the file.
    The body *must* be the raw content of the file.
    Note that a `filename` *must* be indicated in the `Content-Disposition` of this part, although it
    will be ignored.
    Instead the `fileName` inside the JSON of the metadata part will be used.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AttachmentModel, ErrorResponse]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, AttachmentModel, ErrorResponse]]:
    """Create Attachment

     Clients can create attachments without a container first and attach them later on.
    This is useful if the container does not exist at the time the attachment is uploaded.
    After the upload, the client can then claim such containerless attachments for any resource eligible
    (e.g. WorkPackage) on subsequent requests.
    The upload and the claiming *must* be done for the same user account. Attachments uploaded by
    another user cannot be claimed and
    once claimed for a resource, they cannot be claimed by another.

    The upload request must be of type `multipart/form-data` with exactly two parts.

    The first part *must* be called `metadata`. Its content type is expected to be `application/json`,
    the body *must* be a single JSON object, containing at least the `fileName` and optionally the
    attachments `description`.

    The second part *must* be called `file`, its content type *should* match the mime type of the file.
    The body *must* be the raw content of the file.
    Note that a `filename` *must* be indicated in the `Content-Disposition` of this part, although it
    will be ignored.
    Instead the `fileName` inside the JSON of the metadata part will be used.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AttachmentModel, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[Any, AttachmentModel, ErrorResponse]]:
    """Create Attachment

     Clients can create attachments without a container first and attach them later on.
    This is useful if the container does not exist at the time the attachment is uploaded.
    After the upload, the client can then claim such containerless attachments for any resource eligible
    (e.g. WorkPackage) on subsequent requests.
    The upload and the claiming *must* be done for the same user account. Attachments uploaded by
    another user cannot be claimed and
    once claimed for a resource, they cannot be claimed by another.

    The upload request must be of type `multipart/form-data` with exactly two parts.

    The first part *must* be called `metadata`. Its content type is expected to be `application/json`,
    the body *must* be a single JSON object, containing at least the `fileName` and optionally the
    attachments `description`.

    The second part *must* be called `file`, its content type *should* match the mime type of the file.
    The body *must* be the raw content of the file.
    Note that a `filename` *must* be indicated in the `Content-Disposition` of this part, although it
    will be ignored.
    Instead the `fileName` inside the JSON of the metadata part will be used.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AttachmentModel, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
