"use strict";
import i18next from "i18next";

const bwI18Helper = i18next.init({
  lng: "en", // if you're using a language detector, do not define the lng option
  debug: true,
  resources: {
    en: {
      translation: {
        key: "hello world",
      },
    },
  },
});

export { bwI18Helper };
