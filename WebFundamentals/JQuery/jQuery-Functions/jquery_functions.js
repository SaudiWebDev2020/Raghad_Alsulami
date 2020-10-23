$(document).ready(function() {

    $('button.hide').click(function() { 
        $('p.text').hide();
    });

    $('button.show').click(function() { 
        $('p.text').show();
    });

    $('button.toggle').click(function() { 
        $('p.text').toggle();
    });

    $('button.slideUp').click(function() { 
        $('img.image').slideUp();
    });
    $('button.slideDown').click(function() { 
        $('img.image').slideDown();
    });

    $('button.slideToggle').click(function() { 
        $('img.image').slideToggle();
    });

    $('button.fadeIn').click(function() { 
        $('img.image').fadeIn();
    });

    $('button.fadeOut').click(function() { 
        $('img.image').fadeOut();
    });

    $('p.text').click(function() { 
        $(this).before( "<h1>Title</h1>" );
        $(this).addClass('changeTextColor');
        $(this).append('<p> Red color </p>')
    });

    $('img.image').click(function() { 
        $(this).after( "<p>Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>" );
    });

    $('p.text2').click(function() { 
        var htmlString=$(this).html();
        $(this).text(htmlString);
    });

    $('button.setWidth').click(function(){
        $('img.image').attr('width','500');
    });

    $('p.email').click(function(){
        $("input:text").val("x@gmail.com");
    });

});
