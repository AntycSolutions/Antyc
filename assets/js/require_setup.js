requirejs.config({
    paths: {
        jquery: "//code.jquery.com/jquery-2.1.3.min",
        bootstrap: "//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min",
        antyc: "antyc"
    },
    shim: {
        bootstrap: {
            deps: ["jquery"]
        }
    }
});

requirejs(["antyc"]);
