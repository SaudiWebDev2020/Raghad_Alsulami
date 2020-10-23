$(document).ready(function() {

    $('img').hover(function() {
        $(this).attr({
            src: $(this).attr('src2')
        });
    }, function(){
        $(this).attr({
            src: $(this).attr('src1')
        });
    });

});  