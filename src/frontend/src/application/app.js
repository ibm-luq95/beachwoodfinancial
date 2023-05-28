// This is the scss entry file
import "../styles/index.scss";
import "../styles/dashboard.scss";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "@fortawesome/fontawesome-free/js/all.js";
import "preline";
import "css.gg/icons/all.css";
// import "sortable-tablesort/sortable-base.css";
// import "sortable-tablesort/sortable.min.js";
import tableSort from "table-sort-js/table-sort.js";
// eslint-disable-next-line no-unused-vars
import Chart from "chart.js/auto";

window.document.addEventListener("DOMContentLoaded", function () {
  const bwfInputs = document.querySelectorAll(".bw-input");
  const bwDisabledLinks = document.querySelectorAll("a.bw-disabled-anchor");
  const allDisabledCssClassed = ["disabled:opacity-75", "cursor-not-allowed"];
  bwfInputs.forEach((input) => {
    input.disabled = false;
    input.classList.remove(...allDisabledCssClassed);
  });
  bwDisabledLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();
    });
  });
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
});
