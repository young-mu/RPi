function route(handle, pathname, response) {
    if (typeof handle[pathname] === 'function') {
        handle[pathname](response);
    } else {
        console.log("no request handler found for " + pathname);
        response.writeHead(404, {"content-type":"text/plain"});
        response.write("404 not found");
        response.end();
    }
}

exports.route = route;
