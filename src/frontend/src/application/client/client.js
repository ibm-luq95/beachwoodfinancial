// "use strict";

// document.addEventListener("DOMContentLoaded", (readyEvent) => {
//   const clientDetailsDropdownItems = document.querySelectorAll(
//     "a.client-details-dropdown-item",
//   );

//   if (clientDetailsDropdownItems.length > 0) {
//     clientDetailsDropdownItems.forEach((item) => {
//       item.addEventListener("click", (event) => {
//         const currentTarget = event.currentTarget;
//         const modalName = currentTarget.dataset["modalName"];
//         const $jobModal = document.querySelector("#createJobModal");
//         switch (modalName) {
//           case "job":
//             console.warn("Open job modal");
//             console.log($jobModal);
//             window.HSOverlay.open($jobModal);
//             break;

//           default:
//             break;
//         }
//       });
//     });
//   }
// });
