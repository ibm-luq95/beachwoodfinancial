"use strict";

import { fetchUrlPathByName, sendRequest } from "../../utils/apis/apis";
import { FETCHURLNAMEURL } from "../../utils/constants";
import Chart, { elements } from "chart.js/auto";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const mgDashboardHWidgetElements = document.querySelectorAll(".mg-dashboard-h-widget");
  //data-widget-name="jobs"
  //dashboard:manager:management_api:management-dashboard-api
  if (mgDashboardHWidgetElements.length > 0) {
    const urlName = fetchUrlPathByName(
      "dashboard:manager:management_api:management-dashboard-api",
    );
    urlName
      .then((data) => {
        const requestOptions = {
          method: "POST",
          // dataToSend: formInputs,
          url: data["urlPath"],
        };
        const request = sendRequest(requestOptions);
        request
          .then((newData) => {
            // console.log(newData);
            //[ "jobs_count", "clients_count", "assignments_counts", "staff_users_count" ]
            mgDashboardHWidgetElements.forEach((element) => {
              const widgetName = element.dataset["widgetName"];
              const loaderElement = element.querySelector(".loader-element");
              loaderElement.classList.add("hidden");
              // console.log(element);
              switch (widgetName) {
                case "jobs":
                  element.textContent = newData["jobs_count"];
                  break;
                case "clients":
                  element.textContent = newData["clients_count"];
                  break;
                case "assignments":
                  element.textContent = newData["assignments_counts"];
                  break;
                case "staff":
                  element.textContent = newData["staff_users_count"];
                  break;
                default:
                  break;
              }
            });
            // setup chartjs
            const chartDashboardWrapper = document.querySelector(
              "#chart-dashboard-wrapper",
            );
            const chartLoader = chartDashboardWrapper.querySelector(".loader-element");
            const jobChartWrapper =
              chartDashboardWrapper.querySelector("#jobChartWrapper");
            // console.log(chartLoader);
            // console.log(jobChartWrapper);
            chartLoader.classList.add("hidden");
            jobChartWrapper.classList.remove("hidden");
            const jobsChart = document.querySelector("canvas#jobsChart");
            if (jobsChart) {
              const chart = new Chart(jobsChart, {
                type: "doughnut",

                data: {
                  labels: ["Past due", "Completed", "In progress"],
                  datasets: [
                    {
                      backgroundColor: ["#EF4444", "#22C55E", "#EAB308"],
                      data: [
                        newData["jobs_statistics"]["past_due_jobs_count"],
                        newData["jobs_statistics"]["completed_jobs_count"],
                        newData["jobs_statistics"]["in_progress_jobs_count"],
                      ],
                    },
                  ],
                },
                options: {
                  maintainAspectRation: true,
                  responsive: true,
                  aspectRatio: 2,

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
          })
          .catch((error) => {
            console.error(error);
          });
      })
      .catch((error) => {
        console.error(error);
      });
  }
});
