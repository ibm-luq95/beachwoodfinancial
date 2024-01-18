"use strict";

import { bwCleanApiError } from "../../utils/apis/clean_errors";
import { UploadFileRequest } from "../../utils/apis/upload_file";
import { CSRFINPUTNAME, SUCCESSTIMEOUTSECS } from "../../utils/constants";
import {
  disableAndEnableFieldsetItems,
  formInputSerializer,
} from "../../utils/form_helpers";
import { showToastNotification } from "../../utils/toasts";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const updateClientForm = document.querySelector("form#updateClientForm");
  if (updateClientForm) {
    updateClientForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
      const fieldset = currentTarget.querySelector("fieldset");
      const formInputs = formInputSerializer({
        formElement: currentTarget,
        excludedFields: ["_method", "company_logo"],
        returnAsFormData: true,
        filesArray: ["company_logo"],
      });
      disableAndEnableFieldsetItems({
        formElement: updateClientForm,
        state: "disable",
      });
      const uploadRequest = new UploadFileRequest(
        currentTarget.action,
        formInputs,
        currentTarget.elements[CSRFINPUTNAME].value,
        currentTarget["_method"].value.toUpperCase(),
        false,
      );
      const request = uploadRequest.sendRequest();
      request
        .then((data) => {
          console.log(data);
          showToastNotification(`Client updated successfully!`, "success");
          setTimeout(() => {
            window.location.reload();
          }, SUCCESSTIMEOUTSECS);
        })
        .catch((error) => {
          console.error(error);
          const er = bwCleanApiError(error);
          if (er) {
            er.forEach((erElement) => {
              showToastNotification(
                `Error: ${erElement["detail"]} - ${erElement["attr"]}`,
                "danger",
              );
            });
          } else {
            showToastNotification("Error update client!", "error");
          }
        })
        .finally(() => {
          disableAndEnableFieldsetItems({
            formElement: updateClientForm,
            state: "enable",
          });
        });
    });
  }
});
