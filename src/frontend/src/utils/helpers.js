"use strict";

/**
 * Capitalized the first letter of string
 * @param {string} text String will capitalized
 * @returns string
 */
const capitalizedFirstLetter = (text) => {
  const capitalized = text.charAt(0).toUpperCase() + text.slice(1);
  return capitalized;
};

/**
 * Order or sort json object items
 * @param {Object} unorderedObject Un ordered object
 * @returns Object
 */
const orderObjectItems = (unorderedObject) => {
  const orderedObject = Object.keys(unorderedObject)
    .sort()
    .reduce((obj, key) => {
      obj[key] = unorderedObject[key];
      return obj;
    }, {});
  return orderedObject;
};

/**
 * Check if the checkbox single or multiple elements
 * @param {HTMLInputElement|RadioNodeList} htmlElement Element to check
 * @returns string
 */
const checkIfInputSingleOrList = (htmlElement) => {
  // RadioNodeList, HTMLInputElement
  if (htmlElement.getConstructorName() === "RadioNodeList") {
    // in case multiple inputs
    return "multiple";
  } else if (htmlElement.getConstructorName() === "HTMLInputElement") {
    // in case single input
    return "single";
  }
};

/**
 * Check if the text is true or false
 * @param {string} text Text to check true | false
 * @returns bool
 */
const convertStrToBool = (text) => {
  const boolValue = /true/i.test(text);
  if (boolValue === true) {
    return true;
  } else {
    return false;
  }
};
export {
  capitalizedFirstLetter,
  orderObjectItems,
  checkIfInputSingleOrList,
  convertStrToBool,
};
