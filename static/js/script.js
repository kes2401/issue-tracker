$(document).ready(function () {

    $('[data-toggle="tooltip"]').tooltip();

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


    }



    // Stats page
    if (document.title === 'UnicornAttractor - Issue & Feature Tracker - Stats') {

        // contexts
        const allBugsCtx = $('#allBugsChart');
        const allFeaturesCtx = $('#allFeaturesChart');
        const topVotedBugsCtx = $('#topVotedBugsChart');
        const topVotedFeaturesCtx = $('#topVotedFeaturesChart');
        const bugClosureCtx = $('#bugClosureChart');
        const featureClosureCtx = $('#featureClosureChart');

        // gather data
        const allBugsChartData = $('#allBugsChart')[0].dataset.chartdata.split(',').map(num => Number.parseInt(num));
        const allFeaturesChartData = $('#allFeaturesChart')[0].dataset.chartdata.split(',').map(num => Number.parseInt(num));

        $.get('/stats/top_bugs', data => {
            const labelArr = [];
            const dataArr = [];

            for (let obj of data) {
                labelArr.push(obj.title);
                dataArr.push(obj.count)
            }

            buildTopBugsChart(labelArr, dataArr);
        })

        $.get('/stats/top_features', data => {
            const labelArr = [];
            const dataArr = [];

            for (let obj of data) {
                labelArr.push(obj.title);
                dataArr.push(obj.count)
            }

            buildTopFeaturesChart(labelArr, dataArr);
        })

        $.get('/stats/bug_closure', data => {
            const labelArr = [];
            const dataArr = [];

            for (let obj of data) {
                labelArr.push(obj.date);
                dataArr.push(obj.count)
            }

            buildBugClosureChart(labelArr, dataArr);
        })

        $.get('/stats/feature_closure', data => {
            const labelArr = [];
            const dataArr = [];

            for (let obj of data) {
                labelArr.push(obj.date);
                dataArr.push(obj.count)
            }

            buildFeatureClosureChart(labelArr, dataArr);
        })

        // build charts
        function buildBugClosureChart(labels, dataset) {
            const bugClosureChart = new Chart(bugClosureCtx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Bug Closures',
                        data: dataset,
                        backgroundColor: [
                            'rgba(225, 176, 56, 0.7)',
                            'rgba(225, 176, 56, 0.7)',
                            'rgba(225, 176, 56, 0.7)',
                            'rgba(225, 176, 56, 0.7)',
                            'rgba(225, 176, 56, 0.7)'
                        ],
                        borderColor: [
                            'rgba(195, 146, 26, 1)',
                            'rgba(195, 146, 26, 1)',
                            'rgba(195, 146, 26, 1)',
                            'rgba(195, 146, 26, 1)',
                            'rgba(195, 146, 26, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    animation: {
                        animateScale: true
                    },
                    legend: false,
                    scales: {
                        yAxes: [{
                            ticks: {
                                min: 0,
                                stepSize: 1
                            }
                        }]
                    }
                }
            });
        }

        function buildFeatureClosureChart(labels, dataset) {
            const featuresClosureChart = new Chart(featureClosureCtx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Feature Closures',
                        data: dataset,
                        backgroundColor: [
                            'rgba(75, 192, 192, 0.7)',
                            'rgba(75, 192, 192, 0.7)',
                            'rgba(75, 192, 192, 0.7)',
                            'rgba(75, 192, 192, 0.7)',
                            'rgba(75, 192, 192, 0.7)'
                        ],
                        borderColor: [
                            'rgba(45, 162, 162, 1)',
                            'rgba(45, 162, 162, 1)',
                            'rgba(45, 162, 162, 1)',
                            'rgba(45, 162, 162, 1)',
                            'rgba(45, 162, 162, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    animation: {
                        animateScale: true
                    },
                    legend: false,
                    scales: {
                        yAxes: [{
                            ticks: {
                                min: 0,
                                stepSize: 1
                            }
                        }]
                    }
                }
            });
        }

        function buildTopBugsChart(labels, dataset) {
            const topVotedBugsChart = new Chart(topVotedBugsCtx, {
                type: 'horizontalBar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Votes',
                        data: dataset,
                        backgroundColor: [
                            'rgba(75, 192, 192, 0.7)',
                            'rgba(153, 102, 255, 0.7)',
                            'rgba(255, 159, 64, 0.7)'
                        ],
                        borderColor: [
                            'rgba(45, 162, 162, 1)',
                            'rgba(123, 72, 225, 1)',
                            'rgba(225, 129, 34, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    animation: {
                        animateScale: true
                    },
                    legend: false,
                    scales: {
                        xAxes: [{
                            ticks: {
                                min: 0,
                                stepSize: 1
                            }
                        }]
                    }
                }
            });
        }

        function buildTopFeaturesChart(labels, dataset) {
            const topVotedFeaturesChart = new Chart(topVotedFeaturesCtx, {
                type: 'horizontalBar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Votes',
                        data: dataset,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.7)',
                            'rgba(54, 162, 235, 0.7)',
                            'rgba(255, 206, 86, 0.7)'
                        ],
                        borderColor: [
                            'rgba(225, 69, 102, 1)',
                            'rgba(24, 132, 205, 1)',
                            'rgba(225, 176, 56, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    animation: {
                        animateScale: true
                    },
                    legend: false,
                    scales: {
                        xAxes: [{
                            ticks: {
                                min: 0,
                                stepSize: 1
                            }
                        }]
                    }
                }
            });
        }

        const allBugsChart = new Chart(allBugsCtx, {
            type: 'pie',
            data: {
                labels: ['Pending', 'In Progess', 'Closed'],
                datasets: [{
                    label: 'Status of all bugs reported',
                    data: allBugsChartData,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.7)',
                        'rgba(54, 162, 235, 0.7)',
                        'rgba(255, 206, 86, 0.7)'
                    ],
                    borderColor: [
                        'rgba(225, 69, 102, 1)',
                        'rgba(24, 132, 205, 1)',
                        'rgba(225, 176, 56, 1)'
                    ],
                    borderWidth: 1

                }]
            },
            options: {
                animation: {
                    animateScale: true
                },
                legend: {
                    display: true,
                    position: 'right'
                }
            }
        });

        const allFeaturesChart = new Chart(allFeaturesCtx, {
            type: 'pie',
            data: {
                labels: ['Pending', 'In Progess', 'Closed'],
                datasets: [{
                    label: 'Status of all bugs reported',
                    data: allFeaturesChartData,
                    backgroundColor: [
                        'rgba(75, 192, 192, 0.7)',
                        'rgba(153, 102, 255, 0.7)',
                        'rgba(255, 159, 64, 0.7)'
                    ],
                    borderColor: [
                        'rgba(45, 162, 162, 1)',
                        'rgba(123, 72, 225, 1)',
                        'rgba(225, 129, 34, 1)'
                    ],
                    borderWidth: 1

                }]
            },
            options: {
                animation: {
                    animateScale: true
                },
                legend: {
                    display: true,
                    position: 'right'
                }
            }

        });



    }


});