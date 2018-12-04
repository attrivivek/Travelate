(function($, window, document) {
    $(document).ready(function () {
        $(".hotel-score p").each(function() {
            if ( parseFloat( $(this).text() ) >= 0.80 ) {
                $(this).css("color", "green");
            }

            else if ( parseFloat( $(this).text() ) < 0.80 && parseFloat( $(this).text() ) >= 0.5 ) {
                $(this).css("color", "orange");
            }

            else {
                $(this).css("color", "red");
            }
        });
    });
}(window.jQuery, window, document));