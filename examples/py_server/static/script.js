$(document).ready(function() {
    $('#input-submit').click(function(evt) {
        var name = $('input#name').val()

        $.ajax({
            "url": "/submit",
            "method": "GET",
            "data": {'name': name},
            success: function(data) {
                $('#text-box').text(data);
            },
            error: function (error) {
                alert("script:updateContent:"+error.responseText);
            }
        })
    })
});
