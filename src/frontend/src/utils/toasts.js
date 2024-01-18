"use strict";

import { TOASTSTIMEOUTSECS } from "./constants";
import { getIconForToasts } from "./icons";

/**
 * This will display notification message
 * @param {string} msg the message in the notification
 * @param {string} notificationType notification message type
 */
const showToastNotification = (msg, notificationType = "success") => {
  const toastsWrapperElement = document.querySelector("div#toasts-wrapper");
  console.log(toastsWrapperElement);
  const iconWrapper = toastsWrapperElement.querySelector("div#iconWrapper");
  const msgElement = toastsWrapperElement.querySelector("p#msg");
  msgElement.textContent = msg;
  const color = getIconForToasts(notificationType);
  iconWrapper.innerHTML = color["icon"];

  toastsWrapperElement.classList.remove("hidden");
  toastsWrapperElement.classList.add(
    ...["animate__animated", "animate__fadeInRight", "animate__faster"],
  );

  setTimeout(() => {
    toastsWrapperElement.classList.add(...["animate__animated", "animate__fadeOutRight"]);
  }, TOASTSTIMEOUTSECS);
  toastsWrapperElement.classList.remove(...["animate__fadeOutRight"]);
  // setTimeout(() => {
  //   toastsWrapperElement.classList.remove(
  //     ...["animate__animated", "animate__fadeInRight", "animate__faster"],
  //   );
  //   toastsWrapperElement.classList.add("hidden");
  // }, TOASTSTIMEOUTSECS + 500);
};

export { showToastNotification };
