 $(document).ready(function() {
    $('.nav-toggle').on('click', function(){
        $('#menu').toggleClass('active');
    });
    $('.carusel').slick({
        dots: false,
        prevArrow: false,
        nextArrow: false
    });

    var options = {
        strings: ["#design", "#creative","#digital"],
        typeSpeed: 100,
        backSpeed: 100,
        backDelay: 700,
        loop: true
    }

    var typed = new Typed(".typer", options);

    jQuery(document).scroll(function() {
     if (jQuery(this).scrollTop() > 20) {
        jQuery('.container').css({"background-color":"black"});
        jQuery('#menu a').css({"color":"white"});
        $('.nav-toggle').css({"background":"white"});
        $('.nav-toggle span').css({"background":"black"});
        if ($('.nav-toggle span').hasClass('changed')){}
        else {
            $('.nav-toggle span').toggleClass('changed');
        }
        $('.logo img').attr('src','static/presscorp/images/logo-black.png');
        $('#menu a').hover(
            function() {
                $(this).css({"color":"#bfd732"});
            },
            function() {
                $(this).css({"color":"white"});
            }
        );
     } else {
        jQuery('.container').css({"background-color":"white"});
        if ($(window).width() > 768){ jQuery('#menu a').css({"color":"black"});}
        $('.nav-toggle').css({"background":"black"});
        $('.nav-toggle span').css({"background":"white"});
        $('.nav-toggle span').removeClass('changed');
        $('.logo img').attr('src','static/presscorp/images/logo.png');
        $('#menu a').hover(
            function() {
                $(this).css({"color":"#bfd732"});
            },
            function() {
                $(this).css({"color":"black"});
            }
        );
     }
     });

     $(window).resize(function(){
        if($(this).width() > 768 && $(document).scrollTop() < 20) { jQuery('#menu a').css({"color":"black"}); }
        else { jQuery('#menu a').css({"color":"white"});}
     });
 });