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
var selectedElement: number = -1;
var filterInput: HTMLInputElement;
var listContainer: HTMLLIElement;

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

function website(text: string, tasks: string = ""): string {
  return `
  <div class="rounded">
    <div class="maindiv">
      <div class="headline">${text}</div>
      <div style="padding: 10px; overflow: auto;">
        <input class="filterInput" type="text" id="filterInput" 
              placeholder="type to filter ..."/>
        <ul class="styled-list"
            id="listContainer"></ul>
      </div>
    </div>
  </div>
  `;
}

function updateFilteredList() {
  const filterText = filterInput.value.toLowerCase();
  listContainer.innerHTML = "";
  const filteredItems = myWorkPackages.filter((item) =>
    item.subject.toLowerCase().includes(filterText)
  );
  filteredItems.forEach((item) => {
    const listItem = document.createElement("li");
    listItem.textContent = item.subject;
    listContainer.appendChild(listItem);
  });
}

function createUI() {
  const htmlcode = website("Select OpenProject Task", "");
  const app = document.getElementById("app");
  if (app) {
    app.innerHTML = htmlcode;
  } else {
    console.log("app element not found");
    return;
  }

  filterInput = document.getElementById("filterInput") as HTMLInputElement;
  listContainer = document.getElementById("listContainer") as HTMLLIElement;

  if (filterInput == null || listContainer == null) {
    console.log("unable to add elements to app");
    return;
  }

  filterInput.addEventListener("input", updateFilteredList);
  filterInput.addEventListener("keydown", async (e) => {
    console.log(e);
    switch (e.key) {
      case "ArrowUp":
        console.log("Up");
        e.preventDefault();
        break;
      case "ArrowDown":
        console.log("Down");
        e.preventDefault();
        break;
      case "Enter":
        console.log("Enter");
        logseq.hideMainUI({ restoreEditingCursor: true });
        await logseq.Editor.insertAtEditingCursor("put stuff here");
        e.preventDefault();
        break;
      case "Escape":
        logseq.hideMainUI({ restoreEditingCursor: true });
        e.preventDefault();
        break;
    }
  });
}

async function showUI(x: number, y: number) {
  await updateWorkPackages();
  Object.assign(filterInput.style, {
    top: x + "px",
    left: y + "px",
  });
  selectedElement = -1;
  updateFilteredList();
  logseq.showMainUI();
  setTimeout(() => {
    filterInput.focus();
    filterInput.select();  
  }, 100);
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
  createUI();

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

  logseq.Editor.registerSlashCommand("openproject", async () => {
    const pos = await logseq.Editor.getEditingCursorPosition();
    console.log(pos);
    const x = pos ? pos.left + pos.rect.left : 300;
    const y = pos ? pos.top + pos.rect.top : 300;
    await showUI(x, y);
  });
}

logseq.ready(main).catch(console.error);
