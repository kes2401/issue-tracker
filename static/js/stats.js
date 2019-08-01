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