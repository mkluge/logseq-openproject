from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_model_groups import CollectionModelGroups
    from ..models.collection_model_total_sums import CollectionModelTotalSums
    from ..models.file_link_collection_read_model_embedded import FileLinkCollectionReadModelEmbedded
    from ..models.file_link_collection_read_model_links import FileLinkCollectionReadModelLinks


T = TypeVar("T", bound="FileLinkCollectionReadModel")


@attr.s(auto_attribs=True)
class FileLinkCollectionReadModel:
    """
    Example:
        {'_type': 'Collection', 'total': 2, 'count': 2, '_links': {'self': {'href':
            '/api/v3/work_packages/42/file_links'}}, '_embedded': {'elements': [{'id': 1337, '_type': 'FileLink',
            'createdAt': '2021-12-20T13:37:00.211Z', 'updatedAt': '2021-12-20T13:37:00.211Z', 'originData': {'id': 5503,
            'name': 'logo.png', 'mimeType': 'image/png', 'size': 16042, 'createdAt': '2021-12-19T09:42:10.170Z',
            'lastModifiedAt': '2021-12-20T14:00:13.987Z', 'createdByName': 'Luke Skywalker', 'lastModifiedByName': 'Anakin
            Skywalker'}, '_links': {'self': {'href': '/api/v3/work_package/17/file_links/1337', 'title': 'file link'},
            'storage': {'href': '/api/v3/storage/42', 'title': 'storage'}, 'container': {'href': '/api/v3/work_package/17',
            'title': 'work package'}, 'creator': {'href': '/api/v3/users/33', 'title': 'Obi-Wan Kenobi'}, 'delete': {'href':
            '/api/v3/work_package/17/file_links/1337', 'method': 'delete'}, 'originOpen': {'href':
            'https://nextcloud.deathstar.rocks/index.php/f?fileid=5503'}, 'staticOriginOpen': {'href':
            '/api/v3/work_package/17/file_links/1337/open'}}}, {'_hint': 'File Link resource shortened for brevity', 'id':
            1338}]}}

    Attributes:
        field_links (FileLinkCollectionReadModelLinks):
        field_embedded (FileLinkCollectionReadModelEmbedded):
        total (Union[Unset, int]): The total amount of elements available in the collection
        page_size (Union[Unset, int]): Amount of elements that a response will hold
        count (Union[Unset, int]): Actual amount of elements in this response
        offset (Union[Unset, int]): The page number that is requested from paginated collection
        groups (Union[Unset, CollectionModelGroups]): Summarized information about aggregation groups
        total_sums (Union[Unset, CollectionModelTotalSums]): Aggregations of supported values for elements of the
            collection
    """

    field_links: "FileLinkCollectionReadModelLinks"
    field_embedded: "FileLinkCollectionReadModelEmbedded"
    total: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET
    offset: Union[Unset, int] = UNSET
    groups: Union[Unset, "CollectionModelGroups"] = UNSET
    total_sums: Union[Unset, "CollectionModelTotalSums"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_links = self.field_links.to_dict()

        field_embedded = self.field_embedded.to_dict()

        total = self.total
        page_size = self.page_size
        count = self.count
        offset = self.offset
        groups: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict()

        total_sums: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.total_sums, Unset):
            total_sums = self.total_sums.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_links": field_links,
                "_embedded": field_embedded,
            }
        )
        if total is not UNSET:
            field_dict["total"] = total
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if count is not UNSET:
            field_dict["count"] = count
        if offset is not UNSET:
            field_dict["offset"] = offset
        if groups is not UNSET:
            field_dict["groups"] = groups
        if total_sums is not UNSET:
            field_dict["totalSums"] = total_sums

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.collection_model_groups import CollectionModelGroups
        from ..models.collection_model_total_sums import CollectionModelTotalSums
        from ..models.file_link_collection_read_model_embedded import FileLinkCollectionReadModelEmbedded
        from ..models.file_link_collection_read_model_links import FileLinkCollectionReadModelLinks

        d = src_dict.copy()
        field_links = FileLinkCollectionReadModelLinks.from_dict(d.pop("_links"))

        field_embedded = FileLinkCollectionReadModelEmbedded.from_dict(d.pop("_embedded"))

        total = d.pop("total", UNSET)

        page_size = d.pop("pageSize", UNSET)

        count = d.pop("count", UNSET)

        offset = d.pop("offset", UNSET)

        _groups = d.pop("groups", UNSET)
        groups: Union[Unset, CollectionModelGroups]
        if isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = CollectionModelGroups.from_dict(_groups)

        _total_sums = d.pop("totalSums", UNSET)
        total_sums: Union[Unset, CollectionModelTotalSums]
        if isinstance(_total_sums, Unset):
            total_sums = UNSET
        else:
            total_sums = CollectionModelTotalSums.from_dict(_total_sums)

        file_link_collection_read_model = cls(
            field_links=field_links,
            field_embedded=field_embedded,
            total=total,
            page_size=page_size,
            count=count,
            offset=offset,
            groups=groups,
            total_sums=total_sums,
        )

        file_link_collection_read_model.additional_properties = d
        return file_link_collection_read_model

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
