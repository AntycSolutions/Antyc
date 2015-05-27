requirejs.config({
    "paths": {
        // jQuery
        "jquery": "//code.jquery.com/jquery-2.1.3.min",
        // Bootstrap
        "bootstrap_js": "//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min",
        // Bootswatch Simplex Bootstrap
        "bootstrap_css": "//maxcdn.bootstrapcdn.com/bootswatch/3.3.2/simplex/bootstrap.min",
        // Font Awesome
        "font_awesome": "//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min"
    },
    "shim": {
        "bootstrap_js": {
            "deps": ["jquery"]
        }
    },
    "map": {
        '*': {
            // require-css
            'css': '//cdnjs.cloudflare.com/ajax/libs/require-css/0.1.8/css.min.js'
        }
    }
});

require(
    ["css!bootstrap_css", "css!font_awesome",
     "jquery", "bootstrap_js"],
    function ($) {
        // console.log("works");
    }
);
