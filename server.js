var http = require("http");
var url = require("url");
var querystring = require("querystring");

function start(route, handler) {
    http.createServer((req, res) => {
        var pathname = url.parse(req.url).pathname;
        console.log("Request for " + pathname + " received.");

        route(pathname, handler);

        res.writeHead(200, {"Content-Type": "text/html"});
        res.write("Hello World!\n");
        res.end();
    }).listen(8888);

    console.log("Server has started!");
}

exports.start = start;