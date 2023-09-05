"use strict";
import { sendRequest } from "../../utils/apis/apis";
import { CSRFINPUTNAME } from "../../utils/constants";
import {
  disableAndEnableFieldsetItems,
  formInputSerializer,
} from "../../utils/form_helpers";
import { showToastNotification } from "../../utils/toasts";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const createTaskModalForm = document.querySelector("form#createTaskForm");
  if (createTaskModalForm) {
    const fieldset = createTaskModalForm.querySelector("fieldset");
    createTaskModalForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
      const formInputs = formInputSerializer({
        formElement: currentTarget,
        excludedFields: ["_method"],
      });
      disableAndEnableFieldsetItems({
        formElement: createTaskModalForm,
        state: "disable",
      });
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
          showToastNotification("Task created successfully", "success");
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
            formElement: createTaskModalForm,
            state: "enable",
          });
        });
    });
  }
});
