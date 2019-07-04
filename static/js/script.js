$(document).ready(function () {

    // Issue Detail Page
    if (document.title === 'UnicornAttractor - Issue & Feature Tracker - Issue Detail') {

        let csrftoken = getCookie('csrftoken');

        const commentBtn = $('#new-comment-btn');

        // Manage active state of comment button
        $('#new-comment-field').keyup(function () {
            if (!$('#new-comment-field')[0].value) {
                $('#new-comment-btn').addClass('disabled');
                $('#new-comment-btn').attr('disabled', '');
                $('#new-comment-btn').attr('aria-disabled', 'true');
            } else {
                $('#new-comment-btn').removeClass('disabled');
                $('#new-comment-btn').removeAttr('disabled');
                $('#new-comment-btn').removeAttr('aria-disabled', 'true');
            }
        });


        // Add new comment
        $('#new-comment-btn').click(function () {

            // Submit POST request to back-end to add comment to db
            let issueID = Number.parseInt($('#new-comment-btn')[0].dataset.issueId);
            let comment = $('#new-comment-field')[0].value;
            let requestStr = `/issues/tracker/feature_detail/${issueID}/add_comment`;

            $.post({
                url: requestStr,
                headers: {
                    'X-CSRFToken': csrftoken
                },
                data: {
                    'comment': comment
                },
                success: function () { console.log('Successfully saved to DB') }
            });

            $('#new-comment-field')[0].value = '';  // -> then disable button again
            $('#new-comment-btn').addClass('disabled');
            $('#new-comment-btn').attr('disabled', '');
            $('#new-comment-btn').attr('aria-disabled', 'true');

            // add new comment to document


        });



        // get csrf token from cookie
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                let cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    let cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }


    }



});