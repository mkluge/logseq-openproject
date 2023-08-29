import "@logseq/libs";
import { SettingSchemaDesc } from "@logseq/libs/dist/LSPlugin.user";

export const settingsUI = (taskTypes: Array<string> = []) => {
  /* https://logseq.github.io/plugins/types/SettingSchemaDesc.html */
  const settingsTemplate: SettingSchemaDesc[] = [
    {
      key: "OpenProjectURL",
      type: "string",
      title: "URL of your OpenProject Instance",
      description: "Use the base URL without /api/v3 at the end.",
      default: "http://localhost:8080",
    },
    {
      key: "OpenProjectToken",
      type: "string",
      title: "Your app token",
      description:
        "An API key can be generated in OpenProject on the \
                          'Access token' page within the 'My account' section \
                          by clicking on the 'Generate' or 'Reset' (depending \
                          on whether a key already exists) link within the \
                          'API' row",
      default: "",
    },
    {
      key: "TaskTypeFilter",
      type: "enum",
      title: "Only use this kind of tasks",
      enumChoices: taskTypes,
      description: "the currently available task types",
      default: [],
    },
  ];
  logseq.useSettingsSchema(settingsTemplate);
};
