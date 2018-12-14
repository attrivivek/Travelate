(function($, window, document) {
    $(document).ready(function () {
        $(".hotel-score p:nth-child(2), .hotel-overall-score p:nth-child(2)").each(function() {
            if ( parseInt( $(this).text() ) >= 80 ) {
                $(this).css("color", "green");
            }

            else if ( parseInt( $(this).text() ) < 80 && parseInt( $(this).text() ) > 60 ) {
                $(this).css("color", "orange");
            }

            else {
                $(this).css("color", "red");
            }
        });
    });
}(window.jQuery, window, document));