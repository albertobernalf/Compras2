(function($) {
    $(document).on('formset:added', function(event, $row, formsetName) {

    alert ("EntreEvento form handled");
        if (formsetName == 'author_set') {
            // Do something
        }
    });

    $(document).on('formset:removed', function(event, $row, formsetName) {
        // Row removed
    });
})(django.jQuery);