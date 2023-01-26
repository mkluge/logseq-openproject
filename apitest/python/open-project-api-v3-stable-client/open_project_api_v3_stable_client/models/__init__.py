""" Contains all the data models used in inputs/outputs """

from .activity_model import ActivityModel
from .activity_model_comment import ActivityModelComment
from .add_watcher_json_body import AddWatcherJsonBody
from .add_watcher_json_body_user import AddWatcherJsonBodyUser
from .attachment_model import AttachmentModel
from .attachment_model_description import AttachmentModelDescription
from .attachment_model_links import AttachmentModelLinks
from .attachment_model_links_author import AttachmentModelLinksAuthor
from .attachment_model_links_container import AttachmentModelLinksContainer
from .attachment_model_links_delete import AttachmentModelLinksDelete
from .attachment_model_links_download_location import AttachmentModelLinksDownloadLocation
from .attachment_model_links_self import AttachmentModelLinksSelf
from .attachments_model import AttachmentsModel
from .attachments_model_embedded import AttachmentsModelEmbedded
from .attachments_model_embedded_elements_item import AttachmentsModelEmbeddedElementsItem
from .attachments_model_links import AttachmentsModelLinks
from .attachments_model_links_self import AttachmentsModelLinksSelf
from .available_assignees_model import AvailableAssigneesModel
from .available_projects_for_memberships_model import AvailableProjectsForMembershipsModel
from .available_projects_for_query_model import AvailableProjectsForQueryModel
from .available_projects_for_time_entries_model import AvailableProjectsForTimeEntriesModel
from .available_projects_for_versions_model import AvailableProjectsForVersionsModel
from .available_projects_for_work_package_model import AvailableProjectsForWorkPackageModel
from .available_relation_candidates_model import AvailableRelationCandidatesModel
from .available_responsibles_model import AvailableResponsiblesModel
from .available_watchers_model import AvailableWatchersModel
from .budget_model import BudgetModel
from .budget_model_links import BudgetModelLinks
from .budget_model_links_self import BudgetModelLinksSelf
from .budgets_by_project_model import BudgetsByProjectModel
from .categories_by_project_model import CategoriesByProjectModel
from .category_model import CategoryModel
from .category_model_links import CategoryModelLinks
from .category_model_links_default_assignee import CategoryModelLinksDefaultAssignee
from .category_model_links_project import CategoryModelLinksProject
from .category_model_links_self import CategoryModelLinksSelf
from .collection_model import CollectionModel
from .collection_model_groups import CollectionModelGroups
from .collection_model_total_sums import CollectionModelTotalSums
from .comment_work_package_json_body import CommentWorkPackageJsonBody
from .comment_work_package_json_body_comment import CommentWorkPackageJsonBodyComment
from .configuration_model import ConfigurationModel
from .create_group_json_body import CreateGroupJsonBody
from .create_group_json_body_links import CreateGroupJsonBodyLinks
from .create_group_json_body_links_members_item import CreateGroupJsonBodyLinksMembersItem
from .create_project_json_body import CreateProjectJsonBody
from .create_views_json_body import CreateViewsJsonBody
from .create_views_json_body_links import CreateViewsJsonBodyLinks
from .create_views_json_body_links_query import CreateViewsJsonBodyLinksQuery
from .create_views_response_201 import CreateViewsResponse201
from .custom_action_model import CustomActionModel
from .custom_option_model import CustomOptionModel
from .custom_option_model_links import CustomOptionModelLinks
from .custom_option_model_links_self import CustomOptionModelLinksSelf
from .customaction_model import CustomactionModel
from .customaction_model_links import CustomactionModelLinks
from .customaction_model_links_execute_immediately import CustomactionModelLinksExecuteImmediately
from .day_collection_model import DayCollectionModel
from .day_collection_model_embedded import DayCollectionModelEmbedded
from .day_collection_model_links import DayCollectionModelLinks
from .day_collection_model_links_self import DayCollectionModelLinksSelf
from .day_model import DayModel
from .day_model_links import DayModelLinks
from .day_model_links_week_day import DayModelLinksWeekDay
from .day_model_type import DayModelType
from .default_query_for_project_model import DefaultQueryForProjectModel
from .default_query_model import DefaultQueryModel
from .document_model import DocumentModel
from .document_model_links import DocumentModelLinks
from .document_model_links_attachments import DocumentModelLinksAttachments
from .document_model_links_project import DocumentModelLinksProject
from .document_model_links_self import DocumentModelLinksSelf
from .documents_model import DocumentsModel
from .edit_query_json_body import EditQueryJsonBody
from .error_response import ErrorResponse
from .error_response_embedded import ErrorResponseEmbedded
from .error_response_embedded_details import ErrorResponseEmbeddedDetails
from .error_response_type import ErrorResponseType
from .example_form_model import ExampleFormModel
from .example_schema_model import ExampleSchemaModel
from .execute_custom_action_json_body import ExecuteCustomActionJsonBody
from .execute_custom_action_json_body_links import ExecuteCustomActionJsonBodyLinks
from .execute_custom_action_json_body_links_work_package import ExecuteCustomActionJsonBodyLinksWorkPackage
from .file_collection_model import FileCollectionModel
from .file_collection_model_embedded import FileCollectionModelEmbedded
from .file_collection_model_links import FileCollectionModelLinks
from .file_collection_model_links_self import FileCollectionModelLinksSelf
from .file_link_collection_read_model import FileLinkCollectionReadModel
from .file_link_collection_read_model_embedded import FileLinkCollectionReadModelEmbedded
from .file_link_collection_read_model_links import FileLinkCollectionReadModelLinks
from .file_link_collection_read_model_links_self import FileLinkCollectionReadModelLinksSelf
from .file_link_collection_write_model import FileLinkCollectionWriteModel
from .file_link_collection_write_model_embedded import FileLinkCollectionWriteModelEmbedded
from .file_link_origin_data_model import FileLinkOriginDataModel
from .file_link_read_model import FileLinkReadModel
from .file_link_read_model_embedded import FileLinkReadModelEmbedded
from .file_link_read_model_links import FileLinkReadModelLinks
from .file_link_read_model_links_container import FileLinkReadModelLinksContainer
from .file_link_read_model_links_creator import FileLinkReadModelLinksCreator
from .file_link_read_model_links_delete import FileLinkReadModelLinksDelete
from .file_link_read_model_links_origin_open import FileLinkReadModelLinksOriginOpen
from .file_link_read_model_links_origin_open_location import FileLinkReadModelLinksOriginOpenLocation
from .file_link_read_model_links_permission import FileLinkReadModelLinksPermission
from .file_link_read_model_links_self import FileLinkReadModelLinksSelf
from .file_link_read_model_links_static_origin_download import FileLinkReadModelLinksStaticOriginDownload
from .file_link_read_model_links_static_origin_open import FileLinkReadModelLinksStaticOriginOpen
from .file_link_read_model_links_static_origin_open_location import FileLinkReadModelLinksStaticOriginOpenLocation
from .file_link_read_model_links_storage import FileLinkReadModelLinksStorage
from .file_link_read_model_type import FileLinkReadModelType
from .file_link_write_model import FileLinkWriteModel
from .file_link_write_model_links_type_0 import FileLinkWriteModelLinksType0
from .file_link_write_model_links_type_0_storage import FileLinkWriteModelLinksType0Storage
from .file_link_write_model_links_type_1 import FileLinkWriteModelLinksType1
from .file_link_write_model_links_type_1_storage_url import FileLinkWriteModelLinksType1StorageUrl
from .form_model import FormModel
from .form_model_links import FormModelLinks
from .form_model_links_commit import FormModelLinksCommit
from .form_model_links_preview_markup import FormModelLinksPreviewMarkup
from .form_model_links_self import FormModelLinksSelf
from .form_model_links_validate import FormModelLinksValidate
from .formattable import Formattable
from .formattable_format import FormattableFormat
from .grid_model import GridModel
from .grid_model_links import GridModelLinks
from .grid_model_links_page import GridModelLinksPage
from .grid_model_links_self import GridModelLinksSelf
from .grid_model_links_update import GridModelLinksUpdate
from .grid_model_links_update_immediately import GridModelLinksUpdateImmediately
from .grid_model_widgets_item import GridModelWidgetsItem
from .grid_update_form_response_200 import GridUpdateFormResponse200
from .grids_model import GridsModel
from .group_model import GroupModel
from .group_model_links import GroupModelLinks
from .group_model_links_delete import GroupModelLinksDelete
from .group_model_links_members import GroupModelLinksMembers
from .group_model_links_memberships import GroupModelLinksMemberships
from .group_model_links_self import GroupModelLinksSelf
from .group_model_links_update_immediately import GroupModelLinksUpdateImmediately
from .help_text_model import HelpTextModel
from .help_texts_model import HelpTextsModel
from .helptext_model import HelptextModel
from .helptext_model_help_text import HelptextModelHelpText
from .helptext_model_links import HelptextModelLinks
from .helptext_model_links_edit_text import HelptextModelLinksEditText
from .helptext_model_links_self import HelptextModelLinksSelf
from .link import Link
from .link_payload import LinkPayload
from .list_actions_model import ListActionsModel
from .list_available_parent_project_candidates_model import ListAvailableParentProjectCandidatesModel
from .list_capabilities_model import ListCapabilitiesModel
from .list_groups_model import ListGroupsModel
from .list_memberships_model import ListMembershipsModel
from .list_of_news_model import ListOfNewsModel
from .list_projects_by_version_model import ListProjectsByVersionModel
from .list_projects_model import ListProjectsModel
from .list_time_entries_model import ListTimeEntriesModel
from .membership_model import MembershipModel
from .membership_model_links import MembershipModelLinks
from .membership_model_links_principal import MembershipModelLinksPrincipal
from .membership_model_links_project import MembershipModelLinksProject
from .membership_model_links_roles import MembershipModelLinksRoles
from .membership_model_links_self import MembershipModelLinksSelf
from .news_model import NewsModel
from .news_model_links import NewsModelLinks
from .news_model_links_author import NewsModelLinksAuthor
from .news_model_links_project import NewsModelLinksProject
from .news_model_links_self import NewsModelLinksSelf
from .non_working_day_model import NonWorkingDayModel
from .non_working_day_model_links import NonWorkingDayModelLinks
from .non_working_day_model_links_self import NonWorkingDayModelLinksSelf
from .non_working_day_model_type import NonWorkingDayModelType
from .notification_collection_model import NotificationCollectionModel
from .notification_collection_model_embedded import NotificationCollectionModelEmbedded
from .notification_collection_model_links import NotificationCollectionModelLinks
from .notification_collection_model_links_change_size import NotificationCollectionModelLinksChangeSize
from .notification_collection_model_links_jump_to import NotificationCollectionModelLinksJumpTo
from .notification_collection_model_links_self import NotificationCollectionModelLinksSelf
from .notification_model import NotificationModel
from .notification_model_embedded import NotificationModelEmbedded
from .notification_model_links import NotificationModelLinks
from .notification_model_links_activity import NotificationModelLinksActivity
from .notification_model_links_actor import NotificationModelLinksActor
from .notification_model_links_details_item import NotificationModelLinksDetailsItem
from .notification_model_links_project import NotificationModelLinksProject
from .notification_model_links_read_ian import NotificationModelLinksReadIAN
from .notification_model_links_resource import NotificationModelLinksResource
from .notification_model_links_self import NotificationModelLinksSelf
from .notification_model_links_unread_ian import NotificationModelLinksUnreadIAN
from .notification_model_reason import NotificationModelReason
from .notification_model_type import NotificationModelType
from .notification_settings_model_item import NotificationSettingsModelItem
from .notification_settings_model_item_due_date import NotificationSettingsModelItemDueDate
from .notification_settings_model_item_links import NotificationSettingsModelItemLinks
from .notification_settings_model_item_links_project import NotificationSettingsModelItemLinksProject
from .notification_settings_model_item_overdue import NotificationSettingsModelItemOverdue
from .notification_settings_model_item_start_date import NotificationSettingsModelItemStartDate
from .post_model import PostModel
from .post_model_links import PostModelLinks
from .post_model_links_add_attachment import PostModelLinksAddAttachment
from .previewing_model import PreviewingModel
from .principal_model import PrincipalModel
from .principals_model import PrincipalsModel
from .priorities_model import PrioritiesModel
from .priority_model import PriorityModel
from .priority_model_links import PriorityModelLinks
from .priority_model_links_self import PriorityModelLinksSelf
from .project_create_form_json_body import ProjectCreateFormJsonBody
from .project_create_form_response_200 import ProjectCreateFormResponse200
from .project_model import ProjectModel
from .project_model_links import ProjectModelLinks
from .project_model_links_categories import ProjectModelLinksCategories
from .project_model_links_create_work_package import ProjectModelLinksCreateWorkPackage
from .project_model_links_create_work_package_immediately import ProjectModelLinksCreateWorkPackageImmediately
from .project_model_links_delete import ProjectModelLinksDelete
from .project_model_links_memberships import ProjectModelLinksMemberships
from .project_model_links_parent import ProjectModelLinksParent
from .project_model_links_self import ProjectModelLinksSelf
from .project_model_links_status import ProjectModelLinksStatus
from .project_model_links_storages_item import ProjectModelLinksStoragesItem
from .project_model_links_types import ProjectModelLinksTypes
from .project_model_links_update import ProjectModelLinksUpdate
from .project_model_links_update_immediately import ProjectModelLinksUpdateImmediately
from .project_model_links_versions import ProjectModelLinksVersions
from .project_model_links_work_packages import ProjectModelLinksWorkPackages
from .project_model_status_explanation import ProjectModelStatusExplanation
from .project_model_type import ProjectModelType
from .project_update_form_json_body import ProjectUpdateFormJsonBody
from .projects_schema_model import ProjectsSchemaModel
from .queries_model import QueriesModel
from .query_column_model import QueryColumnModel
from .query_filter_instance_schema_model import QueryFilterInstanceSchemaModel
from .query_filter_instance_schema_model_links import QueryFilterInstanceSchemaModelLinks
from .query_filter_instance_schema_model_links_filter import QueryFilterInstanceSchemaModelLinksFilter
from .query_filter_instance_schema_model_links_self import QueryFilterInstanceSchemaModelLinksSelf
from .query_filter_instance_schemas_for_project_model import QueryFilterInstanceSchemasForProjectModel
from .query_filter_instance_schemas_model import QueryFilterInstanceSchemasModel
from .query_filter_model import QueryFilterModel
from .query_model import QueryModel
from .query_model_links import QueryModelLinks
from .query_model_links_star import QueryModelLinksStar
from .query_model_links_unstar import QueryModelLinksUnstar
from .query_model_links_update import QueryModelLinksUpdate
from .query_model_links_update_immediately import QueryModelLinksUpdateImmediately
from .query_operator_model import QueryOperatorModel
from .query_sort_by_model import QuerySortByModel
from .relation_edit_form_model import RelationEditFormModel
from .relation_model import RelationModel
from .relation_model_links import RelationModelLinks
from .relation_model_links_delete import RelationModelLinksDelete
from .relation_model_links_from import RelationModelLinksFrom
from .relation_model_links_schema import RelationModelLinksSchema
from .relation_model_links_self import RelationModelLinksSelf
from .relation_model_links_to import RelationModelLinksTo
from .relation_model_links_update import RelationModelLinksUpdate
from .relation_model_links_update_immediately import RelationModelLinksUpdateImmediately
from .relation_schema_model import RelationSchemaModel
from .relations_model import RelationsModel
from .revision_model import RevisionModel
from .revision_model_links import RevisionModelLinks
from .revision_model_links_author import RevisionModelLinksAuthor
from .revision_model_links_project import RevisionModelLinksProject
from .revision_model_links_self import RevisionModelLinksSelf
from .revision_model_links_show_revision import RevisionModelLinksShowRevision
from .revision_model_message import RevisionModelMessage
from .revisions_model import RevisionsModel
from .role_model import RoleModel
from .role_model_links import RoleModelLinks
from .role_model_links_self import RoleModelLinksSelf
from .roles_model import RolesModel
from .root_model import RootModel
from .root_model_links import RootModelLinks
from .root_model_links_configuration import RootModelLinksConfiguration
from .root_model_links_memberships import RootModelLinksMemberships
from .root_model_links_priorities import RootModelLinksPriorities
from .root_model_links_relations import RootModelLinksRelations
from .root_model_links_self import RootModelLinksSelf
from .root_model_links_statuses import RootModelLinksStatuses
from .root_model_links_time_entries import RootModelLinksTimeEntries
from .root_model_links_types import RootModelLinksTypes
from .root_model_links_user import RootModelLinksUser
from .root_model_links_user_preferences import RootModelLinksUserPreferences
from .root_model_links_work_packages import RootModelLinksWorkPackages
from .root_model_type import RootModelType
from .schema_for_global_queries_model import SchemaForGlobalQueriesModel
from .schema_for_project_queries_model import SchemaForProjectQueriesModel
from .schema_model import SchemaModel
from .schema_model_links import SchemaModelLinks
from .schema_model_links_self import SchemaModelLinksSelf
from .schema_model_type import SchemaModelType
from .show_or_validate_form_json_body import ShowOrValidateFormJsonBody
from .star_query_model import StarQueryModel
from .status_model import StatusModel
from .status_model_links import StatusModelLinks
from .status_model_links_self import StatusModelLinksSelf
from .statuses_model import StatusesModel
from .storage_file_location_model import StorageFileLocationModel
from .storage_file_location_model_links import StorageFileLocationModelLinks
from .storage_file_location_model_links_self import StorageFileLocationModelLinksSelf
from .storage_file_model import StorageFileModel
from .storage_model import StorageModel
from .storage_model_links import StorageModelLinks
from .storage_model_links_authorization_state import StorageModelLinksAuthorizationState
from .storage_model_links_authorize import StorageModelLinksAuthorize
from .storage_model_links_open import StorageModelLinksOpen
from .storage_model_links_origin import StorageModelLinksOrigin
from .storage_model_links_self import StorageModelLinksSelf
from .storage_model_links_type import StorageModelLinksType
from .storage_model_type import StorageModelType
from .time_entry_activity_model import TimeEntryActivityModel
from .time_entry_activity_model_links import TimeEntryActivityModelLinks
from .time_entry_activity_model_links_projects import TimeEntryActivityModelLinksProjects
from .time_entry_activity_model_links_self import TimeEntryActivityModelLinksSelf
from .time_entry_model import TimeEntryModel
from .time_entry_model_links import TimeEntryModelLinks
from .time_entry_model_links_activity import TimeEntryModelLinksActivity
from .time_entry_model_links_delete import TimeEntryModelLinksDelete
from .time_entry_model_links_project import TimeEntryModelLinksProject
from .time_entry_model_links_self import TimeEntryModelLinksSelf
from .time_entry_model_links_update import TimeEntryModelLinksUpdate
from .time_entry_model_links_update_immediately import TimeEntryModelLinksUpdateImmediately
from .time_entry_model_links_user import TimeEntryModelLinksUser
from .time_entry_model_links_work_package import TimeEntryModelLinksWorkPackage
from .type_model import TypeModel
from .type_model_links import TypeModelLinks
from .type_model_links_self import TypeModelLinksSelf
from .types_by_project_model import TypesByProjectModel
from .types_model import TypesModel
from .unstar_query_model import UnstarQueryModel
from .update_activity_json_body import UpdateActivityJsonBody
from .update_activity_json_body_comment import UpdateActivityJsonBodyComment
from .update_group_json_body import UpdateGroupJsonBody
from .update_group_json_body_links import UpdateGroupJsonBodyLinks
from .update_group_json_body_links_members_item import UpdateGroupJsonBodyLinksMembersItem
from .update_project_json_body import UpdateProjectJsonBody
from .update_user_preferences_json_body import UpdateUserPreferencesJsonBody
from .user_collection_model import UserCollectionModel
from .user_collection_model_embedded import UserCollectionModelEmbedded
from .user_collection_model_links import UserCollectionModelLinks
from .user_collection_model_links_self import UserCollectionModelLinksSelf
from .user_create_model import UserCreateModel
from .user_model import UserModel
from .user_model_links import UserModelLinks
from .user_model_links_delete import UserModelLinksDelete
from .user_model_links_lock import UserModelLinksLock
from .user_model_links_memberships import UserModelLinksMemberships
from .user_model_links_self import UserModelLinksSelf
from .user_model_links_show_user import UserModelLinksShowUser
from .user_model_links_unlock import UserModelLinksUnlock
from .user_model_links_update_immediately import UserModelLinksUpdateImmediately
from .user_model_type import UserModelType
from .user_preference_model import UserPreferenceModel
from .user_preference_model_links import UserPreferenceModelLinks
from .user_preference_model_links_self import UserPreferenceModelLinksSelf
from .user_preference_model_links_user import UserPreferenceModelLinksUser
from .user_preferences_model import UserPreferencesModel
from .values_property_model import ValuesPropertyModel
from .values_property_model_links import ValuesPropertyModelLinks
from .values_property_model_links_schema import ValuesPropertyModelLinksSchema
from .values_property_model_links_self import ValuesPropertyModelLinksSelf
from .values_property_model_type import ValuesPropertyModelType
from .version_model import VersionModel
from .version_model_description import VersionModelDescription
from .version_model_links import VersionModelLinks
from .version_model_links_available_in_projects import VersionModelLinksAvailableInProjects
from .version_model_links_defining_project import VersionModelLinksDefiningProject
from .version_model_links_self import VersionModelLinksSelf
from .version_model_links_update import VersionModelLinksUpdate
from .version_model_links_update_immediately import VersionModelLinksUpdateImmediately
from .version_schema_model import VersionSchemaModel
from .versions_by_project_model import VersionsByProjectModel
from .versions_model import VersionsModel
from .view_action_model import ViewActionModel
from .view_capabilities_model import ViewCapabilitiesModel
from .view_global_context_model import ViewGlobalContextModel
from .view_group_model import ViewGroupModel
from .view_membership_model import ViewMembershipModel
from .view_membership_schema_model import ViewMembershipSchemaModel
from .view_project_status_model import ViewProjectStatusModel
from .view_time_entries_activity_model import ViewTimeEntriesActivityModel
from .view_time_entry_model import ViewTimeEntryModel
from .view_time_entry_schema_model import ViewTimeEntrySchemaModel
from .view_user_schema_model import ViewUserSchemaModel
from .watchers_model import WatchersModel
from .watchers_model_embedded import WatchersModelEmbedded
from .watchers_model_embedded_elements_item import WatchersModelEmbeddedElementsItem
from .watchers_model_links import WatchersModelLinks
from .watchers_model_links_self import WatchersModelLinksSelf
from .week_day_collection_model import WeekDayCollectionModel
from .week_day_collection_model_embedded import WeekDayCollectionModelEmbedded
from .week_day_collection_model_links import WeekDayCollectionModelLinks
from .week_day_collection_model_links_self import WeekDayCollectionModelLinksSelf
from .week_day_collection_write_model import WeekDayCollectionWriteModel
from .week_day_collection_write_model_embedded import WeekDayCollectionWriteModelEmbedded
from .week_day_collection_write_model_embedded_elements_item import WeekDayCollectionWriteModelEmbeddedElementsItem
from .week_day_collection_write_model_type import WeekDayCollectionWriteModelType
from .week_day_model import WeekDayModel
from .week_day_model_type import WeekDayModelType
from .week_day_self_link_model import WeekDaySelfLinkModel
from .week_day_self_link_model_self import WeekDaySelfLinkModelSelf
from .week_day_write_model import WeekDayWriteModel
from .week_day_write_model_type import WeekDayWriteModelType
from .wiki_page_model import WikiPageModel
from .wiki_page_model_links import WikiPageModelLinks
from .wiki_page_model_links_add_attachment import WikiPageModelLinksAddAttachment
from .work_package_activities_model import WorkPackageActivitiesModel
from .work_package_model import WorkPackageModel
from .work_package_model_description import WorkPackageModelDescription
from .work_package_model_links import WorkPackageModelLinks
from .work_package_model_links_add_attachment import WorkPackageModelLinksAddAttachment
from .work_package_model_links_add_comment import WorkPackageModelLinksAddComment
from .work_package_model_links_add_file_link import WorkPackageModelLinksAddFileLink
from .work_package_model_links_add_relation import WorkPackageModelLinksAddRelation
from .work_package_model_links_add_watcher import WorkPackageModelLinksAddWatcher
from .work_package_model_links_ancestors_item import WorkPackageModelLinksAncestorsItem
from .work_package_model_links_assignee import WorkPackageModelLinksAssignee
from .work_package_model_links_attachments import WorkPackageModelLinksAttachments
from .work_package_model_links_author import WorkPackageModelLinksAuthor
from .work_package_model_links_available_watchers import WorkPackageModelLinksAvailableWatchers
from .work_package_model_links_budget import WorkPackageModelLinksBudget
from .work_package_model_links_category import WorkPackageModelLinksCategory
from .work_package_model_links_children_item import WorkPackageModelLinksChildrenItem
from .work_package_model_links_custom_actions_item import WorkPackageModelLinksCustomActionsItem
from .work_package_model_links_file_links import WorkPackageModelLinksFileLinks
from .work_package_model_links_parent import WorkPackageModelLinksParent
from .work_package_model_links_preview_markup import WorkPackageModelLinksPreviewMarkup
from .work_package_model_links_priority import WorkPackageModelLinksPriority
from .work_package_model_links_project import WorkPackageModelLinksProject
from .work_package_model_links_relations import WorkPackageModelLinksRelations
from .work_package_model_links_remove_watcher import WorkPackageModelLinksRemoveWatcher
from .work_package_model_links_responsible import WorkPackageModelLinksResponsible
from .work_package_model_links_revisions import WorkPackageModelLinksRevisions
from .work_package_model_links_schema import WorkPackageModelLinksSchema
from .work_package_model_links_self import WorkPackageModelLinksSelf
from .work_package_model_links_status import WorkPackageModelLinksStatus
from .work_package_model_links_time_entries import WorkPackageModelLinksTimeEntries
from .work_package_model_links_type import WorkPackageModelLinksType
from .work_package_model_links_unwatch import WorkPackageModelLinksUnwatch
from .work_package_model_links_update import WorkPackageModelLinksUpdate
from .work_package_model_links_update_immediately import WorkPackageModelLinksUpdateImmediately
from .work_package_model_links_version import WorkPackageModelLinksVersion
from .work_package_model_links_watch import WorkPackageModelLinksWatch
from .work_package_model_links_watchers import WorkPackageModelLinksWatchers
from .work_package_model_type import WorkPackageModelType
from .work_package_relation_form_model import WorkPackageRelationFormModel
from .work_package_schemas_model import WorkPackageSchemasModel
from .work_packages_model import WorkPackagesModel
from .work_packages_model_embedded import WorkPackagesModelEmbedded
from .work_packages_model_links import WorkPackagesModelLinks
from .work_packages_model_links_self import WorkPackagesModelLinksSelf

__all__ = (
    "ActivityModel",
    "ActivityModelComment",
    "AddWatcherJsonBody",
    "AddWatcherJsonBodyUser",
    "AttachmentModel",
    "AttachmentModelDescription",
    "AttachmentModelLinks",
    "AttachmentModelLinksAuthor",
    "AttachmentModelLinksContainer",
    "AttachmentModelLinksDelete",
    "AttachmentModelLinksDownloadLocation",
    "AttachmentModelLinksSelf",
    "AttachmentsModel",
    "AttachmentsModelEmbedded",
    "AttachmentsModelEmbeddedElementsItem",
    "AttachmentsModelLinks",
    "AttachmentsModelLinksSelf",
    "AvailableAssigneesModel",
    "AvailableProjectsForMembershipsModel",
    "AvailableProjectsForQueryModel",
    "AvailableProjectsForTimeEntriesModel",
    "AvailableProjectsForVersionsModel",
    "AvailableProjectsForWorkPackageModel",
    "AvailableRelationCandidatesModel",
    "AvailableResponsiblesModel",
    "AvailableWatchersModel",
    "BudgetModel",
    "BudgetModelLinks",
    "BudgetModelLinksSelf",
    "BudgetsByProjectModel",
    "CategoriesByProjectModel",
    "CategoryModel",
    "CategoryModelLinks",
    "CategoryModelLinksDefaultAssignee",
    "CategoryModelLinksProject",
    "CategoryModelLinksSelf",
    "CollectionModel",
    "CollectionModelGroups",
    "CollectionModelTotalSums",
    "CommentWorkPackageJsonBody",
    "CommentWorkPackageJsonBodyComment",
    "ConfigurationModel",
    "CreateGroupJsonBody",
    "CreateGroupJsonBodyLinks",
    "CreateGroupJsonBodyLinksMembersItem",
    "CreateProjectJsonBody",
    "CreateViewsJsonBody",
    "CreateViewsJsonBodyLinks",
    "CreateViewsJsonBodyLinksQuery",
    "CreateViewsResponse201",
    "CustomActionModel",
    "CustomactionModel",
    "CustomactionModelLinks",
    "CustomactionModelLinksExecuteImmediately",
    "CustomOptionModel",
    "CustomOptionModelLinks",
    "CustomOptionModelLinksSelf",
    "DayCollectionModel",
    "DayCollectionModelEmbedded",
    "DayCollectionModelLinks",
    "DayCollectionModelLinksSelf",
    "DayModel",
    "DayModelLinks",
    "DayModelLinksWeekDay",
    "DayModelType",
    "DefaultQueryForProjectModel",
    "DefaultQueryModel",
    "DocumentModel",
    "DocumentModelLinks",
    "DocumentModelLinksAttachments",
    "DocumentModelLinksProject",
    "DocumentModelLinksSelf",
    "DocumentsModel",
    "EditQueryJsonBody",
    "ErrorResponse",
    "ErrorResponseEmbedded",
    "ErrorResponseEmbeddedDetails",
    "ErrorResponseType",
    "ExampleFormModel",
    "ExampleSchemaModel",
    "ExecuteCustomActionJsonBody",
    "ExecuteCustomActionJsonBodyLinks",
    "ExecuteCustomActionJsonBodyLinksWorkPackage",
    "FileCollectionModel",
    "FileCollectionModelEmbedded",
    "FileCollectionModelLinks",
    "FileCollectionModelLinksSelf",
    "FileLinkCollectionReadModel",
    "FileLinkCollectionReadModelEmbedded",
    "FileLinkCollectionReadModelLinks",
    "FileLinkCollectionReadModelLinksSelf",
    "FileLinkCollectionWriteModel",
    "FileLinkCollectionWriteModelEmbedded",
    "FileLinkOriginDataModel",
    "FileLinkReadModel",
    "FileLinkReadModelEmbedded",
    "FileLinkReadModelLinks",
    "FileLinkReadModelLinksContainer",
    "FileLinkReadModelLinksCreator",
    "FileLinkReadModelLinksDelete",
    "FileLinkReadModelLinksOriginOpen",
    "FileLinkReadModelLinksOriginOpenLocation",
    "FileLinkReadModelLinksPermission",
    "FileLinkReadModelLinksSelf",
    "FileLinkReadModelLinksStaticOriginDownload",
    "FileLinkReadModelLinksStaticOriginOpen",
    "FileLinkReadModelLinksStaticOriginOpenLocation",
    "FileLinkReadModelLinksStorage",
    "FileLinkReadModelType",
    "FileLinkWriteModel",
    "FileLinkWriteModelLinksType0",
    "FileLinkWriteModelLinksType0Storage",
    "FileLinkWriteModelLinksType1",
    "FileLinkWriteModelLinksType1StorageUrl",
    "Formattable",
    "FormattableFormat",
    "FormModel",
    "FormModelLinks",
    "FormModelLinksCommit",
    "FormModelLinksPreviewMarkup",
    "FormModelLinksSelf",
    "FormModelLinksValidate",
    "GridModel",
    "GridModelLinks",
    "GridModelLinksPage",
    "GridModelLinksSelf",
    "GridModelLinksUpdate",
    "GridModelLinksUpdateImmediately",
    "GridModelWidgetsItem",
    "GridsModel",
    "GridUpdateFormResponse200",
    "GroupModel",
    "GroupModelLinks",
    "GroupModelLinksDelete",
    "GroupModelLinksMembers",
    "GroupModelLinksMemberships",
    "GroupModelLinksSelf",
    "GroupModelLinksUpdateImmediately",
    "HelpTextModel",
    "HelptextModel",
    "HelptextModelHelpText",
    "HelptextModelLinks",
    "HelptextModelLinksEditText",
    "HelptextModelLinksSelf",
    "HelpTextsModel",
    "Link",
    "LinkPayload",
    "ListActionsModel",
    "ListAvailableParentProjectCandidatesModel",
    "ListCapabilitiesModel",
    "ListGroupsModel",
    "ListMembershipsModel",
    "ListOfNewsModel",
    "ListProjectsByVersionModel",
    "ListProjectsModel",
    "ListTimeEntriesModel",
    "MembershipModel",
    "MembershipModelLinks",
    "MembershipModelLinksPrincipal",
    "MembershipModelLinksProject",
    "MembershipModelLinksRoles",
    "MembershipModelLinksSelf",
    "NewsModel",
    "NewsModelLinks",
    "NewsModelLinksAuthor",
    "NewsModelLinksProject",
    "NewsModelLinksSelf",
    "NonWorkingDayModel",
    "NonWorkingDayModelLinks",
    "NonWorkingDayModelLinksSelf",
    "NonWorkingDayModelType",
    "NotificationCollectionModel",
    "NotificationCollectionModelEmbedded",
    "NotificationCollectionModelLinks",
    "NotificationCollectionModelLinksChangeSize",
    "NotificationCollectionModelLinksJumpTo",
    "NotificationCollectionModelLinksSelf",
    "NotificationModel",
    "NotificationModelEmbedded",
    "NotificationModelLinks",
    "NotificationModelLinksActivity",
    "NotificationModelLinksActor",
    "NotificationModelLinksDetailsItem",
    "NotificationModelLinksProject",
    "NotificationModelLinksReadIAN",
    "NotificationModelLinksResource",
    "NotificationModelLinksSelf",
    "NotificationModelLinksUnreadIAN",
    "NotificationModelReason",
    "NotificationModelType",
    "NotificationSettingsModelItem",
    "NotificationSettingsModelItemDueDate",
    "NotificationSettingsModelItemLinks",
    "NotificationSettingsModelItemLinksProject",
    "NotificationSettingsModelItemOverdue",
    "NotificationSettingsModelItemStartDate",
    "PostModel",
    "PostModelLinks",
    "PostModelLinksAddAttachment",
    "PreviewingModel",
    "PrincipalModel",
    "PrincipalsModel",
    "PrioritiesModel",
    "PriorityModel",
    "PriorityModelLinks",
    "PriorityModelLinksSelf",
    "ProjectCreateFormJsonBody",
    "ProjectCreateFormResponse200",
    "ProjectModel",
    "ProjectModelLinks",
    "ProjectModelLinksCategories",
    "ProjectModelLinksCreateWorkPackage",
    "ProjectModelLinksCreateWorkPackageImmediately",
    "ProjectModelLinksDelete",
    "ProjectModelLinksMemberships",
    "ProjectModelLinksParent",
    "ProjectModelLinksSelf",
    "ProjectModelLinksStatus",
    "ProjectModelLinksStoragesItem",
    "ProjectModelLinksTypes",
    "ProjectModelLinksUpdate",
    "ProjectModelLinksUpdateImmediately",
    "ProjectModelLinksVersions",
    "ProjectModelLinksWorkPackages",
    "ProjectModelStatusExplanation",
    "ProjectModelType",
    "ProjectsSchemaModel",
    "ProjectUpdateFormJsonBody",
    "QueriesModel",
    "QueryColumnModel",
    "QueryFilterInstanceSchemaModel",
    "QueryFilterInstanceSchemaModelLinks",
    "QueryFilterInstanceSchemaModelLinksFilter",
    "QueryFilterInstanceSchemaModelLinksSelf",
    "QueryFilterInstanceSchemasForProjectModel",
    "QueryFilterInstanceSchemasModel",
    "QueryFilterModel",
    "QueryModel",
    "QueryModelLinks",
    "QueryModelLinksStar",
    "QueryModelLinksUnstar",
    "QueryModelLinksUpdate",
    "QueryModelLinksUpdateImmediately",
    "QueryOperatorModel",
    "QuerySortByModel",
    "RelationEditFormModel",
    "RelationModel",
    "RelationModelLinks",
    "RelationModelLinksDelete",
    "RelationModelLinksFrom",
    "RelationModelLinksSchema",
    "RelationModelLinksSelf",
    "RelationModelLinksTo",
    "RelationModelLinksUpdate",
    "RelationModelLinksUpdateImmediately",
    "RelationSchemaModel",
    "RelationsModel",
    "RevisionModel",
    "RevisionModelLinks",
    "RevisionModelLinksAuthor",
    "RevisionModelLinksProject",
    "RevisionModelLinksSelf",
    "RevisionModelLinksShowRevision",
    "RevisionModelMessage",
    "RevisionsModel",
    "RoleModel",
    "RoleModelLinks",
    "RoleModelLinksSelf",
    "RolesModel",
    "RootModel",
    "RootModelLinks",
    "RootModelLinksConfiguration",
    "RootModelLinksMemberships",
    "RootModelLinksPriorities",
    "RootModelLinksRelations",
    "RootModelLinksSelf",
    "RootModelLinksStatuses",
    "RootModelLinksTimeEntries",
    "RootModelLinksTypes",
    "RootModelLinksUser",
    "RootModelLinksUserPreferences",
    "RootModelLinksWorkPackages",
    "RootModelType",
    "SchemaForGlobalQueriesModel",
    "SchemaForProjectQueriesModel",
    "SchemaModel",
    "SchemaModelLinks",
    "SchemaModelLinksSelf",
    "SchemaModelType",
    "ShowOrValidateFormJsonBody",
    "StarQueryModel",
    "StatusesModel",
    "StatusModel",
    "StatusModelLinks",
    "StatusModelLinksSelf",
    "StorageFileLocationModel",
    "StorageFileLocationModelLinks",
    "StorageFileLocationModelLinksSelf",
    "StorageFileModel",
    "StorageModel",
    "StorageModelLinks",
    "StorageModelLinksAuthorizationState",
    "StorageModelLinksAuthorize",
    "StorageModelLinksOpen",
    "StorageModelLinksOrigin",
    "StorageModelLinksSelf",
    "StorageModelLinksType",
    "StorageModelType",
    "TimeEntryActivityModel",
    "TimeEntryActivityModelLinks",
    "TimeEntryActivityModelLinksProjects",
    "TimeEntryActivityModelLinksSelf",
    "TimeEntryModel",
    "TimeEntryModelLinks",
    "TimeEntryModelLinksActivity",
    "TimeEntryModelLinksDelete",
    "TimeEntryModelLinksProject",
    "TimeEntryModelLinksSelf",
    "TimeEntryModelLinksUpdate",
    "TimeEntryModelLinksUpdateImmediately",
    "TimeEntryModelLinksUser",
    "TimeEntryModelLinksWorkPackage",
    "TypeModel",
    "TypeModelLinks",
    "TypeModelLinksSelf",
    "TypesByProjectModel",
    "TypesModel",
    "UnstarQueryModel",
    "UpdateActivityJsonBody",
    "UpdateActivityJsonBodyComment",
    "UpdateGroupJsonBody",
    "UpdateGroupJsonBodyLinks",
    "UpdateGroupJsonBodyLinksMembersItem",
    "UpdateProjectJsonBody",
    "UpdateUserPreferencesJsonBody",
    "UserCollectionModel",
    "UserCollectionModelEmbedded",
    "UserCollectionModelLinks",
    "UserCollectionModelLinksSelf",
    "UserCreateModel",
    "UserModel",
    "UserModelLinks",
    "UserModelLinksDelete",
    "UserModelLinksLock",
    "UserModelLinksMemberships",
    "UserModelLinksSelf",
    "UserModelLinksShowUser",
    "UserModelLinksUnlock",
    "UserModelLinksUpdateImmediately",
    "UserModelType",
    "UserPreferenceModel",
    "UserPreferenceModelLinks",
    "UserPreferenceModelLinksSelf",
    "UserPreferenceModelLinksUser",
    "UserPreferencesModel",
    "ValuesPropertyModel",
    "ValuesPropertyModelLinks",
    "ValuesPropertyModelLinksSchema",
    "ValuesPropertyModelLinksSelf",
    "ValuesPropertyModelType",
    "VersionModel",
    "VersionModelDescription",
    "VersionModelLinks",
    "VersionModelLinksAvailableInProjects",
    "VersionModelLinksDefiningProject",
    "VersionModelLinksSelf",
    "VersionModelLinksUpdate",
    "VersionModelLinksUpdateImmediately",
    "VersionsByProjectModel",
    "VersionSchemaModel",
    "VersionsModel",
    "ViewActionModel",
    "ViewCapabilitiesModel",
    "ViewGlobalContextModel",
    "ViewGroupModel",
    "ViewMembershipModel",
    "ViewMembershipSchemaModel",
    "ViewProjectStatusModel",
    "ViewTimeEntriesActivityModel",
    "ViewTimeEntryModel",
    "ViewTimeEntrySchemaModel",
    "ViewUserSchemaModel",
    "WatchersModel",
    "WatchersModelEmbedded",
    "WatchersModelEmbeddedElementsItem",
    "WatchersModelLinks",
    "WatchersModelLinksSelf",
    "WeekDayCollectionModel",
    "WeekDayCollectionModelEmbedded",
    "WeekDayCollectionModelLinks",
    "WeekDayCollectionModelLinksSelf",
    "WeekDayCollectionWriteModel",
    "WeekDayCollectionWriteModelEmbedded",
    "WeekDayCollectionWriteModelEmbeddedElementsItem",
    "WeekDayCollectionWriteModelType",
    "WeekDayModel",
    "WeekDayModelType",
    "WeekDaySelfLinkModel",
    "WeekDaySelfLinkModelSelf",
    "WeekDayWriteModel",
    "WeekDayWriteModelType",
    "WikiPageModel",
    "WikiPageModelLinks",
    "WikiPageModelLinksAddAttachment",
    "WorkPackageActivitiesModel",
    "WorkPackageModel",
    "WorkPackageModelDescription",
    "WorkPackageModelLinks",
    "WorkPackageModelLinksAddAttachment",
    "WorkPackageModelLinksAddComment",
    "WorkPackageModelLinksAddFileLink",
    "WorkPackageModelLinksAddRelation",
    "WorkPackageModelLinksAddWatcher",
    "WorkPackageModelLinksAncestorsItem",
    "WorkPackageModelLinksAssignee",
    "WorkPackageModelLinksAttachments",
    "WorkPackageModelLinksAuthor",
    "WorkPackageModelLinksAvailableWatchers",
    "WorkPackageModelLinksBudget",
    "WorkPackageModelLinksCategory",
    "WorkPackageModelLinksChildrenItem",
    "WorkPackageModelLinksCustomActionsItem",
    "WorkPackageModelLinksFileLinks",
    "WorkPackageModelLinksParent",
    "WorkPackageModelLinksPreviewMarkup",
    "WorkPackageModelLinksPriority",
    "WorkPackageModelLinksProject",
    "WorkPackageModelLinksRelations",
    "WorkPackageModelLinksRemoveWatcher",
    "WorkPackageModelLinksResponsible",
    "WorkPackageModelLinksRevisions",
    "WorkPackageModelLinksSchema",
    "WorkPackageModelLinksSelf",
    "WorkPackageModelLinksStatus",
    "WorkPackageModelLinksTimeEntries",
    "WorkPackageModelLinksType",
    "WorkPackageModelLinksUnwatch",
    "WorkPackageModelLinksUpdate",
    "WorkPackageModelLinksUpdateImmediately",
    "WorkPackageModelLinksVersion",
    "WorkPackageModelLinksWatch",
    "WorkPackageModelLinksWatchers",
    "WorkPackageModelType",
    "WorkPackageRelationFormModel",
    "WorkPackageSchemasModel",
    "WorkPackagesModel",
    "WorkPackagesModelEmbedded",
    "WorkPackagesModelLinks",
    "WorkPackagesModelLinksSelf",
)
