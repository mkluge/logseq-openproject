import "@logseq/libs";
import { SettingSchemaDesc } from "@logseq/libs/dist/LSPlugin.user";

export const settingsUI = () => {
  /* https://logseq.github.io/plugins/types/SettingSchemaDesc.html */
  const settingsTemplate: SettingSchemaDesc[] = [
    {
      key: "GitLabURL",
      type: "string",
      title: "URL of your GitLab Instance",
      description: "Use the base URL without /api/v4 at the end.",
      default: "https://gitlab.com",
    },
    {
      key: "GitLabToken",
      type: "string",
      title: "Personal Access Token",
      description:
        "Create a Personal Access Token in GitLab with 'api' scope.",
      default: "",
    },
    {
      key: "GitLabProjectIds",
      type: "string",
      title: "Limit to project IDs (optional)",
      description:
        "Comma-separated project IDs to filter issues. Leave empty for all assigned issues.",
      default: "",
    },
    {
      key: "GitLabLabelFilter",
      type: "string",
      title: "Filter by labels (optional)",
      description:
        "Comma-separated label names used to filter issues assigned to you.",
      default: "",
    },
    {
      key: "GitLabState",
      type: "enum",
      title: "Issue state",
      enumChoices: ["opened", "closed", "all"],
      description: "Filter issues by state.",
      default: "opened",
    },
  ];
  logseq.useSettingsSchema(settingsTemplate);
};
