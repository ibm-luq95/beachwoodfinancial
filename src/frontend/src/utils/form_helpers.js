"use strict";

import { DEBUG } from "./constants";
import { orderObjectItems } from "./helpers";
import { StorageManagement } from "./storage";

/**
 * Enable or disable form fieldset items with form's submit button
 * @typedef param
 * @param {Object} param - this is object param
 * @param {HTMLFormElement} param.formElement HTML form element
 * @param {string} param.state this will enable or disable
 */
const removeBGInputsColors = ({ formElement, state }) => {};

/**
 * Enable or disable form fieldset items with form's submit button
 * @param {HTMLInputElement} param.input HTML checkbox input element
 */
const castBooleanCheckboxElement = (input) => {
  // const trueArray = [/true/i, /on/i];
  /* const booleanMap = new Map();
  booleanMap.set("true", /\b(on|true)\b/i);
  booleanMap.set("false", /\b(off|false)\b/i);
  if(booleanMap.get("true").test(input.value) === true){
    console.warn(booleanMap.get("true").match(input.value));
    return true;
  } */
  const inputValue = input.value.toLowerCase();
  if (input.value === "on" || input.value === "true") {
    return true;
  } else if (input.value === "false" || input.value === "off") {
    return false;
  } else {
    return input.value;
  }
};

/**
 * This will serialize form inputs
 * @typedef param
 * @param {Object} param - this is object param
 * @param {HTMLFormElement} param.formElement The form element
 * @param {Array} param.excludedFields Array of excluded fields
 * @param {boolean} param.isOrdered Order the returned object
 * @param {boolean} param.returnAsFormData Return inputs as FormData object
 * @param {Array} param.filesArray File(s) inputs names
 * @returns {Object|FormData} json object of all inputs
 */
const formInputSerializer = ({
  formElement,
  excludedFields = [],
  isOrdered = false,
  returnAsFormData = false,
  filesArray = [],
}) => {
  const serializedObject = {};
  const checkboxArray = new Set();
  Array.from(formElement.elements).forEach((element) => {
    // check if the element.name in excludedFields
    if (excludedFields.includes(element.name) === false) {
      if (element.name !== "") {
        // check if the element type is checkbox
        if (element.type !== "checkbox") {
          // check if the element name not empty string
          serializedObject[element.name] = element.value;
        } else {
          //checkbox single or multiple inputs
          checkboxArray.add(element.name);
        }
      }
    }
  });
  if (checkboxArray.size > 0) {
    // check if checkboxArray contains only one element
    // if (checkboxArray.size === 1) {
    //   checkboxArray.forEach((ele) => {
    //     const checkboxElement = formElement.querySelector(`input[name='${ele}']:checked`);
    //     console.log(checkboxElement);
    //     if(checkboxElement){
    //       const vvv = castBooleanCheckboxElement(checkboxElement);
    //       console.log(vvv);
    //     }
    //   });
    // }
    for (const checkboxName of checkboxArray) {
      const checkedElementArray = new Array();
      const checkboxElements = formElement.querySelectorAll(
        `input[name='${checkboxName}']:checked`,
      );
      if (checkboxElements.length > 0) {
        checkboxElements.forEach((element) => {
          // checkedElementArray.push(castBooleanCheckboxElement(element));
          checkedElementArray.push(element.value);
        });
        serializedObject[checkboxName] = checkedElementArray;
      }
    }
  }

  // check if returnAsFormData is true
  if (returnAsFormData === false) {
    return isOrdered === true ? orderObjectItems(serializedObject) : serializedObject;
  } else {
    const formData = new FormData();
    for (const key in serializedObject) {
      // check if the element not function, normal element
      if (typeof serializedObject[key] !== "function") {
        formData.append(key, serializedObject[key]);
      }
    }
    // check if filesArray contains items
    if (filesArray.length > 0) {
      for (const fieldName of filesArray) {
        if (formElement.elements[fieldName].files[0]) {
          // console.log(formElement.elements[fieldName]);
          formData.append(fieldName, formElement.elements[fieldName].files[0]);
        }
      }
    }

    return formData;
  }
};

/**
 * This function will set html form elements with values
 * @param {HTMLFormElement} formElement Form element which will set the values
 * @param {Object} objectOfValues Object of values to set
 */
const setFormInputValues = (formElement, objectOfValues) => {
  const wyswygCssClass = "wyswyg-textarea";
  // check the type of formElement is HTMLFormElement
  if (formElement.constructor.name !== "HTMLFormElement") {
    throw new Error("The element to set values not form element!!");
  }
  for (const name in objectOfValues) {
    try {
      if (Object.hasOwnProperty.call(objectOfValues, name)) {
        const inputValue = objectOfValues[name];
        const cleanValue = inputValue.replace(/(<([^>]+)>)/gi, "");
        const fElement = formElement.elements[name];
        fElement.value = cleanValue;
        // formElement.elements[name].value =
      }
    } catch (error) {
      if (error instanceof TypeError) {
        // in case the input or element not exists
        if (DEBUG === true) {
          console.warn(`The element ${name} not exists in the form ${formElement.id}`);
        }
      }
    }
  }
};

/**
 * Enable or disable form fieldset items with form's submit button
 * @typedef param
 * @param {Object} param - this is object param
 * @param {HTMLFormElement} param.formElement HTML form element
 * @param {string} param.state this will enable or disable
 */
const disableAndEnableFieldsetItems = ({ formElement, state }) => {
  console.log(`Call disableAndEnableFieldsetItems: ${state}`);
  const stateLower = state.toLowerCase();
  const fieldset = formElement.querySelector("fieldset");
  // const allFormInputs = document.querySelectorAll(`[data-form-id=${formElement.id}]`);
  const allFormInputs = Array.from(formElement.elements);
  console.log(allFormInputs);
  const submitBtn = document.querySelector(`button[form=${formElement.id}]`);
  switch (stateLower) {
    case "enable":
    case "e":
    case "en":
      fieldset.disabled = false;
      submitBtn.disabled = false;
      submitBtn.classList.remove(...["bg-blue-400", "pointer-events-none"]);
      if (allFormInputs.length > 0) {
        allFormInputs.forEach((element) => {
          element.disabled = false;
          element.classList.remove(
            ...[
              "cursor-not-allowed",
              "opacity-70",
              "pointer-events-none",
              "bg-gray-50",
              "border-gray-200",
            ],
          );
        });
      }
      break;
    case "disable":
    case "dis":
    case "d":
      fieldset.disabled = true;
      submitBtn.disabled = true;
      // submitBtn.classList.add(...["bg-blue-400", "pointer-events-none"]);
      if (allFormInputs.length > 0) {
        allFormInputs.forEach((element) => {
          // StorageManagement.setItem(element.id, element.classList);
          element.disabled = true;
          element.classList.add(
            ...[
              "cursor-not-allowed",
              "opacity-70",
              "pointer-events-none",
              "border-gray-200",
              "bg-gray-50",
            ],
          );
        });
      }
      break;
    default:
      console.warn(`${stateLower} not defined!`);
      break;
  }
};

/**
 * Set all form elements to read only
 * @param {string} formID HTML form id
 */
const setFormInputsReadOnly = (formID) => {
  const readOnlyFormElement = document.querySelector(`form#${formID}`);
  if (readOnlyFormElement) {
    const inputsArray = Array.from(readOnlyFormElement.elements);
    inputsArray.forEach((input) => {
      input.setAttribute("readonly", "readonly");
    });
  }
};

export {
  formInputSerializer,
  setFormInputValues,
  disableAndEnableFieldsetItems,
  removeBGInputsColors,
  setFormInputsReadOnly,
};
