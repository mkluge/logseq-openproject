// import { ProjectModel } from "./openproject_api/api";
// import * as lcfg from "./config.json";
// import axios, { AxiosResponse } from "axios";
import "@logseq/libs";
import { settingsUI } from "./settings";
import {
  Configuration,
  WorkPackagesApi,
  UsersApi,
  WorkPackagesApiListWorkPackagesRequest,
  WorkPackageModel,
} from "./openproject_api";

var myWorkPackages: WorkPackageModel[];
var usersApi: UsersApi = new UsersApi();
var workPackagesApi: WorkPackagesApi = new WorkPackagesApi();
var myself: string = "";

async function updateWorkPackages() {
  console.log("update work packages");
  const filterMyself = [{ assignee: { operator: "**", values: [myself] } }];
  const filter = {
    filters: JSON.stringify(filterMyself),
  };
  // FIXME: would like to call listWorkPackages with the filter
  //        but it throws a server error, probably incorrect usage
  //        of this feature
  const workPackages = await workPackagesApi.listWorkPackages();
  myWorkPackages = workPackages.data._embedded.elements.filter(
    (wp) => wp._links.assignee?.title == myself
  );
}

function website(x: number, y: number, text: string, tasks: string = "") : string {
  const list_style = `
    padding: 0;
    list-style: none;
    margin-left: 0;

  .styled-list li {
    padding: 0px;
    color: #000; /* Black text color */
  }
  
  .styled-list li:nth-child(odd) {
    background-color: #0057B7; /* Blue background color */
    color: #FFFFFF; /* Black text color */
  }
  
  .styled-list li:nth-child(even) {
    background-color: #003797; /* Yellow background color */
    color: #FFFFFF; /* Black text color */
  }
  
  .styled-list li.highlighted {
    background-color: #FFDD00; /* Yellow background color */
    color: #000000; /* Black text color */
  }`;

  return `
    <div style="left: ${x}px, top: ${y}px, width: 500px, height: auto,
                backgroundColor: var(--ls-primary-background-color),
                color: var(--ls-primary-text-color),
                boxShadow: 1px 2px 5px var(--ls-secondary-background-color)">
      <h3>${text}</h3>
      <div style="padding: 10px; overflow: auto; 
        <input style="padding: 10px; margin-bottom: 10px;" 
              data-on-keyup="updateFilteredList" 
              type="text" id="filterInput" 
              placeholder="type to filter ..."/>
        <ul style="padding: 0; list-style: none; margin-left: 0;" id="listContainer">${tasks}</ul>
      </div>
    </div>
  `;
}

async function showUI(x: number, y: number) {
  await updateWorkPackages();
  const htmlcode =  website( 
    x, y, "Packages",
    myWorkPackages.map((wp) => {
      return "<li>" + wp.subject + "</li>";
    }).join("")
  );
  const app = document.getElementById('app');
  if( app) {
    app.innerHTML = htmlcode
  } 
  else{
    console.log("app element not found")
  }
  logseq.showMainUI()
}

async function main() {
  var openProjectToken = "";
  var openProjectURL = "";

  const loadSettings = () => {
    if (logseq.settings) {
      openProjectToken = logseq.settings["OpenProjectToken"];
      openProjectURL = logseq.settings["OpenProjectURL"];
      const openProjectConfiguration = new Configuration({
        basePath: openProjectURL,
        username: "apikey",
        password: openProjectToken,
      });
      usersApi = new UsersApi(openProjectConfiguration);
      workPackagesApi = new WorkPackagesApi(openProjectConfiguration);
    }
  };

  loadSettings();
  logseq.onSettingsChanged(loadSettings);
  settingsUI();

  console.log("loaded config with URL " + openProjectURL);
  // get my name in OpenProject
  const me = await usersApi.viewUser({
    id: "me",
  });
  if (me.status != 200) {
    console.log("Error unable to read user data");
    console.log(me);
    return;
  }
  myself = me.data.name;

`
  );
  logseq.provideModel({
    async updateFilteredList() {
      const inputField = parent.document.getElementById(
        "filterInput"
      ) as HTMLInputElement;
      const listContainer = parent.document.getElementById("listContainer");
      console.log(listContainer);
      const filterText = inputField.value.toLowerCase();
      if (listContainer) {
        listContainer.innerHTML = "";
        const filteredItems = myWorkPackages.filter((item) =>
          item.subject.toLowerCase().includes(filterText)
        );
        filteredItems.forEach((item) => {
          const listItem = document.createElement("div");
          listItem.textContent = item.subject;
          listContainer.appendChild(listItem);
        });
      }
    },
  });

  logseq.Editor.registerSlashCommand("openproject", async () => {
    const cursorat = await logseq.Editor.getEditingCursorPosition();
    const x = cursorat ? cursorat.rect.x : 300;
    const y = cursorat ? cursorat.rect.y : 300;
    await showUI(x, y);
  });
}

buildMainElement();

logseq.ready(main).catch(console.error);
