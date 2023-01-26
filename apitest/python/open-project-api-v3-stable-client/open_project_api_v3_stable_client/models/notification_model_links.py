from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_model_links_activity import NotificationModelLinksActivity
    from ..models.notification_model_links_actor import NotificationModelLinksActor
    from ..models.notification_model_links_details_item import NotificationModelLinksDetailsItem
    from ..models.notification_model_links_project import NotificationModelLinksProject
    from ..models.notification_model_links_read_ian import NotificationModelLinksReadIAN
    from ..models.notification_model_links_resource import NotificationModelLinksResource
    from ..models.notification_model_links_self import NotificationModelLinksSelf
    from ..models.notification_model_links_unread_ian import NotificationModelLinksUnreadIAN


T = TypeVar("T", bound="NotificationModelLinks")


@attr.s(auto_attribs=True)
class NotificationModelLinks:
    """
    Attributes:
        self_ (NotificationModelLinksSelf):
        project (NotificationModelLinksProject):
        actor (NotificationModelLinksActor):
        resource (NotificationModelLinksResource):
        activity (NotificationModelLinksActivity):
        details (List['NotificationModelLinksDetailsItem']):
        read_ian (Union[Unset, NotificationModelLinksReadIAN]):
        unread_ian (Union[Unset, NotificationModelLinksUnreadIAN]):
    """

    self_: "NotificationModelLinksSelf"
    project: "NotificationModelLinksProject"
    actor: "NotificationModelLinksActor"
    resource: "NotificationModelLinksResource"
    activity: "NotificationModelLinksActivity"
    details: List["NotificationModelLinksDetailsItem"]
    read_ian: Union[Unset, "NotificationModelLinksReadIAN"] = UNSET
    unread_ian: Union[Unset, "NotificationModelLinksUnreadIAN"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_.to_dict()

        project = self.project.to_dict()

        actor = self.actor.to_dict()

        resource = self.resource.to_dict()

        activity = self.activity.to_dict()

        details = []
        for details_item_data in self.details:
            details_item = details_item_data.to_dict()

            details.append(details_item)

        read_ian: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.read_ian, Unset):
            read_ian = self.read_ian.to_dict()

        unread_ian: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unread_ian, Unset):
            unread_ian = self.unread_ian.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "project": project,
                "actor": actor,
                "resource": resource,
                "activity": activity,
                "details": details,
            }
        )
        if read_ian is not UNSET:
            field_dict["readIAN"] = read_ian
        if unread_ian is not UNSET:
            field_dict["unreadIAN"] = unread_ian

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notification_model_links_activity import NotificationModelLinksActivity
        from ..models.notification_model_links_actor import NotificationModelLinksActor
        from ..models.notification_model_links_details_item import NotificationModelLinksDetailsItem
        from ..models.notification_model_links_project import NotificationModelLinksProject
        from ..models.notification_model_links_read_ian import NotificationModelLinksReadIAN
        from ..models.notification_model_links_resource import NotificationModelLinksResource
        from ..models.notification_model_links_self import NotificationModelLinksSelf
        from ..models.notification_model_links_unread_ian import NotificationModelLinksUnreadIAN

        d = src_dict.copy()
        self_ = NotificationModelLinksSelf.from_dict(d.pop("self"))

        project = NotificationModelLinksProject.from_dict(d.pop("project"))

        actor = NotificationModelLinksActor.from_dict(d.pop("actor"))

        resource = NotificationModelLinksResource.from_dict(d.pop("resource"))

        activity = NotificationModelLinksActivity.from_dict(d.pop("activity"))

        details = []
        _details = d.pop("details")
        for details_item_data in _details:
            details_item = NotificationModelLinksDetailsItem.from_dict(details_item_data)

            details.append(details_item)

        _read_ian = d.pop("readIAN", UNSET)
        read_ian: Union[Unset, NotificationModelLinksReadIAN]
        if isinstance(_read_ian, Unset):
            read_ian = UNSET
        else:
            read_ian = NotificationModelLinksReadIAN.from_dict(_read_ian)

        _unread_ian = d.pop("unreadIAN", UNSET)
        unread_ian: Union[Unset, NotificationModelLinksUnreadIAN]
        if isinstance(_unread_ian, Unset):
            unread_ian = UNSET
        else:
            unread_ian = NotificationModelLinksUnreadIAN.from_dict(_unread_ian)

        notification_model_links = cls(
            self_=self_,
            project=project,
            actor=actor,
            resource=resource,
            activity=activity,
            details=details,
            read_ian=read_ian,
            unread_ian=unread_ian,
        )

        notification_model_links.additional_properties = d
        return notification_model_links

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
