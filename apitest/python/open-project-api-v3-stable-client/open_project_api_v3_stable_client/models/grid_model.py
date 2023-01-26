import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grid_model_links import GridModelLinks
    from ..models.grid_model_widgets_item import GridModelWidgetsItem


T = TypeVar("T", bound="GridModel")


@attr.s(auto_attribs=True)
class GridModel:
    """
    Example:
        {'_type': 'Grid', 'id': 2, 'rowCount': 8, 'columnCount': 5, 'widgets': [{'_type': 'GridWidget', 'identifier':
            'time_entries_current_user', 'startRow': 1, 'endRow': 8, 'startColumn': 1, 'endColumn': 3}, {'_type':
            'GridWidget', 'identifier': 'news', 'startRow': 3, 'endRow': 8, 'startColumn': 4, 'endColumn': 5}, {'_type':
            'GridWidget', 'identifier': 'documents', 'startRow': 1, 'endRow': 3, 'startColumn': 3, 'endColumn': 6}],
            'createdAt': '2018-12-03T16:58:30Z', 'updatedAt': '2018-12-13T19:36:40Z', '_links': {'scope': {'href':
            '/my/page', 'type': 'text/html'}, 'updateImmediately': {'href': '/api/v3/grids/2', 'method': 'patch'}, 'update':
            {'href': '/api/v3/grids/2/form', 'method': 'post'}, 'self': {'href': '/api/v3/grids/2'}}}

    Attributes:
        id (Union[Unset, int]): Grid's id
        row_count (Union[Unset, int]): The number of rows the grid has
        column_count (Union[Unset, int]): The number of columns the grid has
        widgets (Union[Unset, List['GridModelWidgetsItem']]): The set of `GridWidget`s selected for the grid

            # Conditions

            The widgets cannot overlap
        created_at (Union[Unset, datetime.datetime]): The time the grid was created
        updated_at (Union[Unset, datetime.datetime]): The time the grid was last updated
        field_links (Union[Unset, GridModelLinks]):
    """

    id: Union[Unset, int] = UNSET
    row_count: Union[Unset, int] = UNSET
    column_count: Union[Unset, int] = UNSET
    widgets: Union[Unset, List["GridModelWidgetsItem"]] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    field_links: Union[Unset, "GridModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        row_count = self.row_count
        column_count = self.column_count
        widgets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.widgets, Unset):
            widgets = []
            for widgets_item_data in self.widgets:
                widgets_item = widgets_item_data.to_dict()

                widgets.append(widgets_item)

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if row_count is not UNSET:
            field_dict["rowCount"] = row_count
        if column_count is not UNSET:
            field_dict["columnCount"] = column_count
        if widgets is not UNSET:
            field_dict["widgets"] = widgets
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.grid_model_links import GridModelLinks
        from ..models.grid_model_widgets_item import GridModelWidgetsItem

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        row_count = d.pop("rowCount", UNSET)

        column_count = d.pop("columnCount", UNSET)

        widgets = []
        _widgets = d.pop("widgets", UNSET)
        for widgets_item_data in _widgets or []:
            widgets_item = GridModelWidgetsItem.from_dict(widgets_item_data)

            widgets.append(widgets_item)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, GridModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = GridModelLinks.from_dict(_field_links)

        grid_model = cls(
            id=id,
            row_count=row_count,
            column_count=column_count,
            widgets=widgets,
            created_at=created_at,
            updated_at=updated_at,
            field_links=field_links,
        )

        grid_model.additional_properties = d
        return grid_model

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
