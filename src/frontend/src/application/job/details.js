"use strict";

import { sendRequest } from "../../utils/apis/apis";
import { CSRFINPUTNAME } from "../../utils/constants";
import {
  disableAndEnableFieldsetItems,
  formInputSerializer,
} from "../../utils/form_helpers";
// import { bwI18Helper } from "../../utils/i18_helper";
import { showToastNotification } from "../../utils/toasts";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const updateJobStatusBtn = document.querySelector("button#updateJobStatusBtn");
  const addDiscussionFormInJob = document.querySelector("form#addDiscussionFormInJob");
  const updateJobForm = document.querySelector("form#updateJobForm");
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

    if (updateJobForm) {
      updateJobForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const currentTarget = event.currentTarget;
        const fieldset = currentTarget.querySelector("fieldset");
        const formInputs = formInputSerializer({
          formElement: currentTarget,
          excludedFields: ["_method"],
        });
        disableAndEnableFieldsetItems({ formElement: updateJobForm, state: "disable" });
        const requestOptions = {
          method: currentTarget["_method"]
            ? currentTarget["_method"].value.toUpperCase()
            : "POST",
          dataToSend: formInputs,
          url: currentTarget.action,
          token: currentTarget[CSRFINPUTNAME].value,
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            // console.log(bwI18Helper.t("jobs"));
            // showToastNotification(bwI18Helper.t("key"), "success");
            showToastNotification("Job updated successfully", "success");
            setTimeout(() => {
              window.location.reload();
            }, 1500);
          })
          .catch((error) => {
            console.error(error);
            showToastNotification(`${JSON.stringify(error["user_error_msg"])}`, "danger");
          })
          .finally(() => {
            disableAndEnableFieldsetItems({
              formElement: updateJobForm,
              state: "enable",
            });
          });
      });
    }
  }
});
