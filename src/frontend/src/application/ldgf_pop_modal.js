/**
 * ldgf_pop_modal.js
 * A fully reusable, accessible, production-grade modal UI component
 * No external dependencies - ES6 module pattern
 */

(function () {
    'use strict';

    const LdgfModal = {
        _modals: new Map(),
        _activeModal: null,
        _modalStack: [],
        _focusedElementBeforeOpen: null,
        _cachedContent: new Map(),
        _beforeCloseHandlers: new Map(),

        /**
         * Get CSRF token from cookie
         * @returns {string|null}
         */
        _getCsrfToken() {
            const match = document.cookie.match(/csrftoken=([^;]+)/);
            return match ? match[1] : null;
        },

        /**
         * Normalize modal ID (add # if missing)
         * @param {string} modalId
         * @returns {string}
         */
        _normalizeId(modalId) {
            return modalId.startsWith('#') ? modalId : `#${modalId}`;
        },

        /**
         * Get modal element by ID
         * @param {string} modalId
         * @returns {HTMLElement|null}
         */
        _getModalElement(modalId) {
            const id = this._normalizeId(modalId).replace('#', '');
            return document.getElementById(id);
        },

        /**
         * Get focusable elements within modal
         * @param {HTMLElement} modal
         * @returns {HTMLElement[]}
         */
        _getFocusableElements(modal) {
            const focusableSelectors = [
                'button:not([disabled])',
                'input:not([disabled])',
                'select:not([disabled])',
                'textarea:not([disabled])',
                'a[href]',
                '[tabindex]:not([tabindex="-1"])',
            ].join(', ');

            return Array.from(modal.querySelectorAll(focusableSelectors)).filter(
                (el) => !el.closest('[data-ldgf-modal-close]') ||
                    el.closest('[data-ldgf-modal-panel]')
            );
        },

        /**
         * Focus trap within modal
         * @param {KeyboardEvent} e
         */
        _handleTabKey(e) {
            if (!this._activeModal) return;

            const focusableElements = this._getFocusableElements(this._activeModal);
            if (focusableElements.length === 0) return;

            const firstElement = focusableElements[0];
            const lastElement = focusableElements[focusableElements.length - 1];

            if (e.shiftKey) {
                if (document.activeElement === firstElement) {
                    e.preventDefault();
                    lastElement.focus();
                }
            } else {
                if (document.activeElement === lastElement) {
                    e.preventDefault();
                    firstElement.focus();
                }
            }
        },

        /**
         * Handle escape key
         * @param {KeyboardEvent} e
         */
        _handleEscapeKey(e) {
            if (e.key !== 'Escape' || !this._activeModal) return;

            const backdrop = this._activeModal.dataset.ldgfBackdrop;
            if (backdrop === 'static') {
                this._dispatchEvent(this._activeModal, 'hidePrevented.ldgf.modal', {
                    reason: 'keyboard',
                });
                return;
            }

            this.close(this._activeModal.id);
        },

        /**
         * Dispatch custom event on element
         * @param {HTMLElement} element
         * @param {string} eventName
         * @param {object} detail
         */
        _dispatchEvent(element, eventName, detail = {}) {
            element.dispatchEvent(
                new CustomEvent(eventName, {
                    bubbles: true,
                    detail,
                })
            );
        },

        /**
         * Lock body scroll
         */
        _lockScroll() {
            document.body.style.overflow = 'hidden';
        },

        /**
         * Unlock body scroll
         */
        _unlockScroll() {
            const hasOpenModals = document.querySelectorAll(
                '[data-ldgf-modal]:not(.hidden)'
            ).length > 0;
            if (!hasOpenModals) {
                document.body.style.overflow = '';
            }
        },

        /**
         * Snapshot form values for dirty checking
         * @param {HTMLFormElement} form
         * @returns {object}
         */
        _snapshotFormValues(form) {
            if (!form) return {};
            const values = {};
            const elements = form.querySelectorAll(
                'input, select, textarea'
            );
            elements.forEach((el) => {
                if (el.type === 'checkbox' || el.type === 'radio') {
                    values[el.name] = el.checked;
                } else {
                    values[el.name] = el.value;
                }
            });
            return JSON.stringify(values);
        },

        /**
         * Check if form has dirty values
         * @param {HTMLFormElement} form
         * @param {string} snapshot
         * @returns {boolean}
         */
        _isFormDirty(form, snapshot) {
            if (!form) return false;
            const currentSnapshot = this._snapshotFormValues(form);
            return currentSnapshot !== snapshot;
        },

        /**
         * Get loading spinner HTML
         * @returns {string}
         */
        _getLoadingSpinner() {
            return `
        <div class="flex items-center justify-center p-8">
          <div class="ldgf-modal__spinner animate-spin rounded-full h-10 w-10 border-4 border-gray-200 border-t-blue-600"></div>
        </div>
      `;
        },

        /**
         * Get error message HTML
         * @param {string} message
         * @returns {string}
         */
        _getErrorMessage(message) {
            return `
        <div class="flex flex-col items-center justify-center p-8 text-center">
          <i class="fa-solid fa-circle-exclamation text-red-500 text-4xl mb-4"></i>
          <p class="text-gray-700 dark:text-gray-300">${message || 'Failed to load content. Please try again.'}</p>
          <button type="button"
                  data-ldgf-retry-btn
                  class="mt-4 py-2 px-4 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
            Retry
          </button>
        </div>
      `;
        },

        /**
         * Inject CSRF token into forms in content
         * @param {string} content
         * @param {string} csrfToken
         * @returns {string}
         */
        _injectCsrfToken(content, csrfToken) {
            if (!csrfToken) return content;
            const csrfInput = `<input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">`;
            return content.replace(/<form[^>]*>/i, (match) => {
                if (match.includes('csrfmiddlewaretoken')) return match;
                return match + csrfInput;
            });
        },

        /**
         * Set submit button loading state
         * @param {HTMLElement} button
         * @param {boolean} isLoading
         */
        _setSubmitLoading(button, isLoading) {
            if (!button) return;

            if (isLoading) {
                button.disabled = true;
                button.dataset.ldgfOriginalText = button.innerHTML;
                button.innerHTML = `
          <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          Loading...
        `;
                button.classList.add('ldgf-modal__submit--loading');
            } else {
                button.disabled = false;
                if (button.dataset.ldgfOriginalText) {
                    button.innerHTML = button.dataset.ldgfOriginalText;
                }
                button.classList.remove('ldgf-modal__submit--loading');
            }
        },

        /**
         * Reset form fields to their initial state
         * @param {HTMLFormElement} form
         */
        _resetForm(form) {
            if (!form) return;

            // Remove any injected error messages
            form.querySelectorAll('.ldgf-field-error').forEach((el) => el.remove());

            // Remove red border classes from fields
            form.querySelectorAll('.border-red-500').forEach((el) => {
                el.classList.remove('border-red-500');
            });

            // Reset the submitting flag
            delete form.dataset.ldgfSubmitting;

            // Reset the native form values
            form.reset();
        },

        /**
         * Handle form AJAX submission
         * @param {Event} e
         */
        async _handleFormSubmit(e) {
            const form = e.target;
            if (!form.matches('[data-ldgf-ajax-form]')) return;

            // Prevent double submission: guard against rapid clicks
            if (form.dataset.ldgfSubmitting === 'true') {
                e.preventDefault();
                e.stopImmediatePropagation();
                return;
            }

            const modal = form.closest('[data-ldgf-modal]');
            if (!modal) return;

            form.dataset.ldgfSubmitting = 'true';

            const submitBtn = modal.querySelector('[data-ldgf-modal-submit]');
            this._setSubmitLoading(submitBtn, true);

            try {
                const csrfToken = this._getCsrfToken();
                const formData = new FormData(form);
                const method = form.method.toLowerCase();

                const headers = {
                    'X-Requested-With': 'XMLHttpRequest',
                };
                if (csrfToken) {
                    headers['X-CSRFToken'] = csrfToken;
                }

                const response = await fetch(form.action, {
                    method: method === 'get' ? 'GET' : 'POST',
                    body: method === 'get' ? new URLSearchParams(formData) : formData,
                    headers,
                });

                const contentType = response.headers.get('content-type');
                const isJson = contentType && contentType.includes('application/json');

                if (response.ok && (response.redirected || response.status === 200)) {
                    if (response.redirected) {
                        window.location.href = response.url;
                    } else if (isJson) {
                        const data = await response.json();
                        if (data.success || data.status === 'success') {
                            this.close(modal.id);
                            if (data.redirect) {
                                window.location.href = data.redirect;
                            }
                        } else {
                            this._injectFormErrors(modal, data.errors || {});
                        }
                    } else {
                        this.close(modal.id);
                    }
                } else if (response.status === 400 || response.status === 422) {
                    if (isJson) {
                        const data = await response.json();
                        this._injectFormErrors(modal, data.errors || data.form_errors || {});
                    } else {
                        const html = await response.text();
                        const bodyMatch = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i);
                        if (bodyMatch) {
                            const parser = new DOMParser();
                            const doc = parser.parseFromString(bodyMatch[1], 'text/html');
                            const formHtml = doc.querySelector('[data-ldgf-form-fields], [data-ldgf-checkbox-form-fields]');
                            if (formHtml) {
                                const targetContainer = modal.querySelector(
                                    '[data-ldgf-form-fields], [data-ldgf-checkbox-form-fields]'
                                );
                                if (targetContainer) {
                                    targetContainer.innerHTML = formHtml.innerHTML;
                                }
                            }
                        }
                    }
                } else {
                    const errorMsg = modal.querySelector('[data-ldgf-form-fields]') ||
                        modal.querySelector('[data-ldgf-checkbox-form-fields]');
                    if (errorMsg) {
                        errorMsg.insertAdjacentHTML(
                            'afterbegin',
                            '<div class="mb-4 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">An error occurred. Please try again.</div>'
                        );
                    }
                }
            } catch (error) {
                console.error('Form submission error:', error);
                const errorMsg = modal.querySelector('[data-ldgf-form-fields]') ||
                    modal.querySelector('[data-ldgf-checkbox-form-fields]');
                if (errorMsg) {
                    errorMsg.insertAdjacentHTML(
                        'afterbegin',
                        '<div class="mb-4 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700 text-sm">Network error. Please check your connection and try again.</div>'
                    );
                }
            } finally {
                form.dataset.ldgfSubmitting = 'false';
                this._setSubmitLoading(submitBtn, false);
            }
        },

        /**
         * Inject form errors into form fields
         * @param {HTMLElement} modal
         * @param {object} errors
         */
        _injectFormErrors(modal, errors) {
            Object.keys(errors).forEach((fieldName) => {
                const field = modal.querySelector(`[name="${fieldName}"]`);
                if (!field) return;

                const fieldContainer = field.closest('.mb-4') || field.parentElement;
                const existingError = fieldContainer.querySelector('.ldgf-field-error');
                if (existingError) existingError.remove();

                const errorDiv = document.createElement('div');
                errorDiv.className = 'ldgf-field-error text-red-500 text-sm mt-1';
                errorDiv.textContent = Array.isArray(errors[fieldName])
                    ? errors[fieldName].join(', ')
                    : errors[fieldName];
                fieldContainer.appendChild(errorDiv);

                field.classList.add('border-red-500');
            });
        },

        /**
         * Load dynamic content into modal
         * @param {string} modalId
         * @param {string} url
         * @returns {Promise}
         */
        async loadContent(modalId, url) {
            const modal = this._getModalElement(modalId);
            if (!modal) return;

            const body = modal.querySelector('[data-ldgf-modal-body]');
            if (!body) return;

            const cacheKey = `${modalId}:${url}`;
            if (this._cachedContent.has(cacheKey)) {
                const csrfToken = this._getCsrfToken();
                const content = this._cachedContent.get(cacheKey);
                body.innerHTML = this._injectCsrfToken(content, csrfToken);
                this._dispatchEvent(modal, 'contentLoaded.ldgf.modal', {
                    url,
                    success: true,
                });
                return;
            }

            body.innerHTML = this._getLoadingSpinner();

            try {
                const response = await fetch(url);
                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}`);
                }

                const html = await response.text();
                this._cachedContent.set(cacheKey, html);

                const csrfToken = this._getCsrfToken();
                body.innerHTML = this._injectCsrfToken(html, csrfToken);

                this._dispatchEvent(modal, 'contentLoaded.ldgf.modal', {
                    url,
                    success: true,
                });
            } catch (error) {
                console.error('Failed to load modal content:', error);
                body.innerHTML = this._getErrorMessage();
                this._dispatchEvent(modal, 'contentLoaded.ldgf.modal', {
                    url,
                    success: false,
                });
            }
        },

        /**
         * Open modal
         * @param {string} modalId
         * @param {object} options
         */
        open(modalId, options = {}) {
            const modal = this._getModalElement(modalId);
            if (!modal) {
                console.warn(`LdgfModal: Modal with id "${modalId}" not found.`);
                return;
            }

            if (this._activeModal && this._activeModal !== modal) {
                this.close(this._activeModal.id);
            }

            this._focusedElementBeforeOpen = document.activeElement;

            const relatedTarget = options.trigger || null;
            this._dispatchEvent(modal, 'show.ldgf.modal', {relatedTarget});

            const backdrop = modal.querySelector('[data-ldgf-modal-backdrop]');
            const panel = modal.querySelector('[data-ldgf-modal-panel]');

            if (backdrop) {
                backdrop.classList.remove('opacity-0', 'pointer-events-none');
                backdrop.classList.add('opacity-100');
            }

            if (panel) {
                panel.classList.remove('opacity-0', '-translate-y-4');
                panel.classList.add('opacity-100', 'translate-y-0');
            }

            modal.classList.remove('hidden');

            this._activeModal = modal;
            this._modalStack.push(modalId);
            this._lockScroll();

            const form = modal.querySelector('form');
            if (form && modal.dataset.ldgfDirtyCheck === 'true') {
                modal.dataset.ldgfFormSnapshot = this._snapshotFormValues(form);
            }

            if (modal.dataset.ldgfDynamicSrc) {
                this.loadContent(modalId, modal.dataset.ldgfDynamicSrc);
            }

            panel.addEventListener(
                'transitionend',
                () => {
                    this._dispatchEvent(modal, 'shown.ldgf.modal', {relatedTarget});

                    const focusableElements = this._getFocusableElements(modal);
                    if (focusableElements.length > 0) {
                        focusableElements[0].focus();
                    } else {
                        const closeBtn = modal.querySelector('[data-ldgf-modal-close]');
                        if (closeBtn) closeBtn.focus();
                    }
                },
                {once: true}
            );

            this._modals.set(modalId.replace('#', ''), {
                backdrop: backdrop?.dataset?.ldgfBackdrop || 'default',
            });
        },

        /**
         * Close modal
         * @param {string} modalId
         */
        close(modalId) {
            const modal = this._getModalElement(modalId);
            if (!modal) return;

            const beforeCloseHandler = this._beforeCloseHandlers.get(modalId.replace('#', ''));
            if (beforeCloseHandler) {
                Promise.resolve(beforeCloseHandler()).then((canClose) => {
                    if (!canClose) {
                        this._dispatchEvent(modal, 'hidePrevented.ldgf.modal', {
                            reason: 'custom',
                        });
                        return;
                    }
                    this._performClose(modal);
                });
            } else {
                this._performClose(modal);
            }
        },

        /**
         * Perform the actual close operation
         * @param {HTMLElement} modal
         */
        _performClose(modal) {
            this._dispatchEvent(modal, 'hide.ldgf.modal', {});

            if (modal.dataset.ldgfDirtyCheck === 'true') {
                const form = modal.querySelector('form');
                const snapshot = modal.dataset.ldgfFormSnapshot;
                if (form && snapshot && this._isFormDirty(form, snapshot)) {
                    const confirmed = confirm(
                        'You have unsaved changes. Close anyway?'
                    );
                    if (!confirmed) {
                        this._dispatchEvent(modal, 'hidePrevented.ldgf.modal', {
                            reason: 'dirty',
                        });
                        return;
                    }
                }
            }

            const backdrop = modal.querySelector('[data-ldgf-modal-backdrop]');
            const panel = modal.querySelector('[data-ldgf-modal-panel]');

            if (backdrop) {
                backdrop.classList.remove('opacity-100');
                backdrop.classList.add('opacity-0');
            }

            if (panel) {
                panel.classList.remove('opacity-100', 'translate-y-0');
                panel.classList.add('opacity-0', '-translate-y-4');
            }

            panel.addEventListener(
                'transitionend',
                () => {
                    modal.classList.add('hidden');
                    this._unlockScroll();

                    // Reset form if the modal is configured to do so
                    if (modal.dataset.ldgfResetOnClose === 'true') {
                        const form = modal.querySelector('form');
                        if (form) {
                            this._resetForm(form);
                        }
                    }

                    this._dispatchEvent(modal, 'hidden.ldgf.modal', {});

                    if (this._focusedElementBeforeOpen) {
                        this._focusedElementBeforeOpen.focus();
                    }
                },
                {once: true}
            );

            this._modalStack = this._modalStack.filter((id) => id !== modal.id);
            if (this._activeModal === modal) {
                this._activeModal = null;
            }
        },

        /**
         * Toggle modal
         * @param {string} modalId
         * @param {object} options
         */
        toggle(modalId, options = {}) {
            const modal = this._getModalElement(modalId);
            if (!modal) return;

            if (modal.classList.contains('hidden')) {
                this.open(modalId, options);
            } else {
                this.close(modalId);
            }
        },

        /**
         * Check if modal is open
         * @param {string} modalId
         * @returns {boolean}
         */
        isOpen(modalId) {
            const modal = this._getModalElement(modalId);
            return modal ? !modal.classList.contains('hidden') : false;
        },

        /**
         * Register callback for modal show
         * @param {string} modalId
         * @param {function} callback
         */
        onShow(modalId, callback) {
            const modal = this._getModalElement(modalId);
            if (modal) {
                modal.addEventListener('shown.ldgf.modal', (e) => callback(e.detail));
            }
        },

        /**
         * Register callback for modal hide
         * @param {string} modalId
         * @param {function} callback
         */
        onHide(modalId, callback) {
            const modal = this._getModalElement(modalId);
            if (modal) {
                modal.addEventListener('hidden.ldgf.modal', callback);
            }
        },

        /**
         * Register before close handler
         * @param {string} modalId
         * @param {function} callback - async function that returns boolean
         */
        onBeforeClose(modalId, callback) {
            this._beforeCloseHandlers.set(modalId.replace('#', ''), callback);
        },

        /**
         * Close all modals
         */
        closeAll() {
            [...this._modalStack].forEach((modalId) => {
                this.close(modalId);
            });
        },

        /**
         * Reset submit button state
         * @param {string} modalId
         */
        resetSubmit(modalId) {
            const modal = this._getModalElement(modalId);
            if (!modal) return;
            const submitBtn = modal.querySelector('[data-ldgf-modal-submit]');
            this._setSubmitLoading(submitBtn, false);
        },

        /**
         * Reset form fields in a modal
         * Clears values, removes error styling, and restores defaults
         * @param {string} modalId
         */
        resetForm(modalId) {
            const modal = this._getModalElement(modalId);
            if (!modal) return;
            const form = modal.querySelector('form');
            if (form) {
                this._resetForm(form);
            }
        },

        /**
         * Destroy modal event listeners
         * @param {string} modalId
         */
        destroy(modalId) {
            const modal = this._getModalElement(modalId);
            if (!modal) return;

            const newModal = modal.cloneNode(true);
            modal.parentNode.replaceChild(newModal, modal);
            this._modals.delete(modalId.replace('#', ''));
            this._beforeCloseHandlers.delete(modalId.replace('#', ''));
        },

        /**
         * Initialize all modals and bind events
         */
        init() {
            document.querySelectorAll('[data-ldgf-modal-target]').forEach((trigger) => {
                trigger.addEventListener('click', (e) => {
                    e.preventDefault();
                    const targetId = trigger.dataset.ldgfModalTarget;
                    const backdrop = trigger.dataset.ldgfModalBackdrop;
                    const src = trigger.dataset.ldgfModalSrc;
                    const cache = trigger.dataset.ldgfModalCache;

                    if (backdrop) {
                        const modal = document.querySelector(
                            targetId.startsWith('#') ? targetId : `#${targetId}`
                        );
                        if (modal) {
                            modal.dataset.ldgfBackdrop = backdrop;
                        }
                    }

                    if (src) {
                        const modal = document.querySelector(
                            targetId.startsWith('#') ? targetId : `#${targetId}`
                        );
                        if (modal) {
                            modal.dataset.ldgfDynamicSrc = src;
                            if (cache === 'true') {
                                modal.dataset.ldgfCacheContent = 'true';
                            }
                        }
                    }

                    this.open(targetId, {trigger});
                });
            });

            document.querySelectorAll('[data-ldgf-modal-close]').forEach((closeBtn) => {
                closeBtn.addEventListener('click', () => {
                    const modal = closeBtn.closest('[data-ldgf-modal]');
                    if (modal) {
                        this.close(modal.id);
                    }
                });
            });

            document.querySelectorAll('[data-ldgf-modal-backdrop]').forEach((backdrop) => {
                backdrop.addEventListener('click', () => {
                    const modal = backdrop.closest('[data-ldgf-modal]');
                    if (modal && modal.dataset.ldgfBackdrop !== 'static') {
                        this.close(modal.id);
                    }
                });
            });

            /*document.querySelectorAll('form[data-ldgf-ajax-form]').forEach((form) => {
                form.addEventListener('submit', (e) => {
                    e.preventDefault();
                    this._handleFormSubmit(e);
                });
            });*/

            document.addEventListener('keydown', (e) => {
                this._handleTabKey(e);
                this._handleEscapeKey(e);
            });

            document.addEventListener('htmx:afterSwap', () => {
                this.init();
            });
        },
    };

    window.LdgfModal = LdgfModal;

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => LdgfModal.init());
    } else {
        LdgfModal.init();
    }
})();
