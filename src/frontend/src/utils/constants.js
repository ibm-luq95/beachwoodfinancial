"use strict";

// init and create method to all objects, get object type
Object.prototype.getConstructorName = function () {
  const str = (this.prototype ? this.prototype.constructor : this.constructor).toString();
  const cname = str.match(/function\s(\w*)/)[1];
  const aliases = ["", "anonymous", "Anonymous"];
  return aliases.indexOf(cname) > -1 ? "Function" : cname;
};

const isDisabledCssClass = "is-disabled";
const CSRFINPUTNAME = "csrfmiddlewaretoken";
const eyeSlashIconHTMLCode = `<i class="fa-solid fa-eye-slash"></i>`;
const eyeIconHTMLCode = `<i class="fa-solid fa-eye"></i>`;
// console.log(global.window.settings);
// const DEBUG = window.settings["DEBUG"];
const DEBUG = true;
// const FETCHURLNAMEURL = window.settings["FETCHURLNAMEURL"];
const FETCHURLNAMEURL = "";
// const CURRENTUSER = window.settings["CURRENTUSER"];
const CURRENTUSER = "";

export {
  isDisabledCssClass,
  eyeSlashIconHTMLCode,
  eyeIconHTMLCode,
  DEBUG,
  FETCHURLNAMEURL,
  CURRENTUSER,
  CSRFINPUTNAME,
};
