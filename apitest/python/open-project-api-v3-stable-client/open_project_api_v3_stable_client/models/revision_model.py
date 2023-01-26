import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.revision_model_links import RevisionModelLinks
    from ..models.revision_model_message import RevisionModelMessage


T = TypeVar("T", bound="RevisionModel")


@attr.s(auto_attribs=True)
class RevisionModel:
    """
    Example:
        {'_type': 'Revision', '_links': {'self': {'href': '/api/v3/revisions/1'}, 'project': {'href':
            '/api/v3/projects/1'}, 'author': {'href': '/api/v3/users/1'}, 'showRevision': {'href':
            '/projects/identifier/repository/revision/11f4b07'}}, 'id': 1, 'identifier':
            '11f4b07dff4f4ce9548a52b7d002daca7cd63ec6', 'formattedIdentifier': '11f4b07', 'authorName': 'Some Developer',
            'message': {'format': 'plain', 'raw': 'This revision provides new features\n\nAn elaborate description', 'html':
            '<p>This revision provides new features<br/><br/>An elaborate description</p>'}, 'createdAt':
            '2015-07-21T13:36:59Z'}

    Attributes:
        identifier (str): The raw SCM identifier of the revision (e.g. full SHA hash)
        formatted_identifier (str): The SCM identifier of the revision, formatted (e.g. shortened unambiguous SHA hash).
            May be identical to identifier in many cases
        author_name (str): The name of the author that committed this revision. Note that this name is retrieved from
            the repository and does not identify a user in OpenProject.
        message (RevisionModelMessage):
        created_at (datetime.datetime): The time this revision was committed to the repository
        id (Union[Unset, int]): Revision's id, assigned by OpenProject
        field_links (Union[Unset, RevisionModelLinks]):
    """

    identifier: str
    formatted_identifier: str
    author_name: str
    message: "RevisionModelMessage"
    created_at: datetime.datetime
    id: Union[Unset, int] = UNSET
    field_links: Union[Unset, "RevisionModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier
        formatted_identifier = self.formatted_identifier
        author_name = self.author_name
        message = self.message.to_dict()

        created_at = self.created_at.isoformat()

        id = self.id
        field_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "formattedIdentifier": formatted_identifier,
                "authorName": author_name,
                "message": message,
                "createdAt": created_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.revision_model_links import RevisionModelLinks
        from ..models.revision_model_message import RevisionModelMessage

        d = src_dict.copy()
        identifier = d.pop("identifier")

        formatted_identifier = d.pop("formattedIdentifier")

        author_name = d.pop("authorName")

        message = RevisionModelMessage.from_dict(d.pop("message"))

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, RevisionModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RevisionModelLinks.from_dict(_field_links)

        revision_model = cls(
            identifier=identifier,
            formatted_identifier=formatted_identifier,
            author_name=author_name,
            message=message,
            created_at=created_at,
            id=id,
            field_links=field_links,
        )

        revision_model.additional_properties = d
        return revision_model

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
