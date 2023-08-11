"use strict";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const createTaskModalForm = document.querySelector("form#createTaskForm");
  if (createTaskModalForm) {
    const fieldset = createTaskModalForm.querySelector("fieldset");
    createTaskModalForm.addEventListener("submit", (event) => {
      event.preventDefault();
      fieldset.disabled = true;
      alert("create task");
    });
  }
});
