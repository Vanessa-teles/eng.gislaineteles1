/*
 * Main.js
 * Site functionality
 */
(function($) {
    var $window = $(window),
        $body = $('body'),
        $header = $('#header'),
        $banner = $('#banner');

    // Breakpoints
    breakpoints({
        xlarge: [ '1281px', '1680px' ],
        large: [ '981px', '1280px' ],
        medium: [ '737px', '980px' ],
        small: [ '481px', '736px' ],
        xsmall: [ null, '480px' ]
    });

    // Play initial animations on page load
    $window.on('load', function() {
        window.setTimeout(function() {
            $body.removeClass('is-preload');
        }, 100);
    });

    // Header
    if ($header.hasClass('alt')) {
        $window.on('resize', function() {
            window.setTimeout(function() {
                if ($window.scrollTop() > 0) {
                    $header.removeClass('alt');
                } else {
                    $header.addClass('alt');
                }
            }, 0);
        }).trigger('resize');

        $window.on('scroll', function() {
            if ($window.scrollTop() > 0) {
                $header.removeClass('alt');
            } else {
                $header.addClass('alt');
            }
        });
    }

    // Banner
    if ($banner.length > 0 && $header.hasClass('alt')) {
        $window.on('resize', function() {
            window.setTimeout(function() {
                if ($window.scrollTop() > 0) {
                    $header.removeClass('alt');
                } else {
                    $header.addClass('alt');
                }
            }, 0);
        }).trigger('resize');

        $banner.scrollex({
            bottom: $header.outerHeight(),
            terminate: function() { $header.removeClass('alt'); },
            enter: function() { $header.addClass('alt'); },
            leave: function() { $header.removeClass('alt'); }
        });
    }

    // Smooth scrolling for anchor links
    $('a[href*="#"]:not([href="#"])').click(function() {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html, body').animate({
                    scrollTop: target.offset().top
                }, 1000);
                return false;
            }
        }
    });

})(jQuery);

