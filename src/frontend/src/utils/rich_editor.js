/* eslint-disable no-undef */
"use strict";

document.addEventListener("DOMContentLoaded", (readyEvent) => {
  const allRichEditors = document.querySelectorAll("textarea.rich-editor");
  if (allRichEditors) {
    if (allRichEditors.length > 0) {
      allRichEditors.forEach((textareaElement) => {
        textareaElement.removeAttribute("required");
      });
      tinymce.init({
        selector: "textarea.rich-editor",
        a_plugin_option: true,
        highlight_on_focus: true,
        resize: "both",
        toolbar_mode: "sliding",
        a_configuration_option: 400,
        plugins:
          "autoresize advlist link lists autosave table anchor directionality insertdatetime link",
        min_height: 400,
        menubar: false,
        // toolbar:
        //   "undo redo | styles | bold italic | alignleft aligncenter alignright alignjustify | outdent indent",
        toolbar: [
          { name: "directionalityplugin", items: ["ltr", "rtl"] },
          { name: "history", items: ["undo", "redo"] },
          { name: "styles", items: ["styles"] },
          {
            name: "formatting",
            items: ["bold", "italic", "underline", "strikethrough", "hr"],
          },
          {
            name: "alignment",
            items: ["alignleft", "aligncenter", "alignright", "alignjustify"],
          },
          { name: "listsplugin", items: ["numlist", "bullist"] },
          { name: "indentation", items: ["outdent", "indent"] },

          // { name: "print", items: ["print"] },
          { name: "linkplugin", items: ["link"] },
          { name: "colorsplugins", items: ["backcolor"] },
          { name: "autosaveplugins", items: ["restoredraft"] },
          { name: "insertdatetimeplugin", items: ["insertdatetime"] },
          {
            name: "tableplugin",
            items: [
              "table",
              // "tabledelete",
              // "tableprops",
              // "tablerowprops",
              // "tablecellprops",
              // "tableinsertrowbefore",
              // "tableinsertrowafter",
              // "tabledeleterow",
              // "tableinsertcolbefore",
              // "tableinsertcolafter",
              // "tabledeletecol",
            ],
          },
        ],
        autosave_ask_before_unload: false,
      });
    }
  }
});
// 'table tabledelete | tableprops tablerowprops tablecellprops | tableinsertrowbefore tableinsertrowafter tabledeleterow | tableinsertcolbefore tableinsertcolafter tabledeletecol'
