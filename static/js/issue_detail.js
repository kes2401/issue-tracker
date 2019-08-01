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
    let user = $('#new-comment-btn')[0].dataset.user;
    let requestStr = `/issues/tracker/issue_detail/${issueID}/add_comment`;
    let responseData = '';

    $.post({
        url: requestStr,
        headers: {
            'X-CSRFToken': csrftoken
        },
        data: {
            'comment': comment
        },
        success: function (response) {
            responseData = response;
            addCommentCard();
        }
    });

    $('#new-comment-field')[0].value = '';
    $('#new-comment-btn').addClass('disabled');
    $('#new-comment-btn').attr('disabled', '');
    $('#new-comment-btn').attr('aria-disabled', 'true');


    // add new comment to document
    function addCommentCard() {
        let newCommentStr = `<div class="comment-card w-75 mx-auto pl-4">
                                    <i class="fa fa-chevron-down fa-2x text-black-50"></i>
                                </div>
                                <div class="card heading-border mb-3 w-75 mx-auto">
                                    <div class="card-header">
                                        <p class="text-muted pt-1 mb-0">${user}</p>
                                    </div>
                                    <div class="card-body">
                                        <p class="card-text mt-2 mb-4">${comment}</p>
                                        <hr>
                                        <p class="text-muted text-right mb-0">Commented on ${responseData.substring(0, responseData.indexOf('.'))}</p>
                                    </div>
                                </div>`;
        $('#comment-container').append(newCommentStr);
        let commentCount = Number.parseInt(document.getElementById('comments-count').innerText) + 1;
        document.getElementById('comments-count').innerText = commentCount;
    }

});

// Add/Remove votes
$('.vote-btn').click(function () {

    let voteStatus = $('.vote-btn')[0].dataset.voteStatus;
    let issueID = Number.parseInt($('#new-comment-btn')[0].dataset.issueId);


    if (voteStatus == 'false') {
        $('.vote-btn')[0].dataset.voteStatus = 'true';
        $('.vote-btn').html('<i class="fas fa-thumbs-up fa-2x text-muted"></i>');
        $('.vote-btn').addClass('text-info');
        postVote('add');
    } else {
        $('.vote-btn')[0].dataset.voteStatus = 'false';
        $('.vote-btn').html('<i class="far fa-thumbs-up fa-2x text-muted"></i>');
        $('.vote-btn').removeClass('text-info');
        postVote('remove');
    }


    function postVote(status) {
        if (status === 'remove') {
            requestStr = `/issues/tracker/issue_detail/${issueID}/remove_vote`;
        } else {
            requestStr = `/issues/tracker/issue_detail/${issueID}/add_vote`;
        }

        $.post({
            url: requestStr,
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function (response) {
                updateVoteCount(response);
            },
            error: function (_xhr, err) {
                console.log(err);
            }
        });
    }

    function updateVoteCount(status) {
        if (status === 'added') {
            let voteCount = Number.parseInt($('#vote-count').text());
            voteCount += 1;
            $('#vote-count').text(voteCount);
        } else if (status === 'removed') {
            let voteCount = Number.parseInt($('#vote-count').text());
            voteCount -= 1;
            $('#vote-count').text(voteCount);
        }
    }

})


// get csrf token from cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}