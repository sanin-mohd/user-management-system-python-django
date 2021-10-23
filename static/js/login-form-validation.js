
$(document).ready(function () {

    $("#loginform").validate({ // initialize the plugin
        rules: {
            username: {
                required: true },
            password: {
                required: true,
                minlength: 4
            }
        },
        
    });

});