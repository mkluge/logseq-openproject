import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_model_comment import ActivityModelComment
    from ..models.formattable import Formattable


T = TypeVar("T", bound="ActivityModel")


@attr.s(auto_attribs=True)
class ActivityModel:
    """
    Example:
        {'_type': 'Activity::Comment', '_links': {'self': {'href': '/api/v3/activity/1', 'title': 'Priority changed from
            High to Low'}, 'workPackage': {'href': '/api/v3/work_packages/1', 'title': 'quis numquam qui voluptatum quia
            praesentium blanditiis nisi'}, 'user': {'href': '/api/v3/users/1', 'title': 'John Sheppard - admin'}}, 'id': 1,
            'details': [{'format': 'markdown', 'raw': 'Lorem ipsum dolor sit amet.', 'html': '<p>Lorem ipsum dolor sit
            amet.</p>'}], 'comment': {'format': 'markdown', 'raw': 'Lorem ipsum dolor sit amet.', 'html': '<p>Lorem ipsum
            dolor sit amet.</p>'}, 'createdAt': '2014-05-21T08:51:20Z', 'updatedAt': '2014-05-21T09:14:02Z', 'version': 31}

    Attributes:
        id (Union[Unset, int]): Activity id
        version (Union[Unset, int]): Activity version
        comment (Union[Unset, ActivityModelComment]):
        details (Union[Unset, List['Formattable']]):
        created_at (Union[Unset, datetime.datetime]): Time of creation
        updated_at (Union[Unset, datetime.datetime]): Time of update
    """

    id: Union[Unset, int] = UNSET
    version: Union[Unset, int] = UNSET
    comment: Union[Unset, "ActivityModelComment"] = UNSET
    details: Union[Unset, List["Formattable"]] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        version = self.version
        comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()

                details.append(details_item)

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if version is not UNSET:
            field_dict["version"] = version
        if comment is not UNSET:
            field_dict["comment"] = comment
        if details is not UNSET:
            field_dict["details"] = details
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.activity_model_comment import ActivityModelComment
        from ..models.formattable import Formattable

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        version = d.pop("version", UNSET)

        _comment = d.pop("comment", UNSET)
        comment: Union[Unset, ActivityModelComment]
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = ActivityModelComment.from_dict(_comment)

        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = Formattable.from_dict(details_item_data)

            details.append(details_item)

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

        activity_model = cls(
            id=id,
            version=version,
            comment=comment,
            details=details,
            created_at=created_at,
            updated_at=updated_at,
        )

        activity_model.additional_properties = d
        return activity_model

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
