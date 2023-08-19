"use strict";

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
      });
    }
  }
});
