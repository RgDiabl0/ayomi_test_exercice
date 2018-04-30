$(document).ready(function () {
    let page_name = window.location.pathname.replace('/', '');

    $(window).resize(function () {
        let navbar_height = $(".navbar-fixed-top").height();
        $(document.body).css("padding-top", navbar_height);

        if (page_name === 'profile') {
            let hamburger_content = $("#hamburger-content");
            if (hamburger_content.length > 0) {
                hamburger_content.css("margin-top", navbar_height);
                hamburger_content.css("height", innerHeight - navbar_height);
                $("#hamburger-overlay").css("margin-top", navbar_height);
            }
        }
    }).resize();

    function modify_infos() {
        const testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,}$/i;
        let email = $("input[name=new-email]");

        if (testEmail.test(email.val())) {
            $.ajax({
                url: 'modify_infos',
                type: 'POST',
                data: {'email': email.val()},
                success: function (data) {
                    $("#email span:last-of-type").text(data['email']);
                    $("#modify-infos-modal").modal('toggle');
                    $("#modify-infos-modal input").val('')
                }
            })
        }
    }

    if (page_name === 'profile') {
        $("#menu a[href*=" + page_name + "]").addClass("active");

        let hamburger_overlay = $("#hamburger-overlay");
        if (hamburger_overlay.length > 0) {
            let hamburger_checkbox = $("#hamburger-checkbox");

            hamburger_checkbox.change(function () {
                if (hamburger_checkbox.is(':checked'))
                    $(document.body).css("overflow", "hidden");
                else
                    $(document.body).css("overflow", "initial");
            });

            hamburger_overlay.click(function () {
                hamburger_checkbox.prop('checked', false);
            })
        }
    }
})
;