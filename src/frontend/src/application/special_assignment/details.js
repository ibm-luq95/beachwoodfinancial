"use strict";

import { UploadFileRequest } from "../../utils/apis/upload_file.js";
import { getCookie } from "../../utils/cookie.js";
import { formInputSerializer } from "../../utils/form_helpers.js";
import { showToastNotification } from "../../utils/toasts";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const replyForm = document.querySelector("form#replyForm");
  if (replyForm) {
    const fieldset = replyForm.querySelector("fieldset");
    try {
      replyForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const currentTarget = event.currentTarget;
        const isReplyCheckboxElement = currentTarget.elements["isReplyCheckbox"];
        const replyInputElement = document.querySelector("input[name='replies']:checked");

        const formInputs = formInputSerializer({
          formElement: currentTarget,
          excludedFields: ["_method", "attachment"],
          returnAsFormData: true,
          filesArray: ["attachment"],
        });
        // check if isReply checkbox checked
        if (replyInputElement) {
          if (isReplyCheckboxElement.checked === true) {
            formInputs.append("replies", replyInputElement.value);
          }
        }

        fieldset.disabled = true;
        // console.log(getCookie("csrftoken"));
        const uploadRequest = new UploadFileRequest(
          currentTarget.action,
          formInputs,
          currentTarget.elements["csrfmiddlewaretoken"].value,
          currentTarget.method,
          false,
        );
        const request = uploadRequest.sendRequest();
        request
          .then((data) => {
            console.log(data);
            showToastNotification(data, "success");
            setTimeout(() => {
                window.location.reload();
            }, 1500);
          })
          .catch((error) => {
            console.error(error);
            showToastNotification("Error while add new discussion!", "error");
          })
          .finally(() => {});
      });
    } catch (error) {
      console.error(error);
      showToastNotification("Error while add new discussion!", "error");
      throw new Error(error);
    } finally {
      fieldset.disabled = false;
    }
  }
});
