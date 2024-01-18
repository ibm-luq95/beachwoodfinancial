"use strict";

/**
 *  Filter and return cleaned errors form api errors
 * @param {Error} error the error to filter
 * @returns Array
 */
const bwCleanApiError = (error) => {
  console.log(error);
  const allErrorsArray = [];
  const apiArrayErrors = ["type", "errors"];
  const errorKeys = Object.keys(error);
  if (errorKeys.includes(apiArrayErrors[0]) && errorKeys.includes(apiArrayErrors[1])) {
    const allErrors = error["errors"];
    allErrors.forEach((element) => {
      allErrorsArray.push({
        detail: element["detail"],
        attr: element["attr"],
      });
      // eslint-disable-next-line no-useless-escape
      //   const replace = element["detail"].replace(/[\[\]]/g, "");
      //   console.warn(replace);
      //   const array = replace.split(",");
      //   console.warn(array);
      //   const errorDetail = JSON.parse(JSON.stringify(element["detail"]));
      //   console.warn(typeof errorDetail);
      //   console.warn(errorDetail);
    });
    // console.log(allErrorsArray);
    return allErrorsArray;
  } else {
    console.warn("Not api error");
    return null;
  }
};

export { bwCleanApiError };
