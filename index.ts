// import { ProjectModel } from "./openproject_api/api";
// import * as lcfg from "./config.json";
// import axios, { AxiosResponse } from "axios";
import "@logseq/libs";
import { settingsUI } from "./settings"
import {
  Configuration,
  ProjectsApi,
  WorkPackagesApi,
  WorkPackagesApiListWorkPackagesRequest,
  UsersApi,
} from "./openproject_api";


async function main() {

  var openProjectToken = "";
  var openProjectURL = "";
  
  const loadSettings = () => {
    if (logseq.settings ) {
      openProjectToken = logseq.settings["OpenProjectToken"];
      openProjectURL = logseq.settings["OpenProjectURL"];
    }  
  }

  loadSettings();
  logseq.onSettingsChanged(loadSettings);

  /*const lcfg = {
    API_URL: "http://localhost:8080",
    API_KEY: "aa5a27e52ee6671f4aac50df6471b1f4a84e571f64c8660e2d35bdfa1ae8438c",
  };*/
  const configuration = new Configuration({
    basePath: openProjectURL,
    username: "apikey",
    password: openProjectToken,
  });

  settingsUI();

  console.log("loaded config with URL " + openProjectURL);
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
  const myself: String = me.data.name;
  const workPackagesApi = new WorkPackagesApi(configuration);
  const filterMyself = [{ assignee: { operator: "**", values: [myself] } }];
  const filter = {
    filters: JSON.stringify(filterMyself)
  };
  // FIXME: would like to call listWorkPackages with the filter
  //        but it throws a server error, probably incorrect usage
  //        of this feature
  const workPackages = await workPackagesApi.listWorkPackages();
  const myWorkPackages = workPackages.data._embedded.elements.filter(function (
    wp
  ) {
    if (wp._links.assignee?.title == myself) {
      return true;
    }
    return false;
  });
  console.log(myWorkPackages);
}

logseq.ready(main).catch(console.error);
