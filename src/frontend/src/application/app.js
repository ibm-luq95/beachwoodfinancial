// This is the scss entry file

import "../styles/index.scss";
import "../styles/dashboard.scss";
import "preline";
// import "../styles/tinymce.scss";
// import * as editor from "../utils/rich_editor.js";
import "../utils/rich_editor.js";
import "animate.css";
import "@fortawesome/fontawesome-free/js/all.js";
import "@fortawesome/fontawesome-free/css/all.min.css";

// import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
// import "css.gg/icons/all.css";
// import "css.gg/icons/css/al"
import tableSort from "table-sort-js/table-sort.js";
// eslint-disable-next-line no-unused-vars
import Chart from "chart.js/auto";

import "./job/details.js";
import "./special_assignment/details.js";
import "./special_assignment/special_assignment.js";
import "./task/task.js";
import "./document/document.js";
import "./note/note.js";
import "./discussion/discussion.js";
import "./job/job.js";
import "./important_contact/important_contact.js";
import "./client/client.js";
import "./client_account/client_account.js";
import "./client_account/credentials_inputs.js";
import "./beach_wood_user/details.js";
import { setFormInputsReadOnly } from "../utils/form_helpers";

window.document.addEventListener("DOMContentLoaded", function () {
  const bwfInputs = document.querySelectorAll(".bw-input");
  const bwDisabledLinks = document.querySelectorAll("a.bw-disabled-anchor");
  const allDisabledCssClassed = ["disabled:opacity-75", "cursor-not-allowed"];
  const readonlySelectElements = document.querySelectorAll(".readonly-select");
  if (readonlySelectElements.length > 0) {
    readonlySelectElements.forEach((element) => {
      element.addEventListener("change", (event) => {
        return false;
      });
    });
  }
  // TODO: temporary set it to readonly
  setFormInputsReadOnly("staffUpdateMiniForm");

  bwfInputs.forEach((input) => {
    const dataAttrs = input.dataset;
    const checkKeepDisabled = Object.prototype.hasOwnProperty.call(
      dataAttrs,
      "keepDisabled",
    );
    if (checkKeepDisabled === true) {
      const keepDisabled = dataAttrs["keepDisabled"];
      const keepDisabledValue = /true/.test(keepDisabled);
      if (keepDisabledValue === true) {
        input.disabled = true;
      }
    } else {
      input.disabled = false;
      input.classList.remove(...allDisabledCssClassed);
    }
  });
  bwDisabledLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
    });
  });
  const formBackBtn = document.querySelector("button#formBackBtn");
  if (formBackBtn) {
    formBackBtn.addEventListener("click", (event) => {
      window.history.back();
    });
  }
  const jobsChart = document.querySelector("canvas#jobsChart");
  if (jobsChart) {
    const options2 = {
      type: "pie",
      data: {
        labels: ["Africa", "Asia", "Europe", "Latin America", "North America"],
        datasets: [
          {
            label: "Population (millions)",
            backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
            data: [2478, 5267, 734, 784, 433],
          },
        ],
      },
      options: {
        title: {
          display: true,
          text: "Predicted world population (millions) in 2050",
        },
      },
    };
    const chart = new Chart(jobsChart, {
      type: "doughnut",

      data: {
        labels: ["Past due", "Completed", "In progress"],
        datasets: [
          {
            backgroundColor: ["#EF4444", "#22C55E", "#EAB308"],
            data: [2478, 5267, 734],
          },
        ],
      },
      options: {
        maintainAspectRation: true,
        responsive: true,

        plugins: {
          title: {
            display: true,
            text: "Jobs",
          },
          legend: {
            display: false,
          },
        },
      },
    });
  }

  // Modal Events
  /* const mo = document.querySelector("#hs-static-backdrop-modal");
  mo.addEventListener("open.hs.overlay", (evt) => {
    // console.log(evt);
    console.log("open");
  });
  mo.addEventListener("close.hs.overlay", (evt) => {
    // console.log(evt);
    console.log("Close");
  }); */
});
