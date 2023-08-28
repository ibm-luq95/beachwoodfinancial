"use strict";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const assignedClientsForm = document.querySelector("form#assignedClientsForm");
  if (assignedClientsForm) {
    assignedClientsForm.addEventListener("submit", (event) => {
      event.preventDefault();
      const currentTarget = event.currentTarget;
    });
  }
});
