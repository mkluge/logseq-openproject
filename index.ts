// import { ProjectModel } from "./openproject_api/api";
import "@logseq/libs";

function main() {

  logseq.provideModel({
    openCalendar () {
      console.log("hi, calendar");
      console.log(document.getElementById('tryFindMe'));
      console.log(document.getElementById('app')?.childNodes);
    },
  });
  logseq.Editor.registerSlashCommand("openproject", async () => {
    logseq.provideUI({
      key: 'miktest',
      template: `
        <button
        id="tryFindMe"
        data-on-click="openCalendar">
        Go Calendar
        </button>
      `,
    })
  });
}

logseq.ready(main).catch(console.error);
