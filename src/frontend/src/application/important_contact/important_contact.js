"use strict";

import { sendRequest } from "../../utils/apis/apis";
import { CSRFINPUTNAME, SUCCESSTIMEOUTSECS } from "../../utils/constants";
import {
  disableAndEnableFieldsetItems,
  formInputSerializer,
} from "../../utils/form_helpers";
import { showToastNotification } from "../../utils/toasts";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const createImportantContactModalElement = document.querySelector(
    "div#createImportantContactModal",
  );
  if (createImportantContactModalElement) {
    const createImportantContactForm = createImportantContactModalElement.querySelector(
      "form#createImportantContactForm",
    );
    if (createImportantContactForm) {
      createImportantContactForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const currentTarget = event.currentTarget;
        const formInputs = formInputSerializer({
          formElement: currentTarget,
          excludedFields: ["_method"],
        });
        disableAndEnableFieldsetItems({
          formElement: createImportantContactForm,
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
            showToastNotification("Contact created successfully", "success");
            setTimeout(() => {
              window.location.reload();
            }, SUCCESSTIMEOUTSECS);
          })
          .catch((error) => {
            console.error(error);
            showToastNotification(`${error["errors"].toString()}`, "error");
            disableAndEnableFieldsetItems({
              formElement: createImportantContactForm,
              state: "enable",
            });
          })
          .finally(() => {
            disableAndEnableFieldsetItems({
              formElement: createImportantContactForm,
              state: "enable",
            });
          });
      });
    }
  }
});
