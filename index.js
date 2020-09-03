// var express  = require('express')
// var app = express()

// app.get('/', (req, res) => {
//     res.send('Hello world!')
// })

// app.listen(8000,() => {
//     console.log('Example app listening on port 8000!')
// })


var server = require("./server");
var router = require("./router")
var requestHandlers = require("./requestHandlers");

var handler = {};
handler["/"] = requestHandlers.start;
handler["/start"] = requestHandlers.start;
handler["/load"] = requestHandlers.upload;
server.start(router.route, handler);