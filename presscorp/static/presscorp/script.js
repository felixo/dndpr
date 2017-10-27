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
        backDelay: 500,
        loop: true
    }

    var typed = new Typed(".typer", options);
 });