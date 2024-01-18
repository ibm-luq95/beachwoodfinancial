"use strict";

import { bwCleanApiError } from "../../utils/apis/clean_errors";
import { UploadFileRequest } from "../../utils/apis/upload_file";
import { CSRFINPUTNAME, SUCCESSTIMEOUTSECS } from "../../utils/constants";
import { formInputSerializer } from "../../utils/form_helpers";
import { showToastNotification } from "../../utils/toasts";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const createAssignmentForm = document.querySelector("form#createAssignmentForm");
  if (createAssignmentForm) {
    const fieldset = createAssignmentForm.querySelector("fieldset");
    try {
      createAssignmentForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const currentTarget = event.currentTarget;

        const formInputs = formInputSerializer({
          formElement: currentTarget,
          excludedFields: ["_method", "attachment"],
          returnAsFormData: true,
          filesArray: ["attachment"],
        });
        // console.log(formInputs);
        fieldset.disabled = true;
        // console.log(getCookie("csrftoken"));
        const uploadRequest = new UploadFileRequest(
          currentTarget.action,
          formInputs,
          currentTarget.elements[CSRFINPUTNAME].value,
          currentTarget.method,
          false,
        );
        const request = uploadRequest.sendRequest();
        request
          .then((data) => {
            console.log(data);
            showToastNotification("Assignment created successfully!", "success");
            setTimeout(() => {
              window.location.reload();
            }, SUCCESSTIMEOUTSECS);
          })
          .catch((error) => {
            const er = bwCleanApiError(error);
            if (er) {
              er.forEach((erElement) => {
                showToastNotification(
                  `Error: ${erElement["detail"]} - ${erElement["attr"]}`,
                  "danger",
                );
              });
            } else {
              showToastNotification("Error while add new assignment!", "error");
            }
            console.error(error);
          })
          .finally(() => {});
      });
    } catch (error) {
      console.error(error);
      showToastNotification("Error while add new assignment!", "error");
      throw new Error(error);
    } finally {
      fieldset.disabled = false;
    }
  }
});
