import { ProjectModel } from "./openproject_api/api";
import "@logseq/libs";

async function main() {
  const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
  for (let i = 0; i < 14; i++) {
    logseq.Editor.registerSlashCommand("wait" + i + "d", async () => {
      var result = new Date();
      result.setDate(result.getDate() + i);
      let datum = result.toISOString().substring(0, 10);
      datum += " " + days[result.getDay()];
      const dueDate =
        `
SCHEDULED: <` +
        datum +
        ">";
      const currentBlock = await logseq.Editor.getCurrentBlock();
      if (currentBlock) {
        //console.log(currentBlock);
        const newContent = "TODO " + currentBlock.content + dueDate;
        await logseq.Editor.updateBlock(currentBlock.uuid, newContent);
        //await logseq.Editor.exitEditingMode();
      }
    });
  }
}

import * as lcfg from "./config.json";
import axios, { AxiosResponse } from "axios";
import { Configuration, ProjectsApi } from "./openproject_api";

const configuration = new Configuration({
  basePath: lcfg.API_URL,
  username: "apikey",
  password: lcfg.API_KEY,
});

console.log("loaded config with URL " + lcfg.API_URL);

//const data = await axios.get(lcfg.API_URL + "/projects", {
//  auth: {
//    username: "apikey",
//    password: lcfg.API_KEY,
//  },
//});
//console.log(data);

const projectsApi = new ProjectsApi(configuration);
const projects: AxiosResponse<ProjectModel[], any> =
  await projectsApi.listProjects();
console.log(projects);

logseq.ready(main).catch(console.error);
