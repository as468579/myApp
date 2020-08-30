var http = require("http");
var url = require("url");
var querystring = require("querystring");

function start() {
    http.createServer((req, res) => {
        var pathname = url.parse(req.url).pathname;
        var a = url.parse(req.url).query;
        var b = querystring.parse(req.url);
        console.log(req.url);
        res.writeHead(200, {"Content-Type": "text/html"});
        res.write("Hello World!");
        res.end();
    }).listen(8888);

    console.log("Server has started!");
}

exports.start = start;