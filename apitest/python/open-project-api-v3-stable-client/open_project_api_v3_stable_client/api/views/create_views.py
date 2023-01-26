from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.create_views_json_body import CreateViewsJsonBody
from ...models.create_views_response_201 import CreateViewsResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: CreateViewsJsonBody,
) -> Dict[str, Any]:
    url = "{}/api/v3/views/{id}".format(client.base_url, id=id)

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
) -> Optional[Union[Any, CreateViewsResponse201, ErrorResponse]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = CreateViewsResponse201.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
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
) -> Response[Union[Any, CreateViewsResponse201, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    json_body: CreateViewsJsonBody,
) -> Response[Union[Any, CreateViewsResponse201, ErrorResponse]]:
    """Create view

     When calling this endpoint the client provides a single object, containing at least the properties
    and links that are required, in the body.
    The required fields of a View can be found in its schema, which is embedded in the respective form.
    Note that it is only allowed to provide properties or links supporting the write operation.

    There are different subtypes of `Views` (e.g. `Views::WorkPackagesTable`) with each having its own
    endpoint for creating that subtype e.g.

    * `/api/v3/views/work_packages_table` for `Views::WorkPackagesTable`
    * `/api/v3/views/team_planner` for `Views::TeamPlanner`
    * `/api/v3/views/work_packages_calendar` for `Views::WorkPackagesCalendar`

    **Not yet implemented** To get the list of available subtypes and by that the endpoints for creating
    a subtype, use the
    ```
      /api/v3/views/schemas
    ```
    endpoint.

    Args:
        id (str):
        json_body (CreateViewsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateViewsResponse201, ErrorResponse]]
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
    id: str,
    *,
    client: Client,
    json_body: CreateViewsJsonBody,
) -> Optional[Union[Any, CreateViewsResponse201, ErrorResponse]]:
    """Create view

     When calling this endpoint the client provides a single object, containing at least the properties
    and links that are required, in the body.
    The required fields of a View can be found in its schema, which is embedded in the respective form.
    Note that it is only allowed to provide properties or links supporting the write operation.

    There are different subtypes of `Views` (e.g. `Views::WorkPackagesTable`) with each having its own
    endpoint for creating that subtype e.g.

    * `/api/v3/views/work_packages_table` for `Views::WorkPackagesTable`
    * `/api/v3/views/team_planner` for `Views::TeamPlanner`
    * `/api/v3/views/work_packages_calendar` for `Views::WorkPackagesCalendar`

    **Not yet implemented** To get the list of available subtypes and by that the endpoints for creating
    a subtype, use the
    ```
      /api/v3/views/schemas
    ```
    endpoint.

    Args:
        id (str):
        json_body (CreateViewsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateViewsResponse201, ErrorResponse]]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: CreateViewsJsonBody,
) -> Response[Union[Any, CreateViewsResponse201, ErrorResponse]]:
    """Create view

     When calling this endpoint the client provides a single object, containing at least the properties
    and links that are required, in the body.
    The required fields of a View can be found in its schema, which is embedded in the respective form.
    Note that it is only allowed to provide properties or links supporting the write operation.

    There are different subtypes of `Views` (e.g. `Views::WorkPackagesTable`) with each having its own
    endpoint for creating that subtype e.g.

    * `/api/v3/views/work_packages_table` for `Views::WorkPackagesTable`
    * `/api/v3/views/team_planner` for `Views::TeamPlanner`
    * `/api/v3/views/work_packages_calendar` for `Views::WorkPackagesCalendar`

    **Not yet implemented** To get the list of available subtypes and by that the endpoints for creating
    a subtype, use the
    ```
      /api/v3/views/schemas
    ```
    endpoint.

    Args:
        id (str):
        json_body (CreateViewsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateViewsResponse201, ErrorResponse]]
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
    id: str,
    *,
    client: Client,
    json_body: CreateViewsJsonBody,
) -> Optional[Union[Any, CreateViewsResponse201, ErrorResponse]]:
    """Create view

     When calling this endpoint the client provides a single object, containing at least the properties
    and links that are required, in the body.
    The required fields of a View can be found in its schema, which is embedded in the respective form.
    Note that it is only allowed to provide properties or links supporting the write operation.

    There are different subtypes of `Views` (e.g. `Views::WorkPackagesTable`) with each having its own
    endpoint for creating that subtype e.g.

    * `/api/v3/views/work_packages_table` for `Views::WorkPackagesTable`
    * `/api/v3/views/team_planner` for `Views::TeamPlanner`
    * `/api/v3/views/work_packages_calendar` for `Views::WorkPackagesCalendar`

    **Not yet implemented** To get the list of available subtypes and by that the endpoints for creating
    a subtype, use the
    ```
      /api/v3/views/schemas
    ```
    endpoint.

    Args:
        id (str):
        json_body (CreateViewsJsonBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateViewsResponse201, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
