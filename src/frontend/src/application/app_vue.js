import { createApp } from "vue";
import App from "../components/App.vue";

// Mount main app
if (document.querySelector("#app")) {
  createApp(App).mount("#app");
}

// Mount Client Selector Dropdown
if (document.querySelector("#vue-client-selector")) {
  import("../components/dashboard/ClientSelectorDropdown.vue").then(module => {
    const { default: ClientSelectorDropdown } = module;
    const mountElement = document.querySelector("#vue-client-selector");

    const app = createApp(ClientSelectorDropdown, {
      apiEndpoint: mountElement.dataset.apiEndpoint || "/dashboard/client/api/dropdown/",
      currentClientId: mountElement.dataset.currentClientId || null,
      currentClientName: mountElement.dataset.currentClientName || "",
      currentClientEmail: mountElement.dataset.currentClientEmail || "",
      currentClientLogo: mountElement.dataset.currentClientLogo || ""
    });

    // Handle client selection - navigate to the selected client's page
    const handleClientSelected = ({ detail }) => {
      if (detail && detail.url) {
        window.location.href = detail.url;
      }
    };

    // Mount the app first
    app.mount("#vue-client-selector");

    // Then listen for custom DOM events
    // The Vue component will emit a custom DOM event that bubbles up
    mountElement.addEventListener("client-selected", handleClientSelected);
  });
}
