requirejs.config({
    "paths": {
        // jQuery
        "jquery": "//code.jquery.com/jquery-2.1.3.min",
        // Bootstrap
        "bootstrap_js": "//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min"
    },
    "shim": {
        "bootstrap_js": {
            "deps": ["jquery"]
        }
    },
});

require(
    [
     "jquery", "bootstrap_js"
    ],
    function ($) {
        // console.log("works");
    }
);
