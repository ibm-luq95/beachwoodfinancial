interface InitRequestOptions {
  url: string;
  contentType: string;
  xCsrfToken: string;
  formObject: HTMLFormElement;
  accept: string;
  body: FormData | Object;
}
