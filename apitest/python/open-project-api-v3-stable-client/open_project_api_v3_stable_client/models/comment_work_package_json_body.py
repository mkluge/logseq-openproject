from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_work_package_json_body_comment import CommentWorkPackageJsonBodyComment


T = TypeVar("T", bound="CommentWorkPackageJsonBody")


@attr.s(auto_attribs=True)
class CommentWorkPackageJsonBody:
    """
    Example:
        {'comment': {'raw': 'I think this is awesome!'}}

    Attributes:
        comment (Union[Unset, CommentWorkPackageJsonBodyComment]):
    """

    comment: Union[Unset, "CommentWorkPackageJsonBodyComment"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comment_work_package_json_body_comment import CommentWorkPackageJsonBodyComment

        d = src_dict.copy()
        _comment = d.pop("comment", UNSET)
        comment: Union[Unset, CommentWorkPackageJsonBodyComment]
        if isinstance(_comment, Unset):
            comment = UNSET
        else:
            comment = CommentWorkPackageJsonBodyComment.from_dict(_comment)

        comment_work_package_json_body = cls(
            comment=comment,
        )

        comment_work_package_json_body.additional_properties = d
        return comment_work_package_json_body

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
