"use strict";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const updateJobStatusBtn = document.querySelector("button#updateJobStatusBtn");
  const addDiscussionFormInJob = document.querySelector("form#addDiscussionFormInJob");
  if (updateJobStatusBtn) {
    updateJobStatusBtn.addEventListener("click", (event) => {
      const jobStatusInput = document.querySelector("input#job-status-input");
      console.log(jobStatusInput.value);
    });

    if (addDiscussionFormInJob) {
      addDiscussionFormInJob.addEventListener("submit", (event) => {
        event.preventDefault();
        console.log("Add reply");
      });
    }
  }
});
