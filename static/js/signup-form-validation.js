
$(document).ready(function () {

    $("#signup-form").validate({ // initialize the plugin
        rules: {
            username: {
                required: true
                
                
            },
            email: {
                required: true,
                type:email
                
            },
            career: {
                required: true
                
                
            },
            password: {
                required: true,
                minlength: 5
            },
            cpassword: {
                required: true,
                minlength: 5
            }
        }
    });

});