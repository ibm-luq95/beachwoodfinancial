"use strict";

class StorageManagement {
  static clear() {
    window.localStorage.clear();
  }

  static checkExists(keyName) {
    if (window.localStorage.getItem(keyName) !== null) {
      return true;
    } else {
      return false;
    }
  }
  static getItem(keyName) {
    if (StorageManagement.checkExists(keyName) === true) {
      return window.localStorage.getItem(keyName);
    } else {
      return null;
    }
  }

  static deleteItem(keyName) {
    if (StorageManagement.checkExists(keyName) === true) {
      window.localStorage.removeItem(keyName);
    } else {
      console.warn(`Item ${keyName} not exists in storage!`);
    }
  }

  static setItem(keyName, keyValue, replace = true) {
    window.localStorage.setItem(keyName, keyValue);
  }
}

export { StorageManagement };
