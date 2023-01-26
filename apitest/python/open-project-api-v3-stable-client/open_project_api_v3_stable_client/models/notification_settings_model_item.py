from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.notification_settings_model_item_due_date import NotificationSettingsModelItemDueDate
from ..models.notification_settings_model_item_overdue import NotificationSettingsModelItemOverdue
from ..models.notification_settings_model_item_start_date import NotificationSettingsModelItemStartDate
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_settings_model_item_links import NotificationSettingsModelItemLinks


T = TypeVar("T", bound="NotificationSettingsModelItem")


@attr.s(auto_attribs=True)
class NotificationSettingsModelItem:
    """
    Attributes:
        document_added (bool):
        forum_messages (bool):
        involved (bool):
        membership_added (bool):
        membership_updated (bool):
        mentioned (bool):
        news_added (bool):
        news_commented (bool):
        watched (bool):
        work_package_created (bool):
        work_package_commented (bool):
        work_package_processed (bool):
        work_package_prioritized (bool):
        work_package_scheduled (bool):
        wiki_page_added (bool):
        wiki_page_updated (bool):
        field_links (NotificationSettingsModelItemLinks):
        overdue (Union[Unset, NotificationSettingsModelItemOverdue]): Sets an overdue notification for work packages. It
            is null when no notification is set,
            otherwise it holds an ISO8601 formatted duration string with the possible values listed below.
            The possible values are: none, every day, every 3 days, every week.
        start_date (Union[Unset, NotificationSettingsModelItemStartDate]): Sets a startDate notification for work
            packages. It is null when no notification is set,
            otherwise it holds an ISO8601 formatted duration string with the possible values listed below.
            The possible values are: none, same day, 1 day before, 3 days before, 1 week before.
        due_date (Union[Unset, NotificationSettingsModelItemDueDate]): Sets a dueDate notification for work packages. It
            is null when no notification is set,
            otherwise it holds an ISO8601 formatted duration string with the possible values listed below.
            The possible values are: none, same day, 1 day before, 3 days before, 1 week before.
    """

    document_added: bool
    forum_messages: bool
    involved: bool
    membership_added: bool
    membership_updated: bool
    mentioned: bool
    news_added: bool
    news_commented: bool
    watched: bool
    work_package_created: bool
    work_package_commented: bool
    work_package_processed: bool
    work_package_prioritized: bool
    work_package_scheduled: bool
    wiki_page_added: bool
    wiki_page_updated: bool
    field_links: "NotificationSettingsModelItemLinks"
    overdue: Union[Unset, NotificationSettingsModelItemOverdue] = UNSET
    start_date: Union[Unset, NotificationSettingsModelItemStartDate] = UNSET
    due_date: Union[Unset, NotificationSettingsModelItemDueDate] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_added = self.document_added
        forum_messages = self.forum_messages
        involved = self.involved
        membership_added = self.membership_added
        membership_updated = self.membership_updated
        mentioned = self.mentioned
        news_added = self.news_added
        news_commented = self.news_commented
        watched = self.watched
        work_package_created = self.work_package_created
        work_package_commented = self.work_package_commented
        work_package_processed = self.work_package_processed
        work_package_prioritized = self.work_package_prioritized
        work_package_scheduled = self.work_package_scheduled
        wiki_page_added = self.wiki_page_added
        wiki_page_updated = self.wiki_page_updated
        field_links = self.field_links.to_dict()

        overdue: Union[Unset, str] = UNSET
        if not isinstance(self.overdue, Unset):
            overdue = self.overdue.value

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.value

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentAdded": document_added,
                "forumMessages": forum_messages,
                "involved": involved,
                "membershipAdded": membership_added,
                "membershipUpdated": membership_updated,
                "mentioned": mentioned,
                "newsAdded": news_added,
                "newsCommented": news_commented,
                "watched": watched,
                "workPackageCreated": work_package_created,
                "workPackageCommented": work_package_commented,
                "workPackageProcessed": work_package_processed,
                "workPackagePrioritized": work_package_prioritized,
                "workPackageScheduled": work_package_scheduled,
                "wikiPageAdded": wiki_page_added,
                "wikiPageUpdated": wiki_page_updated,
                "_links": field_links,
            }
        )
        if overdue is not UNSET:
            field_dict["overdue"] = overdue
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.notification_settings_model_item_links import NotificationSettingsModelItemLinks

        d = src_dict.copy()
        document_added = d.pop("documentAdded")

        forum_messages = d.pop("forumMessages")

        involved = d.pop("involved")

        membership_added = d.pop("membershipAdded")

        membership_updated = d.pop("membershipUpdated")

        mentioned = d.pop("mentioned")

        news_added = d.pop("newsAdded")

        news_commented = d.pop("newsCommented")

        watched = d.pop("watched")

        work_package_created = d.pop("workPackageCreated")

        work_package_commented = d.pop("workPackageCommented")

        work_package_processed = d.pop("workPackageProcessed")

        work_package_prioritized = d.pop("workPackagePrioritized")

        work_package_scheduled = d.pop("workPackageScheduled")

        wiki_page_added = d.pop("wikiPageAdded")

        wiki_page_updated = d.pop("wikiPageUpdated")

        field_links = NotificationSettingsModelItemLinks.from_dict(d.pop("_links"))

        _overdue = d.pop("overdue", UNSET)
        overdue: Union[Unset, NotificationSettingsModelItemOverdue]
        if isinstance(_overdue, Unset):
            overdue = UNSET
        else:
            overdue = NotificationSettingsModelItemOverdue(_overdue)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, NotificationSettingsModelItemStartDate]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = NotificationSettingsModelItemStartDate(_start_date)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, NotificationSettingsModelItemDueDate]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = NotificationSettingsModelItemDueDate(_due_date)

        notification_settings_model_item = cls(
            document_added=document_added,
            forum_messages=forum_messages,
            involved=involved,
            membership_added=membership_added,
            membership_updated=membership_updated,
            mentioned=mentioned,
            news_added=news_added,
            news_commented=news_commented,
            watched=watched,
            work_package_created=work_package_created,
            work_package_commented=work_package_commented,
            work_package_processed=work_package_processed,
            work_package_prioritized=work_package_prioritized,
            work_package_scheduled=work_package_scheduled,
            wiki_page_added=wiki_page_added,
            wiki_page_updated=wiki_page_updated,
            field_links=field_links,
            overdue=overdue,
            start_date=start_date,
            due_date=due_date,
        )

        notification_settings_model_item.additional_properties = d
        return notification_settings_model_item

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
