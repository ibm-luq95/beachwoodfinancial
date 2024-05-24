"use strict";

import { FETCHURLNAMEURL } from "../constants";
import { getCookie } from "../cookie";

/**
 * Fetches the URL path by name from backend.
 *
 * @param {string} urlName - The name of the URL.
 * @param {string|null} pk - The primary key (optional).
 * @returns {Promise} - A promise that resolves to the fetched data.
 * @throws {Error} - If there is an HTTP error.
 */
const fetchUrlPathByName = async (urlName, pk = null) => {
  try {
    const controller = new AbortController(); // the AbortController
    const { signal } = controller;
    const headers = new Headers({
      "Content-Type": "application/json;charset=utf-8",
      Accept: "application/json",
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),
    });
    const dataToSend = { urlName: urlName };
    if (pk) {
      dataToSend["pk"] = pk;
    }

    const fetchOptions = {
      method: "POST",
      mode: "same-origin",
      credentials: "include",
      cache: "no-cache",
      body: JSON.stringify(dataToSend),
    };
    const request = new Request(FETCHURLNAMEURL, {
      headers: headers,
      signal: signal,
    });
    const response = await fetch(request, fetchOptions);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(error);
  }
};

/**
 * Sends a request to the specified URL with the given options.
 *
 * @param {Object} options - The options for the request.
 * @param {string} options.url - The URL to send the request to.
 * @param {string} [options.contentType="application/json;charset=utf-8"] - The content type of the request.
 * @param {string} [options.token] - The CSRF token for the request.
 * @param {string} [options.method="GET"] - The HTTP method for the request.
 * @param {Object} [options.dataToSend] - The data to send with the request.
 * @returns {Promise} A promise that resolves with the response data or rejects with an error.
 *
 * @throws {Error} If an error occurs while sending the request.
 */
const sendRequest = (options) => {
  return new Promise((resolve, reject) => {
    try {
      const url = options["url"];
      const controller = new AbortController(); // the AbortController
      const { signal } = controller;
      const headers = new Headers({
        "Content-Type": options["contentType"] ?? "application/json;charset=utf-8",
        // "Content-Type": `Content-Type: application/pdf`,
        // "Content-Type": "application/x-www-form-urlencoded",
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": options["token"] ? options["token"] : getCookie("csrftoken"),
        // "Content-Disposition": "attachment; filename=upload.jpg",
      });
      // const formData = Object.fromEntries(options["dataToSend"].entries());
      const fetchOptions = {
        method: options["method"],
        mode: "same-origin",
        credentials: "include",
        cache: "no-cache",
        body: JSON.stringify(options["dataToSend"]),
        // body: formData,
      };
      const request = new Request(url, {
        headers: headers,
        signal: signal,
      });
      const fetchObj = fetch(request, fetchOptions);
      fetchObj
        .then((response) => {
          if (!response.ok) {
            return response.text().then((text) => {
              reject(JSON.parse(text));
            });
          }
          resolve(response.json());
        })
        .catch((error) => {
          reject(error);
        });
    } catch (error) {
      reject(error);
    }
  });
};

export { fetchUrlPathByName, sendRequest };
