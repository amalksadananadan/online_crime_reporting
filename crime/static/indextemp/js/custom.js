$(document).ready(function() {
    "use strict";

    /*------------------------------------------------------------------
        Accordion
     -------------------------------------------------------------------*/

    $( "#accordion" ).accordion();
    $( "#accordion2" ).accordion();
    $( "#accordion3" ).accordion();
    $( "#accordion4" ).accordion();

    /*------------------------------------------------------------------
        Tabs
     -------------------------------------------------------------------*/

    $( "#tabs" ).tabs();

    /*------------------------------------------------------------------
        Parallax
     -------------------------------------------------------------------*/

    function parallaxInit() {
        $('.bg1').parallax("10%", 0.6);
        $('.bg2').parallax("10%", 0.6);
    }
    parallaxInit();

    /*------------------------------------------------------------------
        Testimonials
     -------------------------------------------------------------------*/

        $('.testi_slider').cycle({
            fx:      'scrollHorz',
            pager:   '.pagers',
        });

    /*------------------------------------------------------------------
     Slider
     -------------------------------------------------------------------*/


    $('.slider').cycle({
            fx:      'scrollHorz',
        });

    $('.main_slider').owlCarousel({
        items: 1,
        animateIn: 'pulse',
        autoplay: true,
        loop: true,
        margin: 10,
        nav: true,
    });

    /*------------------------------------------------------------------
        Animation
     -------------------------------------------------------------------*/

    $(window).load(function(){

        var width = $(window).width();
        if(width < 480)
        {
            $(".animated").removeClass('animated, slide');
            $(".animated").removeClass('animated, fade');
            $(".animated").removeClass('animated, hatch');
            $(".animated").removeClass('animated, entrance');
        }

    });


    jQuery('.animated').appear();
    jQuery(document.body).on('appear', '.fade', function() {
        jQuery(this).each(function(){ jQuery(this).addClass('ae-animation-fade') });
    });
    jQuery(document.body).on('appear', '.slide', function() {
        jQuery(this).each(function(){ jQuery(this).addClass('ae-animation-slide') });
    });
    jQuery(document.body).on('appear', '.hatch', function() {
        jQuery(this).each(function(){ jQuery(this).addClass('ae-animation-hatch') });
    });
    jQuery(document.body).on('appear', '.entrance', function() {
        jQuery(this).each(function(){ jQuery(this).addClass('ae-animation-entrance') });
    });

    /*------------------------------------------------------------------
        Counter
     -------------------------------------------------------------------*/

    jQuery('.statistics').appear();
    jQuery('.skill_counter').appear();

    jQuery(document.body).on('appear', function() {
        $({someValue: 1000}).animate({someValue: 5649}, {
            duration: 3000,
            easing:'easeInQuint',
            step: function() {
                $('#counter1 a').text(Math.round(this.someValue));
            }
        });
    });

    jQuery(document.body).on('appear', function() {
        $({someValue: 100}).animate({someValue: 340}, {
            duration: 3000,
            easing:'easeInQuint',
            step: function() {
                $('#counter2 a').text(Math.round(this.someValue));
            }
        });
    });

    jQuery(document.body).on('appear', function() {
        $({someValue: 100}).animate({someValue: 240}, {
            duration: 3000,
            easing:'easeInQuint',
            step: function() {
                $('#counter3 a').text(Math.round(this.someValue));
            }
        });
    });

    jQuery(document.body).on('appear', function() {
        $({someValue: 100}).animate({someValue: 240}, {
            duration: 3000,
            easing:'easeInQuint',
            step: function() {
                $('#counter4 a').text(Math.round(this.someValue));
            }
        });
    });

    jQuery(document.body).on('appear', function() {
        $({someValue: 1000}).animate({someValue: 5489}, {
            duration: 3000,
            easing:'easeInQuint',
            step: function() {
                $('#counter5 a').text(Math.round(this.someValue));
            }
        });
    });

    jQuery(document.body).on('appear', function() {
        $({someValue: 100}).animate({someValue: 207}, {
            duration: 3000,
            easing:'easeInQuint',
            step: function() {
                $('#counter6 a').text(Math.round(this.someValue));
            }
        });
    });

    jQuery(document.body).on('appear', function() {
        $({someValue: 1000}).animate({someValue: 4935}, {
            duration: 3000,
            easing:'easeInQuint',
            step: function() {
                $('#counter7 a').text(Math.round(this.someValue));
            }
        });
    });

    /*------------------------------------------------------------------
     Progress Bars
     -------------------------------------------------------------------*/



    (function($) {

        $.fn.progress_fnc = function(options) {
            var settings = $.extend({
                type: 'start'
            }, options);

            var div = $(this);
            var progress = div.find('.progress');

            progress.each(function() {
                var self = $(this);
                var progress_bar = self.find('.bar');
                var progress_label = self.find('.labels, .cssProgress-label2');
                var progress_value = progress_bar.data('percent');
                var percentage = parseInt(progress_value, 10) + '%';

                progress_bar.css({'width': '0%', 'transition': 'none', '-webkit-transition': 'none', '-moz-transition': 'none'});

                if(settings.type == 'start') {

                    progress_bar.animate({
                        width: percentage
                    }, {
                        duration: 1000,
                        step: function(x) {
                            progress_label.text(Math.round(x) + '%');
                        }
                    });

                } else if(settings.type == 'reset') {
                    progress_bar.css('width', '0%');
                    progress_label.text('0%');
                }

            });
        }

    }(jQuery));


    jQuery('.progress_bar_wrap').appear();
    jQuery(document.body).on('appear', '.progress_bar_wrap', function() {
        $('#progress_bars').progress_fnc();
    });


    /*------------------------------------------------------------------
     Validate
     -------------------------------------------------------------------*/

    $( "#submit-form" ).on( "click", function() {
        var errors = "";

        var contact_name = document.getElementById("user_name");
        var contact_email_address = document.getElementById("email");

        if(contact_name.value == ""){
            errors+= 'Please provide your name.';
        }
        else if(contact_email_address.value == ""){
            errors+= 'Please provide an email address.';
        }
        else if(contact_email_address.value == ""){
            errors+= 'Please provide a valid email address.';
        }
        else if(contact_subject.value == ""){
            errors+= 'Please provide a Reason.';
        }


        if(errors)
        {
            document.getElementById("error").style.display = "block";
            document.getElementById("error").innerHTML = errors;
            return false;
        }

        else{

            $.ajax({
                type: "POST",
                url: 'process.php',
                data: $("#injury_form").serialize(),
                success: function(msg)
                {
                    if(msg == 'success')
                    {
                        document.getElementById("error").style.display = "none";
                        document.getElementById("contact_name").value = "";
                        document.getElementById("contact_email").value = "";
                        document.getElementById("contact_subject").value = "";
                        document.getElementById("message").value = "";
                        $("#injury_form").hide();
                        document.getElementById("success").style.display = "block";
                        document.getElementById("success").innerHTML = "Thank You! We'll contact you shortly.";
                    }else{
                        document.getElementById("error").style.display = "block";
                        document.getElementById("error").innerHTML = "Oops! Something went wrong while prceeding.";
                    }
                }

            });

        }
    });


    /*------------------------------------------------------------------
     Inner Contact Form
     -------------------------------------------------------------------*/

    $( "#submit" ).on( "click", function() {
        var errors = "";

        var contact_name = document.getElementById("name");
        var contact_email_address = document.getElementById("email");

        if(contact_name.value == ""){
            errors+= 'Please provide your name.';
        }
        else if(contact_email_address.value == ""){
            errors+= 'Please provide an email email.';
        }
        else if(contact_email_address.value == ""){
            errors+= 'Please provide a valid email.';
        }
        else if(contact_subject.value == ""){
            errors+= 'Please provide a Reason.';
        }


        if(errors)
        {
            document.getElementById("error").style.display = "block";
            document.getElementById("error").innerHTML = errors;
            return false;
        }

        else{

            $.ajax({
                type: "POST",
                url: 'process.php',
                data: $("#single_form").serialize(),
                success: function(msg)
                {
                    if(msg == 'success')
                    {
                        document.getElementById("error").style.display = "none";
                        document.getElementById("contact_name").value = "";
                        document.getElementById("contact_email").value = "";
                        $("#single_form").hide();
                        document.getElementById("success").style.display = "block";
                        document.getElementById("success").innerHTML = "Thank You! We'll contact you shortly.";
                    }else{
                        document.getElementById("error").style.display = "block";
                        document.getElementById("error").innerHTML = "Oops! Something went wrong while prceeding.";
                    }
                }

            });

        }
    });


    /*------------------------------------------------------------------
        Validate Footer Email
    -------------------------------------------------------------------*/

    $( "#send" ).on( "click", function() {
        var errors = "";

        var contact_email_address = document.getElementById("subcribe_email");

        if(contact_email_address.value == ""){
            errors+= 'Please provide an email address.';
        }
        else if(contact_email_address.value == ""){
            errors+= 'Please provide a valid email address.';
        }


        if(errors)
        {
            document.getElementById("error").style.display = "block";
            document.getElementById("error").innerHTML = errors;
            return false;
        }

        else{

            $.ajax({
                type: "POST",
                url: 'process.php',
                data: $("#footer_mail").serialize(),
                success: function(msg)
                {
                    if(msg == 'success')
                    {
                        document.getElementById("error").style.display = "none";
                        document.getElementById("subcribe_email").value = "";
                        document.getElementById("message").value = "";
                        $("#footer_mail").hide();
                        document.getElementById("success").style.display = "block";
                        document.getElementById("success").innerHTML = "Thank You! We'll contact you shortly.";
                    }else{
                        document.getElementById("error").style.display = "block";
                        document.getElementById("error").innerHTML = "Oops! Something went wrong while prceeding.";
                    }
                }

            });

        }
    });

    /*------------------------------------------------------------------
     Contact Form 
    -------------------------------------------------------------------*/

    $( "#contact_submit" ).on( "click", function() {
        var errors = "";

        var contact_name = document.getElementById("contact_name");
        var contact_email_address = document.getElementById("contact_email");

        if(contact_name.value == ""){
            errors+= 'Please provide your name.';
        }
        else if(contact_email_address.value == ""){
            errors+= 'Please provide an email email.';
        }
        else if(contact_email_address.value == ""){
            errors+= 'Please provide a valid email.';
        }
        else if(contact_subject.value == ""){
            errors+= 'Please provide a Reason.';
        }


        if(errors)
        {
            document.getElementById("error").style.display = "block";
            document.getElementById("error").innerHTML = errors;
            return false;
        }

        else{

            $.ajax({
                type: "POST",
                url: 'process.php',
                data: $("#contact_form").serialize(),
                success: function(msg)
                {
                    if(msg == 'success')
                    {
                        document.getElementById("error").style.display = "none";
                        document.getElementById("contact_name").value = "";
                        document.getElementById("contact_email").value = "";
                        $("#contact_form").hide();
                        document.getElementById("success").style.display = "block";
                        document.getElementById("success").innerHTML = "Thank You! We'll contact you shortly.";
                    }else{
                        document.getElementById("error").style.display = "block";
                        document.getElementById("error").innerHTML = "Oops! Something went wrong while prceeding.";
                    }
                }

            });

        }
    });


    /*------------------------------------------------------------------
     Consultant Form 
    -------------------------------------------------------------------*/

    $( "#get_consult" ).on( "click", function() {
        var errors = "";

        var contact_name = document.getElementById("user_name");
        var contact_email_address = document.getElementById("user_email");

        if(contact_name.value == ""){
            errors+= 'Please provide your name.';
        }
        else if(contact_email_address.value == ""){
            errors+= 'Please provide an email email.';
        }
        else if(contact_email_address.value == ""){
            errors+= 'Please provide a valid email.';
        }
        else if(contact_subject.value == ""){
            errors+= 'Please provide a Reason.';
        }


        if(errors)
        {
            document.getElementById("error").style.display = "block";
            document.getElementById("error").innerHTML = errors;
            return false;
        }

        else{

            $.ajax({
                type: "POST",
                url: 'process.php',
                data: $("#consult_form").serialize(),
                success: function(msg)
                {
                    if(msg == 'success')
                    {
                        document.getElementById("error").style.display = "none";
                        document.getElementById("contact_name").value = "";
                        document.getElementById("contact_email").value = "";
                        $("#consult_form").hide();
                        document.getElementById("success").style.display = "block";
                        document.getElementById("success").innerHTML = "Thank You! We'll contact you shortly.";
                    }else{
                        document.getElementById("error").style.display = "block";
                        document.getElementById("error").innerHTML = "Oops! Something went wrong while prceeding.";
                    }
                }

            });

        }
    });



    /*------------------------------------------------------------------
     Back to Top
     -------------------------------------------------------------------*/

    jQuery(document).ready(function($){
    // browser window scroll (in pixels) after which the "back to top" link is shown
        var offset = 300,
    //browser window scroll (in pixels) after which the "back to top" link opacity is reduced
            offset_opacity = 1200,
    //duration of the top scrolling animation (in ms)
            scroll_top_duration = 1400,
    //grab the "back to top" link
            $back_to_top = $('.cd-top');

    //hide or show the "back to top" link
        $(window).scroll(function(){
            ( $(this).scrollTop() > offset ) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
            if( $(this).scrollTop() > offset_opacity ) {
                $back_to_top.addClass('cd-fade-out');
            }
        });

    //smooth scroll to top
        $back_to_top.on('click', function(event){
            event.preventDefault();
            $('body,html').animate({
                    scrollTop: 0 ,
                }, scroll_top_duration
            );
        });

    });


});