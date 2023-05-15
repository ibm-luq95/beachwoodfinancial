/** @type {import('tailwindcss').Config} */
const Path = require("path");
const pwd = process.env.PWD;

// We can add current project paths here
const projectPaths = [
  Path.join(pwd, "../templates/**/*.html"),
  // add js file paths if you need
];

const contentPaths = [...projectPaths];
console.log(`tailwindcss will scan ${contentPaths}`);
module.exports = {
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
