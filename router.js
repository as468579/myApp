function route (pathname, handler){
    console.log("About to route a requset for " + pathname);
    if (typeof(handler[pathname]) == "function"){
        handler[pathname]();
    }
    else{
        console.log("No request handler found for " + pathname);
    }
}
exports.route = route;