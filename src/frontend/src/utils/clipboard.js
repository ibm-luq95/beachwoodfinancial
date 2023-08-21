"use strict";

import { capitalizedFirstLetter } from "./helpers";
import { showToastNotification } from "./toasts";

/**
 * Copy text to clipboard using native javascript api with toast notifications
 * @typedef param
 * @param {Object} param - this is object param
 * @param {string} param.textWillCopy Text will copy to clipboard
 * @param {string} param.label Label which will appear in notification
 * @param {boolean} param.isNotify If true will display notification message after copy
 * @param {string} param.notificationMsg Custom notification message not the default
 * @param {string} param.notificationType Notification type
 */
const addTxtToClipboardWithNotification = ({
  textWillCopy,
  label,
  isNotify = true,
  notificationMsg = null,
  notificationType = "success",
}) => {
  navigator.clipboard.writeText(textWillCopy);
  if (isNotify === true) {
    const msg = notificationMsg
      ? capitalizedFirstLetter(notificationMsg)
      : capitalizedFirstLetter(`${label} copied successfully!`);
    showToastNotification(msg, notificationType);
  }
};

export { addTxtToClipboardWithNotification };
