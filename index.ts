// import { ProjectModel } from "./openproject_api/api";
// import * as lcfg from "./config.json";
// import axios, { AxiosResponse } from "axios";
import "@logseq/libs";
import { Configuration, ConfigurationApiAxiosParamCreator, ProjectsApi, WorkPackagesApi } from "./openproject_api";

async function main() {
  console.log("2")
  const lcfg = {
    "API_URL": "http://localhost:8080",
    "API_KEY": "aa5a27e52ee6671f4aac50df6471b1f4a84e571f64c8660e2d35bdfa1ae8438c"
  }
  const configuration = new Configuration({
    basePath: lcfg.API_URL,
    username: "apikey",
    password: lcfg.API_KEY,
  });
  
  console.log("loaded config with URL " + lcfg.API_URL);
  const projectsApi = new ProjectsApi(configuration);
  const projects = await projectsApi.listProjects();
  console.log(projects);
  const workPackagesApi = new WorkPackagesApi(configuration);
  console.log(await workPackagesApi.listWorkPackages());
}

logseq.ready(main).catch(console.error);