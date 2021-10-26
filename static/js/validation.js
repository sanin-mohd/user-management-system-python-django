
$(document).ready(function () {

    $("#form").validate({ // initialize the plugin
        rules: {
            username: {
                required: true 
            },
            password: {
                required: true,
                minlength: 4
            },cpassword: {
                required: true,
                minlength: 5
            },
            email: {
                required: true,
                email:true
                
            },
            career: {
                required: true
                
                
            },
            img:{
                required:true
            }
        },
        
    });

});