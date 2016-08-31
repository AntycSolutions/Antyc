requirejs.config({
    "paths": {
        // jQuery
        "jquery": "//code.jquery.com/jquery-2.2.4.min",
        // Bootstrap
        "bootstrap_js": "//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min"
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
