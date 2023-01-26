import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.project_model_type import ProjectModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.formattable import Formattable
    from ..models.project_model_links import ProjectModelLinks
    from ..models.project_model_status_explanation import ProjectModelStatusExplanation


T = TypeVar("T", bound="ProjectModel")


@attr.s(auto_attribs=True)
class ProjectModel:
    """
    Attributes:
        field_type (Union[Unset, ProjectModelType]):
        id (Union[Unset, int]): Projects' id
        identifier (Union[Unset, str]):
        name (Union[Unset, str]):
        active (Union[Unset, bool]): Indicates whether the project is currently active or already archived
        status_explanation (Union[Unset, ProjectModelStatusExplanation]):
        public (Union[Unset, bool]): Indicates whether the project is accessible for everybody
        description (Union[Unset, Formattable]):  Example: {'format': 'markdown', 'raw': 'I am formatted!', 'html': 'I
            am formatted!'}.
        created_at (Union[Unset, datetime.datetime]): Time of creation
        updated_at (Union[Unset, datetime.datetime]): Time of the most recent change to the project
        field_links (Union[Unset, ProjectModelLinks]):
    """

    field_type: Union[Unset, ProjectModelType] = UNSET
    id: Union[Unset, int] = UNSET
    identifier: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    status_explanation: Union[Unset, "ProjectModelStatusExplanation"] = UNSET
    public: Union[Unset, bool] = UNSET
    description: Union[Unset, "Formattable"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    field_links: Union[Unset, "ProjectModelLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_type: Union[Unset, str] = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value

        id = self.id
        identifier = self.identifier
        name = self.name
        active = self.active
        status_explanation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status_explanation, Unset):
            status_explanation = self.status_explanation.to_dict()

        public = self.public
        description: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict()

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
        if field_type is not UNSET:
            field_dict["_type"] = field_type
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if active is not UNSET:
            field_dict["active"] = active
        if status_explanation is not UNSET:
            field_dict["statusExplanation"] = status_explanation
        if public is not UNSET:
            field_dict["public"] = public
        if description is not UNSET:
            field_dict["description"] = description
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.formattable import Formattable
        from ..models.project_model_links import ProjectModelLinks
        from ..models.project_model_status_explanation import ProjectModelStatusExplanation

        d = src_dict.copy()
        _field_type = d.pop("_type", UNSET)
        field_type: Union[Unset, ProjectModelType]
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = ProjectModelType(_field_type)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        active = d.pop("active", UNSET)

        _status_explanation = d.pop("statusExplanation", UNSET)
        status_explanation: Union[Unset, ProjectModelStatusExplanation]
        if isinstance(_status_explanation, Unset):
            status_explanation = UNSET
        else:
            status_explanation = ProjectModelStatusExplanation.from_dict(_status_explanation)

        public = d.pop("public", UNSET)

        _description = d.pop("description", UNSET)
        description: Union[Unset, Formattable]
        if isinstance(_description, Unset):
            description = UNSET
        else:
            description = Formattable.from_dict(_description)

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
        field_links: Union[Unset, ProjectModelLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = ProjectModelLinks.from_dict(_field_links)

        project_model = cls(
            field_type=field_type,
            id=id,
            identifier=identifier,
            name=name,
            active=active,
            status_explanation=status_explanation,
            public=public,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            field_links=field_links,
        )

        project_model.additional_properties = d
        return project_model

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
