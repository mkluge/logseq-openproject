from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_model_links import PostModelLinks


T = TypeVar("T", bound="PostModel")


@attr.s(auto_attribs=True)
class PostModel:
    """
    Example:
        {'_type': 'Post', 'id': 1, 'subject': 'A post with a subject', '_embedded': {'project': {'_type':
            'Project...'}}, '_links': {'self': {'href': '/api/v3/posts/1'}, 'attachments': {'href':
            '/api/v3/posts/1/attachments'}, 'addAttachment': {'href': '/api/v3/posts/1/attachments', 'method': 'post'},
            'project': {'href': '/api/v3/projects/1', 'title': 'A project with a title'}}}

    Attributes:
        subject (str): The post's subject
        id (Union[Unset, int]): Identifier of this post
        field_links (Union[Unset, PostModelLinks]):
    """

    subject: str
    id: Union[Unset, int] = UNSET
    field_links: Union[Unset, "PostModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        id = self.id
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject": subject,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_model_links import PostModelLinks

        d = src_dict.copy()
        subject = d.pop("subject")

        id = d.pop("id", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, PostModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = PostModelLinks.from_dict(_field_links)

        post_model = cls(
            subject=subject,
            id=id,
            field_links=field_links,
        )

        post_model.additional_properties = d
        return post_model

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
