"use strict";

/**
 * Object to handle localstorage in js
 */
class SessionStorageManagement {
  /**
   * Clear localstorage all keys
   */
  static clear() {
    sessionStorage.clear();
  }

  /**
   * Check if key exists in localstorage
   * @param {string} keyName kes name
   */
  static checkExists(keyName) {
    if (sessionStorage.getItem(keyName) !== null) {
      return true;
    } else {
      return false;
    }
  }
  /**
   * Get the value saved in localstorage
   * @param {string} keyName key name
   */
  static getItem(keyName) {
    if (SessionStorageManagement.checkExists(keyName) === true) {
      return sessionStorage.getItem(keyName);
    } else {
      return null;
    }
  }

  /**
   * Delete item from localstorage
   * @param {string} keyName key name
   */
  static deleteItem(keyName) {
    if (SessionStorageManagement.checkExists(keyName) === true) {
      sessionStorage.removeItem(keyName);
    } else {
      console.warn(`Item ${keyName} not exists in storage!`);
    }
  }

  /**
   * Set or update item in localStorage
   * @param {string} keyName key name
   * @param {*} keyValue value will saved
   * @param {boolean} replace if true will replace or update exist item
   */
  static setItem(keyName, keyValue, replace = true) {
    sessionStorage.setItem(keyName, keyValue);
  }
}

export { SessionStorageManagement };
