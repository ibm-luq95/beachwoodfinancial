/** @type {import('tailwindcss').Config} */
const Path = require("path");
// const fs = require("fs");
const chalk = require("chalk");
const log = console.log;
const pwd = process.env.PWD;
const pwdParent = Path.dirname(pwd);

// We can add current project paths here
const projectPaths = [
  Path.join(pwdParent, "templates", "**", "*.html"),
  Path.join(pwdParent, "templates", "**", "*.jinja"),
  // Path.join(pwdParent, "bw_jinja2", "templates", "**", "*.html"),
  // Path.join(pwdParent, "bw_jinja2", "templates", "**", "*.jinja"),
  Path.join(pwdParent, "static", "**", "*.js"),
  Path.join(pwdParent, "components", "**", "*.js"),
  Path.join(pwdParent, "components", "**", "*.html"),
  Path.join(pwdParent, "components", "**", "*.jinja"),
  // add js file paths if you need
];

const contentPaths = [...projectPaths];
console.log(`tailwindcss will scan ${contentPaths}`);
module.exports = {
  // darkMode: "class",
  content: contentPaths,
  theme: {
    extend: {},
  },
  corePlugins: {
    aspectRatio: false,
  },
  plugins: [
    require("@tailwindcss/typography"),
    require("@tailwindcss/forms"),
    require("@tailwindcss/aspect-ratio"),
    require("@tailwindcss/container-queries"),
    require("preline/plugin"),
  ],
};
