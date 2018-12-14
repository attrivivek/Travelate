(function($, window, document) {
    $(document).ready(function () {
        $(".hotel-score p:nth-child(2), .hotel-overall-score p:nth-child(2)").each(function() {
            if ( parseFloat( $(this).text() ) >= 0.80 ) {
                $(this).css("color", "green");
            }

            else if ( parseFloat( $(this).text() ) < 0.80 && parseFloat( $(this).text() ) > 0.6 ) {
                $(this).css("color", "orange");
            }

            else {
                $(this).css("color", "red");
            }
        });
    });
}(window.jQuery, window, document));