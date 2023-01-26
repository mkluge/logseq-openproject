from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.list_available_parent_project_candidates_model import ListAvailableParentProjectCandidatesModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
    of: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v3/projects/available_parent_projects".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["filters"] = filters

    params["of"] = of

    params["sortBy"] = sort_by

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
) -> Optional[Union[ErrorResponse, ListAvailableParentProjectCandidatesModel]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListAvailableParentProjectCandidatesModel.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ErrorResponse, ListAvailableParentProjectCandidatesModel]]:
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
    of: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, ListAvailableParentProjectCandidatesModel]]:
    """List available parent project candidates

     Lists projects which can become parent to another project. Only sound candidates are returned.
    For instance a project cannot become parent of itself or it's children.

    To specify the project for which a parent is queried for, the `of` parameter can be provided. If no
    `of`
    parameter is provided, a new project is assumed. Then, the check for the hierarchy is omitted as a
    new project cannot be
    part of a hierarchy yet.

    Candidates can be filtered. Most commonly one will want to filter by name or identifier.
    You can do this through the `filters` parameter which works just like the work package index.

    For instance to find all parent candidates with \"rollout\" in their name:

    ```
    ?filters=[{\"name_and_identifier\":{\"operator\":\"~\",\"values\":[\"rollout\"]}}]
    ```

    Args:
        filters (Union[Unset, None, str]):
        of (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListAvailableParentProjectCandidatesModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        filters=filters,
        of=of,
        sort_by=sort_by,
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
    of: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, ListAvailableParentProjectCandidatesModel]]:
    """List available parent project candidates

     Lists projects which can become parent to another project. Only sound candidates are returned.
    For instance a project cannot become parent of itself or it's children.

    To specify the project for which a parent is queried for, the `of` parameter can be provided. If no
    `of`
    parameter is provided, a new project is assumed. Then, the check for the hierarchy is omitted as a
    new project cannot be
    part of a hierarchy yet.

    Candidates can be filtered. Most commonly one will want to filter by name or identifier.
    You can do this through the `filters` parameter which works just like the work package index.

    For instance to find all parent candidates with \"rollout\" in their name:

    ```
    ?filters=[{\"name_and_identifier\":{\"operator\":\"~\",\"values\":[\"rollout\"]}}]
    ```

    Args:
        filters (Union[Unset, None, str]):
        of (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListAvailableParentProjectCandidatesModel]]
    """

    return sync_detailed(
        client=client,
        filters=filters,
        of=of,
        sort_by=sort_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
    of: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, ListAvailableParentProjectCandidatesModel]]:
    """List available parent project candidates

     Lists projects which can become parent to another project. Only sound candidates are returned.
    For instance a project cannot become parent of itself or it's children.

    To specify the project for which a parent is queried for, the `of` parameter can be provided. If no
    `of`
    parameter is provided, a new project is assumed. Then, the check for the hierarchy is omitted as a
    new project cannot be
    part of a hierarchy yet.

    Candidates can be filtered. Most commonly one will want to filter by name or identifier.
    You can do this through the `filters` parameter which works just like the work package index.

    For instance to find all parent candidates with \"rollout\" in their name:

    ```
    ?filters=[{\"name_and_identifier\":{\"operator\":\"~\",\"values\":[\"rollout\"]}}]
    ```

    Args:
        filters (Union[Unset, None, str]):
        of (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListAvailableParentProjectCandidatesModel]]
    """

    kwargs = _get_kwargs(
        client=client,
        filters=filters,
        of=of,
        sort_by=sort_by,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    filters: Union[Unset, None, str] = UNSET,
    of: Union[Unset, None, str] = UNSET,
    sort_by: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, ListAvailableParentProjectCandidatesModel]]:
    """List available parent project candidates

     Lists projects which can become parent to another project. Only sound candidates are returned.
    For instance a project cannot become parent of itself or it's children.

    To specify the project for which a parent is queried for, the `of` parameter can be provided. If no
    `of`
    parameter is provided, a new project is assumed. Then, the check for the hierarchy is omitted as a
    new project cannot be
    part of a hierarchy yet.

    Candidates can be filtered. Most commonly one will want to filter by name or identifier.
    You can do this through the `filters` parameter which works just like the work package index.

    For instance to find all parent candidates with \"rollout\" in their name:

    ```
    ?filters=[{\"name_and_identifier\":{\"operator\":\"~\",\"values\":[\"rollout\"]}}]
    ```

    Args:
        filters (Union[Unset, None, str]):
        of (Union[Unset, None, str]):
        sort_by (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListAvailableParentProjectCandidatesModel]]
    """

    return (
        await asyncio_detailed(
            client=client,
            filters=filters,
            of=of,
            sort_by=sort_by,
        )
    ).parsed
