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
  const ul_style = "padding: 0; list-style: none; margin-left: 0;";
  return `
    <div style="width: 500px, height: auto,
                backgroundColor: var(--ls-primary-background-color),
                color: var(--ls-primary-text-color),
                boxShadow: 1px 2px 5px var(--ls-secondary-background-color)">
      <h3>${text}</h3>
      <div style="padding: 10px; overflow: auto; 
        <input style="padding: 10px; margin-bottom: 10px;" 
              data-on-keyup="updateFilteredList" 
              type="text" id="filterInput" 
              placeholder="type to filter ..."/>
        <ul style="${ul_style}" id="listContainer"></ul>
      </div>
    </div>
  `;
}

function updateFilteredList() {
  const inputField = document.getElementById("filterInput") as HTMLInputElement;
  const listContainer = parent.document.getElementById("listContainer");
  console.log(listContainer);
  const filterText = inputField.value.toLowerCase();
  if (listContainer) {
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
}

function createUI() {
  const htmlcode = website("Packages", "");
  const app = document.getElementById("app");
  if (app) {
    app.innerHTML = htmlcode;
  } else {
    console.log("app element not found");
    return;
  }

  const styles = `.styled-list li {
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
  var styleSheet = document.createElement("style");
  styleSheet.innerText = styles;
  document.head.appendChild(styleSheet);

  filterInput = document.getElementById("filterInput") as HTMLInputElement;
  if (filterInput == null) {
    console.log("unable to add elements to app");
    return;
  }

  filterInput.addEventListener("keydown", async (e) => {
    switch (e.key) {
      case "ArrowUp":
        console.log("Up");
      case "ArrowDown":
        console.log("Down");
      case "Enter":
        console.log("Enter");
        logseq.hideMainUI({ restoreEditingCursor: true });
        await logseq.Editor.insertAtEditingCursor("put stuff here");
    }
    e.preventDefault();
  });

  document.addEventListener(
    "keydown",
    function (e) {
      console.log(e);
      if (e.key === "ESC") {
        logseq.hideMainUI({ restoreEditingCursor: true });
      }
      e.stopPropagation();
    },
    false
  );

  document.addEventListener("click", (e) => {
    if (!(e.target as HTMLElement).closest(".emoji-picker__wrapper")) {
      logseq.hideMainUI({ restoreEditingCursor: true });
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
    const x = pos ? pos.rect.x : 300;
    const y = pos ? pos.rect.y : 300;
    await showUI(x, y);
  });
}

logseq.ready(main).catch(console.error);
