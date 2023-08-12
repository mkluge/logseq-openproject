// import { ProjectModel } from "./openproject_api/api";
import "@logseq/libs";

function main() {

  logseq.provideModel({
    openCalendar () {
      console.log("hi, calendar");
    },
  });
  logseq.Editor.registerSlashCommand("openproject", async () => {
    logseq.provideUI({
      key: 'miktest',
      template: `
        <button
        class="pomodoro-timer-btn is-start"
        data-on-click="openCalendar">
        Go Calendar
        </button>
      `,
    })
  });
}

logseq.ready(main).catch(console.error);
