$(document).ready(function() {

    $('img').click(function() {
        console.log('data-alt-src value is', $(this).attr('data-alt-src'));
        $(this).attr({
            src: $(this).attr('src2'),
            alt: $(this).attr('alt2')
        });
    });

});  