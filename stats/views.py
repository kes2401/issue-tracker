from django.shortcuts import render
from issues.models import Issue, IssueComment, IssueVote
from operator import itemgetter
from django.http import HttpResponse, JsonResponse
from django.db.models import Count
from datetime import datetime


def stats(request):
    """ Renders the Stats page to display statistics for bug reports and feature requests """

    all_bugs_chart = '' + str(Issue.objects.filter(issue_type='bug').filter(status='pending').count()) + ',' + str(Issue.objects.filter(issue_type='bug').filter(
        status='in progress').count()) + ',' + str(Issue.objects.filter(issue_type='bug').filter(status='closed').count())

    all_features_chart = '' + str(Issue.objects.filter(issue_type='feature').filter(status='pending').count()) + ',' + str(Issue.objects.filter(issue_type='feature').filter(
        status='in progress').count()) + ',' + str(Issue.objects.filter(issue_type='feature').filter(status='closed').count())

    return render(request, 'stats.html', {
        'all_bugs_chart': all_bugs_chart,
        'all_features_chart': all_features_chart
    })


def top_bugs(request):
    """ Returns JSON data for the 5 top voted bugs to be displayed on chart """

    open_bugs = Issue.objects.filter(issue_type='bug').exclude(status='closed')
    top_voted_bugs = []
    for bug in open_bugs:
        temp_dict = {}
        temp_dict['title'] = bug.title
        temp_dict['count'] = IssueVote.objects.filter(issue=bug.pk).count()
        top_voted_bugs.append(temp_dict)

    top_voted_bugs = sorted(
        top_voted_bugs, key=itemgetter('count'), reverse=True)[:5]

    return JsonResponse(top_voted_bugs, safe=False)


def top_features(request):
    """ Returns JSON data for the 5 top voted features to be displayed on chart """

    open_features = Issue.objects.filter(
        issue_type='feature').exclude(status='closed')
    top_voted_features = []
    for feature in open_features:
        temp_dict = {}
        temp_dict['title'] = feature.title
        temp_dict['count'] = IssueVote.objects.filter(issue=feature.pk).count()
        top_voted_features.append(temp_dict)

    top_voted_features = sorted(
        top_voted_features, key=itemgetter('count'), reverse=True)[:5]

    return JsonResponse(top_voted_features, safe=False)


def bug_closure(request):
    """ Returns JSON data for the last 5 dates on which bugs were closed, and how many on each date """

    closed_bugs = Issue.objects.filter(
        issue_type='bug').filter(status='closed')
    closed_dates = closed_bugs.values('date_complete').distinct()[:5]
    bug_closures_per_date = []
    for date in closed_dates:
        temp_dict = {}
        temp_dict['date'] = date['date_complete'].strftime("%m/%d/%Y")
        temp_dict['count'] = closed_bugs.filter(
            date_complete=date['date_complete']).count()
        bug_closures_per_date.append(temp_dict)

    bug_closures_per_date = sorted(
        bug_closures_per_date, key=itemgetter('date'), reverse=False)

    return JsonResponse(bug_closures_per_date, safe=False)


def feature_closure(request):
    """ Returns JSON data for the last 5 dates on which features were closed, and how many on each date """

    closed_features = Issue.objects.filter(
        issue_type='feature').filter(status='closed')
    closed_dates = closed_features.values('date_complete').distinct()[:5]
    feature_closures_per_date = []
    for date in closed_dates:
        temp_dict = {}
        temp_dict['date'] = date['date_complete'].strftime("%m/%d/%Y")
        temp_dict['count'] = closed_features.filter(
            date_complete=date['date_complete']).count()
        feature_closures_per_date.append(temp_dict)

    feature_closures_per_date = sorted(
        feature_closures_per_date, key=itemgetter('date'), reverse=False)

    return JsonResponse(feature_closures_per_date, safe=False)
