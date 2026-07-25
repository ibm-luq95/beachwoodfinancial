"use strict";
// import Worker from "worker-loader!./notifications_worker.js";
import Worker from "./notifications_worker.js";
import { getCookie } from "../utils/cookie.js";
document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const allNotificationItems = document.querySelectorAll("a.notificationsItem");
  const setAllNotificationsReadBtn = document.querySelector(
    "button#setAllNotificationsReadBtn",
  );
  if (setAllNotificationsReadBtn) {
    setAllNotificationsReadBtn.addEventListener("click", async (event) => {
      const url = "/notifications/api/notifications/mark_all_read/";
      const token =
        document
          .querySelector('meta[name="csrf-token"]')
          ?.getAttribute("content") || getCookie("csrftoken");

      try {
        const response = await fetch(url, {
          method: "POST",
          headers: {
            Accept: "application/json",
            "X-CSRFToken": token,
          },
        });

        if (response.ok) {
          window.location.reload();
        } else {
          console.error("Failed to mark all notifications as read");
        }
      } catch (error) {
        console.error("Error marking all notifications as read:", error);
      }
    });
  }
  if (allNotificationItems.length > 0) {
    allNotificationItems.forEach((item) => {
      item.addEventListener("click", (event) => {
        // Destructure required event properties
        const { button, ctrlKey, metaKey, shiftKey, altKey, currentTarget } =
          event;

        // Ignore right-clicks or modified clicks
        if (button !== 0 || ctrlKey || metaKey || shiftKey || altKey) return;

        /** @type {HTMLAnchorElement} */
        const anchor = currentTarget;
        const { href, dataset } = anchor;

        // Validate href
        if (!href || href.startsWith("javascript:")) return;

        // Prevent default navigation
        event.preventDefault();
        // alert("Clicke");
        const notificationsWorker = new Worker(
          new URL("./notifications_worker.js", import.meta.url),
          {
            name: "NotificationsWorker",
            type: "module",
            credentials: "same-origin",
          },
        );
        // console.log(dataset);

        // const dataset = anchor.dataset;
        const csrfToken =
          document
            .querySelector('meta[name="csrf-token"]')
            ?.getAttribute("content") || getCookie("csrftoken");

        notificationsWorker.postMessage({
          pk: dataset["notificationPk"],
          url: document.querySelector("input#notificationUrl").value,
          token: csrfToken,
          user: dataset["user"],
          notificationType: dataset["notificationType"],
        });
        notificationsWorker.onmessage = (event) => {
          // console.log("Worker response:", event.data);
          // console.log("Worker response:", event);
          notificationsWorker.terminate();
          window.location.assign(href);
        };

        notificationsWorker.onerror = (error) => {
          console.error("Worker error:", error);
          console.error("Worker error:", error["message"]);
          notificationsWorker.terminate();
        };
      });
    });
  }
});
