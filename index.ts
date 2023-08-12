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

function website(x: number, y: number, text: string, tasks: string[] = []) {
  return {
    key: "opeproject-task-selection",
    template: `
    <div padding: 10px; overflow: auto; data-on-load="console.log('popup')" onLoad="console.log('popup')">
    <input type="text" id="filterInput" placeholder="Filter..." data-on-change="setupDialog"/>
    <div id="listContainer"></div>
    </div>
    <button data-on-click="openCalendar" onclick="alert('abc')' style="opacity: .6; display: inline-flex; padding-left: 3px;'>
   asdfasfsdas</button>
  `,
    style: {
      left: x + "px",
      top: y + "px",
      width: "500px",
      height: "300px",
      backgroundColor: "var(--ls-primary-background-color)",
      color: "var(--ls-primary-text-color)",
      boxShadow: "1px 2px 5px var(--ls-secondary-background-color)",
    },
    attrs: {
      title: text,
    },
  };
}

async function showUI(x: number, y: number) {
  await updateWorkPackages();
  logseq.provideUI(
    website(
      x,
      y,
      "Packages",
      myWorkPackages.map((wp) => wp.subject)
    )
  );
}

async function updateFilteredList() {
  const inputField = document.getElementById(
    "filterInput"
  ) as HTMLInputElement;
  const listContainer = document.getElementById("listContainer");
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
}

async function setupDialog(e: any) {
  console.log("run setupDialog");
  // Attach an event listener to the input field to trigger filtering
  const inputField = document.getElementById(
    "filterInput"
  ) as HTMLInputElement;
  inputField.focus();
  inputField.addEventListener("input", updateFilteredList);
  // Initial rendering of the list
  updateFilteredList();
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

  logseq.provideModel({
    openCalendar () {
      console.log("hi, calendar");
    },
    updateFilteredList,
    setupDialog
  });
  
  logseq.Editor.registerSlashCommand("openproject", async () => {
    const cursorat = await logseq.Editor.getEditingCursorPosition();
    const x = cursorat ? cursorat.rect.x : 300;
    const y = cursorat ? cursorat.rect.y : 300;
    await showUI(x, y);
  });
}

logseq.ready(main).catch(console.error);
