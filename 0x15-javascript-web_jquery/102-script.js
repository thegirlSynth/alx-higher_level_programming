$(document).ready(function() {
    $("INPUT#btn_translate").click(function() {
        var languageCode = $("INPUT#language_code").val();
        $.ajax({
            url: "https://www.fourtonfish.com/hellosalut/hello/",
            type: 'GET',
            dataType: "json",
            data: {
                lang: languageCode
            },
            success: function(result) {
                $("DIV#hello").text(result.hello);
            }
        });
    });
});
