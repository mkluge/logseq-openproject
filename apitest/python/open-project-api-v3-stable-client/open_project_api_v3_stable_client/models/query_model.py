import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_filter_instance_schema_model import QueryFilterInstanceSchemaModel
    from ..models.query_model_links import QueryModelLinks


T = TypeVar("T", bound="QueryModel")


@attr.s(auto_attribs=True)
class QueryModel:
    """
    Attributes:
        created_at (datetime.datetime): Time of creation
        updated_at (datetime.datetime): Time of the most recent change to the query
        id (Union[Unset, int]): Query id
        name (Union[Unset, str]): Query name
        filters (Union[Unset, List['QueryFilterInstanceSchemaModel']]): A set of QueryFilters which will be applied to
            the work packages to determine the resulting work packages
        sums (Union[Unset, bool]): Should sums (of supported properties) be shown?
        timeline_visible (Union[Unset, bool]): Should the timeline mode be shown?
        timeline_labels (Union[Unset, List[str]]): Which labels are shown in the timeline, empty when default
        timeline_zoom_level (Union[Unset, str]): Which zoom level should the timeline be rendered in?
        highlighting_mode (Union[Unset, str]): Which highlighting mode should the table have?
        show_hierarchies (Union[Unset, bool]): Should the hierarchy mode be enabled?
        hidden (Union[Unset, bool]): Should the query be hidden from the query list?
        public (Union[Unset, bool]): Can users besides the owner see the query?
        starred (Union[Unset, bool]): Should the query be highlighted to the user?
        field_links (Union[Unset, QueryModelLinks]):
    """

    created_at: datetime.datetime
    updated_at: datetime.datetime
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    filters: Union[Unset, List["QueryFilterInstanceSchemaModel"]] = UNSET
    sums: Union[Unset, bool] = UNSET
    timeline_visible: Union[Unset, bool] = UNSET
    timeline_labels: Union[Unset, List[str]] = UNSET
    timeline_zoom_level: Union[Unset, str] = UNSET
    highlighting_mode: Union[Unset, str] = UNSET
    show_hierarchies: Union[Unset, bool] = UNSET
    hidden: Union[Unset, bool] = UNSET
    public: Union[Unset, bool] = UNSET
    starred: Union[Unset, bool] = UNSET
    field_links: Union[Unset, "QueryModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        id = self.id
        name = self.name
        filters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()

                filters.append(filters_item)

        sums = self.sums
        timeline_visible = self.timeline_visible
        timeline_labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.timeline_labels, Unset):
            timeline_labels = self.timeline_labels

        timeline_zoom_level = self.timeline_zoom_level
        highlighting_mode = self.highlighting_mode
        show_hierarchies = self.show_hierarchies
        hidden = self.hidden
        public = self.public
        starred = self.starred
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if filters is not UNSET:
            field_dict["filters"] = filters
        if sums is not UNSET:
            field_dict["sums"] = sums
        if timeline_visible is not UNSET:
            field_dict["timelineVisible"] = timeline_visible
        if timeline_labels is not UNSET:
            field_dict["timelineLabels"] = timeline_labels
        if timeline_zoom_level is not UNSET:
            field_dict["timelineZoomLevel"] = timeline_zoom_level
        if highlighting_mode is not UNSET:
            field_dict["highlightingMode"] = highlighting_mode
        if show_hierarchies is not UNSET:
            field_dict["showHierarchies"] = show_hierarchies
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if public is not UNSET:
            field_dict["public"] = public
        if starred is not UNSET:
            field_dict["starred"] = starred
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_filter_instance_schema_model import QueryFilterInstanceSchemaModel
        from ..models.query_model_links import QueryModelLinks

        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        filters = []
        _filters = d.pop("filters", UNSET)
        for filters_item_data in _filters or []:
            filters_item = QueryFilterInstanceSchemaModel.from_dict(filters_item_data)

            filters.append(filters_item)

        sums = d.pop("sums", UNSET)

        timeline_visible = d.pop("timelineVisible", UNSET)

        timeline_labels = cast(List[str], d.pop("timelineLabels", UNSET))

        timeline_zoom_level = d.pop("timelineZoomLevel", UNSET)

        highlighting_mode = d.pop("highlightingMode", UNSET)

        show_hierarchies = d.pop("showHierarchies", UNSET)

        hidden = d.pop("hidden", UNSET)

        public = d.pop("public", UNSET)

        starred = d.pop("starred", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, QueryModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = QueryModelLinks.from_dict(_field_links)

        query_model = cls(
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            name=name,
            filters=filters,
            sums=sums,
            timeline_visible=timeline_visible,
            timeline_labels=timeline_labels,
            timeline_zoom_level=timeline_zoom_level,
            highlighting_mode=highlighting_mode,
            show_hierarchies=show_hierarchies,
            hidden=hidden,
            public=public,
            starred=starred,
            field_links=field_links,
        )

        query_model.additional_properties = d
        return query_model

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
