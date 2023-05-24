// This is the scss entry file
import "../styles/index.scss";
import "../styles/dashboard.scss";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "@fortawesome/fontawesome-free/js/all.js";
import "preline";
import "css.gg/icons/all.css";
import "sortable-tablesort/sortable.min.css";
import "sortable-tablesort/sortable.min.js";
// eslint-disable-next-line no-unused-vars
import Chart from "chart.js/auto";

window.document.addEventListener("DOMContentLoaded", function () {
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
