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
var commentField: HTMLTextAreaElement;
var listIDs: Array<number>;
var openProjectURL = "";
var useComment: boolean = false;

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

function opWorkpackageToString(wp: WorkPackageModel): string {
  return (
    "ID" + wp.id! + ": " + wp.subject + " [" + wp._links.project.title + "]"
  );
}

function opWorkpackageToLogseqEntry(wp: WorkPackageModel): string {
  return (
    "[" +
    "ID" +
    wp.id! +
    " " +
    wp.subject +
    "](" +
    openProjectURL +
    "/work_packages/" +
    wp.id! +
    ") " +
    "[[" +
    wp._links.project.title +
    "]] " +
    "#OpenProject"
  );
}

function website(text: string, tasks: string = ""): string {
  return `
  <div class="rounded">
    <div class="maindiv">
      <div class="headline">${text}</div>
      <div class="listContainer">
        <input class="filterInput" type="text" id="filterInput" 
              placeholder="type to filter ..."/>
        <ul class="styled-list" id="listContainer"></ul>
        <textarea style="display: none;" class="filterInput" rows="5" 
                  id="commentField"
                  placeholder="type comment ..."></textarea>
        </div>
    </div>
  </div>
  `;
}

function checkMatches(item: WorkPackageModel): boolean {
  var result = true;
  const filterText = filterInput.value.toLowerCase();
  // for each substring of filterText, check individually
  const itemtext =
    item.id +
    item.subject.toLowerCase() +
    item._links.project.title?.toLowerCase();
  filterText.split(" ").forEach((text) => {
    if (text.length > 0 && !itemtext.includes(text)) {
      result = false;
    }
  });
  return result;
}

function updateFilteredList(): void {
  listContainer.innerHTML = "";
  listIDs = [];
  const filteredItems = myWorkPackages.filter(checkMatches);
  console.log(filteredItems);
  filteredItems.forEach((item) => {
    const listItem = document.createElement("li");
    listItem.textContent = opWorkpackageToString(item);
    listContainer.appendChild(listItem);
    listIDs.push(item.id!);
  });
  // reset selection
  if (listContainer.childElementCount == 0) {
    selectedElement = -1;
  } else {
    // auto-select first entry when this makes sense
    selectedElement = 0;
    listContainer.children[selectedElement].classList.add("highlighted");
  }
}

function createUI(): void {
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
  commentField = document.getElementById("commentField") as HTMLTextAreaElement;

  if (filterInput == null || listContainer == null || commentField == null) {
    console.log("unable to add elements to app");
    return;
  }

  filterInput.addEventListener("input", updateFilteredList);
  filterInput.addEventListener("keydown", async (e) => {
    // console.log(e);
    const oldSelectedElement = selectedElement;
    const numChilds = listContainer.childElementCount;
    switch (e.key) {
      case "ArrowUp":
        if (numChilds == 0) return;
        if (selectedElement == -1) {
          selectedElement = 0;
        } else if (selectedElement != 0) {
          selectedElement -= 1;
        }
        e.preventDefault();
        break;
      case "ArrowDown":
        if (numChilds == 0) return;
        if (selectedElement == -1) {
          selectedElement = 0;
        } else if (selectedElement >= numChilds - 1) {
          selectedElement = numChilds - 1;
        } else {
          selectedElement += 1;
        }
        e.preventDefault();
        break;
      case "Enter":
        // if comment is used and comment is empty
        // jump to comment first
        if (useComment && commentField.value.length == 0) {
          commentField.focus();
          commentField.select();
          break;
        }
        logseq.hideMainUI({ restoreEditingCursor: true });
        if (selectedElement != -1) {
          const id = listIDs[selectedElement];
          const wp = myWorkPackages.find((wp) => wp.id == id);
          if (wp) {
            await logseq.Editor.insertAtEditingCursor(
              opWorkpackageToLogseqEntry(wp)
            );
          }
        }
        e.preventDefault();
        break;
      case "Escape":
        logseq.hideMainUI({ restoreEditingCursor: true });
        e.preventDefault();
        break;
    }
    if (selectedElement != oldSelectedElement) {
      if (oldSelectedElement != -1) {
        listContainer.children[oldSelectedElement].classList.remove(
          "highlighted"
        );
      }
      listContainer.children[selectedElement].classList.add("highlighted");
    }
  });

  commentField.addEventListener("keydown", async (e) => {
    switch (e.key) {
      case "Enter":
        // if task is selected and non empty comment
        // -> submit
        if (selectedElement != -1 && commentField.value.length > 0) {
          logseq.hideMainUI({ restoreEditingCursor: true });
          const id = listIDs[selectedElement];
          const wp = myWorkPackages.find((wp) => wp.id == id);
          if (wp) {
            await logseq.Editor.insertAtEditingCursor(
              opWorkpackageToLogseqEntry(wp)
            );
            const currentBlock = await logseq.Editor.getCurrentBlock();
            if (currentBlock) {
              const newBlock = await logseq.Editor.insertBlock(
                currentBlock.uuid,
                commentField.value,
                {
                  sibling: true,
                }
              );
              if (newBlock) {
                await logseq.Editor.moveBlock(
                  newBlock.uuid,
                  currentBlock.uuid,
                  { children: true }
                );
              }
            }
          }
        }
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
    useComment = false;
    commentField.style.display = "none";
    await showUI(x, y);
  });
  logseq.Editor.registerSlashCommand("openproject_comment", async () => {
    const pos = await logseq.Editor.getEditingCursorPosition();
    console.log(pos);
    const x = pos ? pos.left + pos.rect.left : 300;
    const y = pos ? pos.top + pos.rect.top : 300;
    useComment = true;
    commentField.style.display = "block";
    await showUI(x, y);
  });
}

logseq.ready(main).catch(console.error);
