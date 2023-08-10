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


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>String Filter Popup</title>
  <style>
    /* Styles for the popup */
    .popup-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: rgba(0, 0, 0, 0.5);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1000;
    }
    .popup {
      background-color: white;
      padding: 20px;
      border-radius: 5px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    }
  </style>
</head>
<body>
  <!-- Button to open the popup -->
  <button id="openButton">Open Popup</button>

  <!-- Popup container (hidden by default) -->
  <div class="popup-container" id="popupContainer" style="display: none;">
    <div class="popup">
      <input type="text" id="filterInput" placeholder="Filter...">
      <div id="listContainer"></div>
    </div>
  </div>

  <script>
    const openButton = document.getElementById('openButton');
    const popupContainer = document.getElementById('popupContainer');
    const inputField = document.getElementById('filterInput') as HTMLInputElement;
    const listContainer = document.getElementById('listContainer');

    const itemList = ['Apple', 'Banana', 'Cherry', 'Grapes', 'Lemon', 'Orange', 'Peach', 'Strawberry'];

    function updateFilteredList() {
      const filterText = inputField.value.toLowerCase();
      listContainer.innerHTML = '';

      const filteredItems = itemList.filter(item => item.toLowerCase().includes(filterText));

      filteredItems.forEach(item => {
        const listItem = document.createElement('div');
        listItem.textContent = item;
        listContainer.appendChild(listItem);
      });
    }

    inputField.addEventListener('input', updateFilteredList);

    // Open the popup when the button is clicked
    openButton.addEventListener('click', () => {
      popupContainer.style.display = 'flex';
      updateFilteredList();
    });

    // Close the popup when the ESC key is pressed
    window.addEventListener('keydown', event => {
      if (event.key === 'Escape') {
        popupContainer.style.display = 'none';
      }
    });
  </script>
</body>
</html>


// Get references to the input field and the list container in your HTML
const inputField = document.getElementById('filterInput') as HTMLInputElement;
const listContainer = document.getElementById('listContainer');

// Sample list of strings
const itemList: string[] = ['Apple', 'Banana', 'Cherry', 'Grapes', 'Lemon', 'Orange', 'Peach', 'Strawberry'];

// Function to update the displayed list based on the filter
function updateFilteredList() {
  const filterText = inputField.value.toLowerCase();

  // Clear the existing list
  listContainer.innerHTML = '';

  // Filter the items based on the filter text
  const filteredItems = itemList.filter(item => item.toLowerCase().includes(filterText));

  // Display the filtered items
  filteredItems.forEach(item => {
    const listItem = document.createElement('div');
    listItem.textContent = item;
    listContainer.appendChild(listItem);
  });
}

// Attach an event listener to the input field to trigger filtering
inputField.addEventListener('input', updateFilteredList);

// Initial rendering of the list
updateFilteredList();


async function main() {

  var openProjectToken = "";
  var openProjectURL = "";
  var usersApi : UsersApi = new UsersApi();
  var workPackagesApi : WorkPackagesApi = new WorkPackagesApi();
  
  const loadSettings = () => {
    if (logseq.settings ) {
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
  }

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
  const myself: String = me.data.name;
  const filterMyself = [{ assignee: { operator: "**", values: [myself] } }];
  const filter = {
    filters: JSON.stringify(filterMyself)
  };
  // FIXME: would like to call listWorkPackages with the filter
  //        but it throws a server error, probably incorrect usage
  //        of this feature
  const workPackages = await workPackagesApi.listWorkPackages();
  const myWorkPackages = workPackages.data._embedded.elements.filter( wp => wp._links.assignee?.title == myself);
  console.log(myWorkPackages);
}

logseq.ready(main).catch(console.error);