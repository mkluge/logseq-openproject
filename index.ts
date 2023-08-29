/*
Copyright (C) 2023, Michael Kluge, vollseil@mailbox.org

This program is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public 
License along with this program. If not, see 
<https://www.gnu.org/licenses/>.
*/

import "@logseq/libs";
import { settingsUI } from "./settings";
import {
  Configuration,
  WorkPackagesApi,
  UsersApi,
  WorkPackagesApiCommentWorkPackageRequest,
  WorkPackagesApiListWorkPackagesRequest,
  WorkPackageModel,
  TypesApi,
} from "./openproject_api";

let myWorkPackages: WorkPackageModel[];
let usersApi: UsersApi = new UsersApi();
let workPackagesApi: WorkPackagesApi = new WorkPackagesApi();
let typesApi: TypesApi = new TypesApi();
let myself: number;
let selectedElement: number = -1;
let filterInput: HTMLInputElement;
let listContainer: HTMLLIElement;
let commentField: HTMLTextAreaElement;
let listIDs: Array<number>;
const typeMap: Map<string, number> = new Map();
let openProjectURL = "";
let useComment: boolean = false;
let filterType: string = "";

async function updateWorkPackages() {
  console.log("update work packages");
  // FIXME: would like to call listWorkPackages with the filter
  //        but it throws a server error, probably incorrect usage
  //        of this feature
  const filter = [{ assignee: { operator: "=", values: [myself] } }];
  if (filterType.length > 0) {
    const typeID = typeMap[filterType];
    filter.push({ type: { operator: "=", values: [typeID] } });
  }
  //const filter = {
  //  filters: JSON.stringify(filterMyself),
  //};
  const listOptions: WorkPackagesApiListWorkPackagesRequest = {
    pageSize: 20000,
    filters: JSON.stringify(filter),
  };
  const workPackages = await workPackagesApi.listWorkPackages(listOptions);
  console.log(workPackages.data._embedded.elements);
  myWorkPackages = workPackages.data._embedded.elements;
  //myWorkPackages = workPackages.data._embedded.elements.filter(
  //  (wp) => wp._links.assignee?.title == myself
  //);
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

function website(text: string): string {
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
  let result = true;
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

async function submitData() {
  logseq.hideMainUI({ restoreEditingCursor: true });
  const id = listIDs[selectedElement];
  const wp = myWorkPackages.find((wp) => wp.id == id);
  if (wp) {
    await logseq.Editor.insertAtEditingCursor(opWorkpackageToLogseqEntry(wp));
    if (useComment) {
      // add comment as child block
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
          await logseq.Editor.moveBlock(newBlock.uuid, currentBlock.uuid, {
            children: true,
          });
        }
      }
      // add comment to work package in OpenProject
      const newComment: WorkPackagesApiCommentWorkPackageRequest = {
        id: id,
        notify: true,
        commentWorkPackageRequest: {
          comment: {
            raw: commentField.value,
          },
        },
      };
      await workPackagesApi.commentWorkPackage(newComment);
    }
  }
}

function createUI(): void {
  const htmlcode = website("Select OpenProject Task");
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
        submitData();
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
          submitData();
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
  let openProjectToken = "";

  const loadSettings = () => {
    if (logseq.settings) {
      openProjectToken = logseq.settings["OpenProjectToken"];
      openProjectURL = logseq.settings["OpenProjectURL"];
      filterType = logseq.settings[""];
      const openProjectConfiguration = new Configuration({
        basePath: openProjectURL,
        username: "apikey",
        password: openProjectToken,
      });
      usersApi = new UsersApi(openProjectConfiguration);
      workPackagesApi = new WorkPackagesApi(openProjectConfiguration);
      typesApi = new TypesApi(openProjectConfiguration);
    }
  };

  loadSettings();
  logseq.onSettingsChanged(loadSettings);
  createUI();

  console.log("loaded config with URL " + openProjectURL);
  // get my name in OpenProject
  const me = await usersApi.viewUser({
    id: "me",
  });
  console.log(me);
  if (me.status != 200) {
    console.log("Error unable to read user data");
    return;
  }
  myself = me.data.id;

  const response = await typesApi.listAllTypes();
  typeMap.clear();
  // type not well defined
  response.data._embedded.elements.map((el) => {
    typeMap[el.name] = el.id;
  });
  settingsUI(Array.from(typeMap.keys()));

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
