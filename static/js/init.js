(function ($) {
    $(function () {

        $('.button-collapse').sideNav();

    });

    $(function () {

        $('select').material_select();

    });

    $('#favorite').click(function () {
        var fc = $('#favorite_count');
        if ($.trim($(this).text()) === 'star') {

            $(this).html('star_border');
            fc.html((parseInt(fc.text()) - 1).toString())
        }
        else {
            var size = $(this).css('font-size')
            $(this).animate({fontSize: '10em'}, "slow").delay(500);
            $(this).animate({fontSize: size}, "fast");
            $(this).html('star');
            fc.html((parseInt(fc.text()) + 1).toString())
        }
    });

    $("[id^=stock_dec]").click(function () {
        var num = this.id.slice('stock_dec'.length);
        var count = $('#stock_count' + num);
        if (count.val() > 0) {
            count.val((parseInt(count.val()) - 1).toString());
        }
    });

    $("[id^=stock_inc]").click(function () {
        var num = this.id.slice('stock_inc'.length);
        var count = $('#stock_count' + num);
        count.val((parseInt(count.val()) + 1).toString());
    });


    $('#available_switch').click(function () {
        var av = $('#available');
        if ($.trim(av.text()) === 'Disponible') {
            av.html('No Disponible');
            av.removeClass("light-green-text").addClass("grey-text")
        }
        else {
            av.html('Disponible');
            av.removeClass("grey-text").addClass("light-green-text")
        }
    });

    $("[id^=image_to_popup]").click(function () {
        var num = this.id.slice('image_to_popup'.length);
        var modal = document.getElementById('image_modal');
        var modalImg = document.getElementById('image_popup');
        var captionText = document.getElementById('image_popup_caption');
        var image = this.getElementsByTagName('img')[0];
        modal.style.display = "block";
        modalImg.src = image.src;
        captionText.innerHTML = image.alt;
    });

    $("#close").click(function () {
        var modal = document.getElementById('image_modal');
        modal.style.display = "none";
    });

})
(jQuery);

