// $(function(){}) is short for $(document).ready(function() { ... });
$(function() {
    $('button').click(function() {
        $.ajax({
            url: "http://127.0.0.1:5000/signUpUser",
            data: $("form").serialize(),
            type: "POST",
            success: function(response) {
                console.log("response found" +response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
