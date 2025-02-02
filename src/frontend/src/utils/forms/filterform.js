"use strict";

/**
 * @class FilterPersistence
 * @description Handles storing, retrieving, and syncing filter form inputs using localStorage and URL parameters.
 */
class FilterPersistence {
  /**
   * Creates an instance of FilterPersistence.
   * @param {HTMLFormElement} form - The filter form element.
   * @param {string} storagePrefix - Prefix for localStorage keys to store individual inputs.
   */
  constructor(form, storagePrefix = "filter_") {
    if (!form || !(form instanceof HTMLFormElement)) {
      throw new Error("A valid HTMLFormElement is required.");
    }

    this.form = form;
    this.storagePrefix = storagePrefix;
    this.inputListener = (event) => this.safeSaveFilter(event.target);

    // ✅ Check for saved filters and apply them when the page loads
    this.loadFilters();

    // ✅ Add input event listener to save filters
    this.form.addEventListener("input", this.inputListener);

    // ✅ Add reset event listener to clear filters
    this.form.addEventListener("reset", () => {
      this.safeResetFilters();
    });
  }

  /**
   * Safely saves an individual filter input to localStorage and updates the URL.
   * @param {HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement} input - The input element to save.
   */
  safeSaveFilter(input) {
    try {
      if (!input.name) return;

      let value;
      if (input.type === "checkbox") {
        value = input.checked ? "true" : "false";
      } else if (input.type === "radio") {
        if (!input.checked) return;
        value = input.value;
      } else if (input.multiple) {
        value = Array.from(input.selectedOptions)
          .map((opt) => opt.value)
          .join(",");
      } else {
        value = input.value;
      }

      // ✅ Save individual input value to localStorage
      localStorage.setItem(`${this.storagePrefix}${input.name}`, value);

      // ✅ Update URL parameters
      const url = new URL(window.location);
      url.searchParams.set(input.name, value);
      window.history.replaceState({}, "", url);

      this.form.dispatchEvent(new Event("filtersSaved"));
    } catch (error) {
      console.error(`Error saving filter [${input.name}]:`, error);
    }
  }

  /**
   * Loads saved filter values from localStorage and URL parameters, and applies them to the form.
   * If filters exist, it updates the URL and navigates to the filtered page.
   */
  loadFilters() {
    try {
      const urlParams = new URLSearchParams(window.location.search);
      let hasFilters = false;

      Array.from(this.form.elements).forEach((input) => {
        if (!input.name) return;

        // ✅ Get value from URL first, fallback to localStorage
        const urlValue = urlParams.get(input.name);
        const savedValue = localStorage.getItem(`${this.storagePrefix}${input.name}`);
        const value = urlValue !== null ? urlValue : savedValue;

        if (value === null) return;

        // ✅ Apply saved value to the form input
        if (input.type === "checkbox") {
          input.checked = value === "true";
        } else if (input.type === "radio") {
          if (input.value === value) input.checked = true;
        } else if (input.multiple) {
          const valuesArray = value.split(",");
          Array.from(input.options).forEach((opt) => {
            opt.selected = valuesArray.includes(opt.value);
          });
        } else {
          input.value = value;
        }

        // ✅ Update URL if the value is from localStorage and not already in the URL
        if (urlValue === null && savedValue !== null) {
          urlParams.set(input.name, savedValue);
          hasFilters = true;
        }
      });

      // ✅ If filters were applied from localStorage, navigate to the updated URL
      if (hasFilters) {
        const newUrl = `${window.location.pathname}?${urlParams.toString()}`;
        window.history.replaceState({}, "", newUrl);
        window.location.href = newUrl; // Navigate to updated URL
      }
    } catch (error) {
      console.error("Error loading filters:", error);
    }
  }

  /**
   * Safely resets the filter form, clears localStorage, removes URL parameters, and resets input values.
   */
  safeResetFilters() {
    try {
      // 🔹 Remove all stored filter values from localStorage FIRST
      Array.from(this.form.elements).forEach((input) => {
        if (input.name) {
          localStorage.removeItem(`${this.storagePrefix}${input.name}`);
        }
      });

      // 🔹 Clear all URL parameters
      const url = new URL(window.location);
      url.search = "";
      window.history.replaceState({}, "", url);

      // 🔹 Temporarily remove the input event listener to prevent re-saving old values
      this.form.removeEventListener("input", this.inputListener);

      // 🔹 Reset the form (this clears visible input values)
      this.form.reset();

      // 🔹 Ensure checkboxes, radios, and multi-selects are properly cleared
      setTimeout(() => {
        Array.from(this.form.elements).forEach((input) => {
          if (input.type === "checkbox" || input.type === "radio") {
            input.checked = false;
          } else if (input.multiple) {
            Array.from(input.options).forEach((opt) => (opt.selected = false));
          } else {
            input.value = ""; // Clear text and number inputs
          }
        });

        // 🔹 Restore input event listener after reset
        this.form.addEventListener("input", this.inputListener);
      }, 0);

      // 🔹 Dispatch a custom event when filters are reset
      this.form.dispatchEvent(new Event("filtersReset"));
    } catch (error) {
      console.error("Error resetting filters:", error);
    }
  }
}

// Example usage:
/**
 const filterForm = document.getElementById("filter-form");
if (filterForm) {
  const filterPersistence = new FilterPersistence(filterForm);

  filterForm.addEventListener("filtersSaved", () => {
    console.log("Filters saved!");
  });
  filterForm.addEventListener("filtersReset", () => {
    console.log("Filters reset!");
  });
}
*/
export default FilterPersistence;
