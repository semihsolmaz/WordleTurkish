gameForm = $('.gameForm')

gameForm.submit(function (e) {
    e.preventDefault();
    $.ajax(
        {
            type: "POST",
            url: "/wordle/play/",
            data: gameForm.serialize(),
            cache: false,
            dataType: "json",
            success: function (response) {
                console.log(response.cell);
            }
        })
});