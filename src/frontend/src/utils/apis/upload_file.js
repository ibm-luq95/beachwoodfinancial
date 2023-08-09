"use strict";

import { showToastNotification } from "../toasts";

/**
 * This object will send request api with uploaded file using XMLHTTPRequest
 */
class UploadFileRequest {
  /**
   * Constructor which will init url and form data to the object
   * @param {string} url the url endpoint
   * @param {FormData} formDataObject FormData object which contains all data to upload
   * @param {string} csrfToken django csrf token
   * @param {string} requestMethod request type, default POST
   * @param {boolean} isDebugging logging output
   */
  constructor(url, formDataObject, csrfToken, requestMethod, isDebugging = false) {
    this.url = url;
    this.formData = formDataObject;
    this.csrfToken = csrfToken;
    this.requestMethod = requestMethod ?? "POST";
    this.ajaxObject = new XMLHttpRequest();
    this.isDebugging = isDebugging;
  }

  /**
   * This method will set the header for the request
   */
  setHeaders() {
    try {
      if (this.csrfToken == "") {
        throw new Error("CSRF Token Required!");
      }
      // this.ajaxObject.setRequestHeader("Content-Type", "multipart/form-data");
      // this.ajaxObject.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      this.ajaxObject.setRequestHeader("X-Requested-With", "XMLHttpRequest");
      this.ajaxObject.setRequestHeader("Accept", "application/json");
      this.ajaxObject.setRequestHeader("Cache-Control", "no-cache");
      // this.ajaxObject.setRequestHeader("Access-Control-Allow-Origin", "*");
      this.ajaxObject.setRequestHeader("X-CSRFToken", this.csrfToken);
      // console.log(this.csrfToken);
      this.ajaxObject.withCredentials = true;
      // this.ajaxObject.timeout = 60;
      this.ajaxObject.responseType = "json";
    } catch (error) {
      console.error(error);
      showToastNotification(error, "danger");
    }
  }
  /**
   * This method will send the request
   * @returns Promise
   */
  sendRequest() {
    return new Promise((resolve, reject) => {
      try {
        // set upload progress handler

        if (this.isDebugging === true) {
          // this.ajaxObject.addEventListener("progress", this.uploadProgressHandler, false);
          this.ajaxObject.upload.addEventListener(
            "progress",
            this.uploadProgressHandler,
            false,
          );
          // set upload error handler
        }

        // open the connection
        this.ajaxObject.open(this.requestMethod, this.url, true);

        // call setHeader method
        this.setHeaders();

        // this.ajaxObject.addEventListener("error", this.errorHandler, false);
        this.ajaxObject.addEventListener("error", this.errorHandler, false);
        // set upload abort handler
        // this.ajaxObject.addEventListener("abort", this.abortHandler, false);
        this.ajaxObject.addEventListener("abort", this.abortHandler, false);

        // set upload complete handler
        this.ajaxObject.addEventListener(
          "load",
          (event) => {
            console.warn("Load event!");
            console.log(event);
          },
          false,
        );
        this.ajaxObject.send(this.formData);
        // eslint-disable-next-line no-unused-vars
        this.ajaxObject.addEventListener("readystatechange", (event) => {
          if (this.ajaxObject.readyState === 4) {
            const response = this.ajaxObject.response;
            if (this.ok() === true) {
              resolve(response["msg"]);
            } else {
              console.error(this.ajaxObject.response);
              reject(response["user_error_msg"]);
            }
          }
        });
      } catch (error) {
        console.error(error);
        showToastNotification(error, "danger");
        reject(error);
      }
    });
  }
  /**
   * This check if the response is ok
   * @returns bool
   */
  ok() {
    // console.log(this.ajaxObject.status);
    if (this.ajaxObject.status >= 200 && this.ajaxObject.status < 400) {
      return true;
    } else {
      return false;
    }
  }
  uploadProgressHandler(event) {
    const percent = (event.loaded / event.total) * 100;
    console.log(Math.round(percent) + "%");
  }

  errorHandler(event) {
    showToastNotification("Error while uploading!", "danger");
    console.error(event);
  }
  // eslint-disable-next-line no-unused-vars
  abortHandler(event) {
    this.ajaxObject.abort();
    showToastNotification("Abort uploading!", "danger");
  }
}

export { UploadFileRequest };
