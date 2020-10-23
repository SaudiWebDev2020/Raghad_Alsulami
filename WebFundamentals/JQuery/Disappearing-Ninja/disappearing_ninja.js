$(document).ready(function() {

    $('img.ninja').click(function() { 
        $(this).fadeOut();
    });

    $('button.restore').click(function() { 
        $('img.ninja').fadeIn();
    });
    
});  