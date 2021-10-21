$(document).ready(function () {

    $("#login-form").validate({ // initialize the plugin
        rules: {
            username: {
                required: true,
                type:email
                
            },
            password: {
                required: true,
                minlength: 5
            }
        }
    });

});