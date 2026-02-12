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
import axios from "axios";
import { settingsUI } from "./settings";

type GitLabIssue = {
  id: number;
  iid: number;
  project_id: number;
  title: string;
  web_url: string;
  labels: string[];
  state: string;
};

let myIssues: GitLabIssue[] = [];
let selectedElement: number = -1;
let filterInput: HTMLInputElement;
let listContainer: HTMLLIElement;
let commentField: HTMLTextAreaElement;
let listIDs: Array<number> = [];
let gitlabUrl = "";
let gitlabToken = "";
let projectIdsFilter: number[] = [];
let labelFilter: string[] = [];
let stateFilter: "opened" | "closed" | "all" = "opened";
let useComment: boolean = false;
async function updateIssues() {
  console.log("update gitlab issues");
  try {
    const params: Record<string, string | number | boolean> = {
      scope: "assigned_to_me",
      per_page: 100,
    };
    if (stateFilter !== "all") {
      params.state = stateFilter;
    }
    if (labelFilter.length > 0) {
      params.labels = labelFilter.join(",");
    }

    const issues: GitLabIssue[] = [];
    let page = 1;
    while (true) {
      const response = await axios.get(`${gitlabUrl}/api/v4/issues`, {
        headers: {
          "PRIVATE-TOKEN": gitlabToken,
        },
        params: {
          ...params,
          page,
        },
      });
      if (!Array.isArray(response.data) || response.data.length === 0) {
        break;
      }
      issues.push(...response.data);
      page += 1;
      if (response.data.length < 100) {
        break;
      }
    }

    if (projectIdsFilter.length > 0) {
      myIssues = issues.filter((issue) =>
        projectIdsFilter.includes(issue.project_id)
      );
    } else {
      myIssues = issues;
    }
  } catch (error) {
    console.error("Fehler beim Abrufen der GitLab Issues:", error);
    myIssues = [];
  }
}

function gitlabIssueToString(issue: GitLabIssue): string {
  return `#${issue.iid}: ${issue.title} [${issue.project_id}]`;
}

function gitlabIssueToLogseqEntry(issue: GitLabIssue): string {
  return `[#${issue.iid} ${issue.title}](${issue.web_url}) #GitLab`;
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

function checkMatches(item: GitLabIssue): boolean {
  let result = true;
  const filterText = filterInput.value.toLowerCase();
  // for each substring of filterText, check individually
  const itemtext =
    item.iid +
    item.title.toLowerCase() +
    String(item.project_id);
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
  const filteredItems = myIssues.filter(checkMatches);
  console.log(filteredItems);
  filteredItems.forEach((item) => {
    const listItem = document.createElement("li");
    listItem.textContent = gitlabIssueToString(item);
    listContainer.appendChild(listItem);
    listIDs.push(item.id);
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
  const issue = myIssues.find((issue) => issue.id == id);
  if (issue) {
    await logseq.Editor.insertAtEditingCursor(
      gitlabIssueToLogseqEntry(issue)
    );
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
      // add comment to GitLab issue
      await axios.post(
        `${gitlabUrl}/api/v4/projects/${issue.project_id}/issues/${issue.iid}/notes`,
        {
          body: commentField.value,
        },
        {
          headers: {
            "PRIVATE-TOKEN": gitlabToken,
          },
        }
      );
    }
  }
}

function createUI(): void {
  const htmlcode = website("Select GitLab Issue");
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
  await updateIssues();
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

async function loadSettings(): void {
  if (logseq.settings) {
    gitlabToken = logseq.settings["GitLabToken"] || "";
    gitlabUrl = logseq.settings["GitLabURL"] || "";
    const projectIdsRaw = logseq.settings["GitLabProjectIds"] || "";
    projectIdsFilter = projectIdsRaw
      .split(",")
      .map((value: string) => Number(value.trim()))
      .filter((value: number) => !Number.isNaN(value) && value > 0);
    const labelsRaw = logseq.settings["GitLabLabelFilter"] || "";
    labelFilter = labelsRaw
      .split(",")
      .map((value: string) => value.trim())
      .filter((value: string) => value.length > 0);
    stateFilter =
      (logseq.settings["GitLabState"] as "opened" | "closed" | "all") ||
      "opened";
    console.log("loaded config with URL " + gitlabUrl);
  }

  settingsUI();
}

async function main() {
  loadSettings();
  logseq.onSettingsChanged(loadSettings);
  createUI();

  logseq.Editor.registerSlashCommand("gitlab", async () => {
    const pos = await logseq.Editor.getEditingCursorPosition();
    console.log(pos);
    const x = pos ? pos.left + pos.rect.left : 300;
    const y = pos ? pos.top + pos.rect.top : 300;
    useComment = false;
    commentField.style.display = "none";
    await showUI(x, y);
  });
  logseq.Editor.registerSlashCommand("gitlab_comment", async () => {
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
