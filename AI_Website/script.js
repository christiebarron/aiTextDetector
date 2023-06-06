$(document).ready(function(){
    $(document).mousemove(function(e){
        $('.apple').css({'top': e.pageY,'left': e.pageX});
    });

    $('#loginForm').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/login',
            data: $(this).serialize(),
            success: function(data) {
                // If login is successful, redirect to the next page
                window.location.href = '/next_page';
            },
            error: function() {
                $('#loginResult').html('An error occurred.');
            }
        });
    });
    
    
});
