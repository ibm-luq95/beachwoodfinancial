"use strict";

import { sendRequest } from "../../utils/apis/apis";
import { bwCleanApiError } from "../../utils/apis/clean_errors";
import { UploadFileRequest } from "../../utils/apis/upload_file";
import { CSRFINPUTNAME, SUCCESSTIMEOUTSECS } from "../../utils/constants";
import {
  disableAndEnableFieldsetItems,
  formInputSerializer,
} from "../../utils/form_helpers";
import { showToastNotification } from "../../utils/toasts";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const createNoteForm = document.querySelector("form#createNoteForm");

  if (createNoteForm) {
    createNoteForm.addEventListener("submit", (event) => {
      try {
        event.preventDefault();
        const currentTarget = event.currentTarget;
        const formInputs = formInputSerializer({
          formElement: currentTarget,
          excludedFields: ["_method"],
        });
        disableAndEnableFieldsetItems({
          formElement: createNoteForm,
          state: "disable",
        });
        const requestOptions = {
          method: currentTarget["_method"]
            ? currentTarget["_method"].value.toUpperCase()
            : currentTarget.method,
          dataToSend: formInputs,
          url: currentTarget.action,
          token: currentTarget[CSRFINPUTNAME].value,
        };
        const request = sendRequest(requestOptions);
        request
          .then((data) => {
            // console.log(bwI18Helper.t("jobs"));
            // showToastNotification(bwI18Helper.t("key"), "success");
            showToastNotification("Note created successfully", "success");
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
              showToastNotification(`Error adding note!`, "danger");
            }
            console.error(error);
          })
          .finally(() => {
            disableAndEnableFieldsetItems({
              formElement: createNoteForm,
              state: "enable",
            });
          });
      } catch (error) {
        console.error(error);
        showToastNotification("Error while add new note!");
      } finally {
        disableAndEnableFieldsetItems({
          formElement: createNoteForm,
          state: "enable",
        });
      }
    });
  }
});
