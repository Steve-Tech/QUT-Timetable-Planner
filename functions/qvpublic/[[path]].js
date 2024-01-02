export function onRequest(context) {
    const url = new URL(context.request.url);
    return fetch("https://qutvirtual3.qut.edu.au/" + url.pathname.substring(1) + url.search, context.request);
}