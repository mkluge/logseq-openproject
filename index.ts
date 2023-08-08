// import { ProjectModel } from "./openproject_api/api";
// import * as lcfg from "./config.json";
// import axios, { AxiosResponse } from "axios";
import "@logseq/libs";
import {
  Configuration,
  ProjectsApi,
  WorkPackagesApi,
  WorkPackagesApiListWorkPackagesRequest,
  UsersApi,
} from "./openproject_api";

async function main() {
  const lcfg = {
    API_URL: "http://localhost:8080",
    API_KEY: "aa5a27e52ee6671f4aac50df6471b1f4a84e571f64c8660e2d35bdfa1ae8438c",
  };
  const configuration = new Configuration({
    basePath: lcfg.API_URL,
    username: "apikey",
    password: lcfg.API_KEY,
  });

  console.log("loaded config with URL " + lcfg.API_URL);
  // get my name in OpenProject
  const usersApi = new UsersApi(configuration);
  const me = await usersApi.viewUser({
    id: "me",
  });
  if (me.status != 200) {
    console.log("Error unable to read user data");
    console.log(me);
    return;
  }
  const myself = me.data.name;
  const workPackagesApi = new WorkPackagesApi(configuration);
  const filterMyself = [{ assignee: { operator: "**", values: [myself] } }];
  console.log(JSON.stringify(filterMyself))
  const filter: WorkPackagesApiListWorkPackagesRequest = {
    filters: JSON.stringify(filterMyself),
  };
  const workPackages = await workPackagesApi.listWorkPackages(filter);
  workPackages.data._embedded.elements.map(function (wp) {
    console.log(wp._links.assignee?.title);
  });
}

logseq.ready(main).catch(console.error);
