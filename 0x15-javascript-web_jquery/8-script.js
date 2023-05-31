$(document).ready(function() {
    $.ajax({
        url: "https://swapi-api.alx-tools.com/api/films/?format=json",
        dataType: "json",
        success: function(data) {
            $.each(data.results, function(index, value){
                $("#list_movies").append("<li>" + value.title + "</li>");
            });
        }
    });
});
