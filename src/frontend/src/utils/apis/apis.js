"use strict";

import { FETCHURLNAMEURL } from "../constants";
import { getCookie } from "../cookie";

/**
 * Fetch the url path by url name
 * @param {string} urlName URL name to fetch url
 * @param {string} pk PK value
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
 * This function will send a request to backend server
 * @param {Object} options json object of all options of the request
 * @returns Promise
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
