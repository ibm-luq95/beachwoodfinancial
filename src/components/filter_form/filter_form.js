/* "use strict";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const resetFilterBtn = document.querySelector("a#resetFilterBtn");
  if (resetFilterBtn) {
    resetFilterBtn.addEventListener("click", (event) => {
      event.preventDefault();
      const formId = event.currentTarget.dataset["form"];
      if (formId !== null || formId !== "None") {
        const filterForm = document.querySelector(`form#${formId}`);
        console.log(filterForm);
        if (filterForm) {
          filterForm.reset();
        }
      }
    });
  }
});
 */