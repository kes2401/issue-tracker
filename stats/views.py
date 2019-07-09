from django.shortcuts import render
from issues.models import Issue, IssueComment, IssueVote
from operator import itemgetter
from django.http import HttpResponse, JsonResponse


def stats(request):
    """ Renders the Stats page to display statistics for bug reports and feature requests """

    all_bugs_chart = '' + str(Issue.objects.filter(issue_type='bug').filter(status='pending').count()) + ',' + str(Issue.objects.filter(issue_type='bug').filter(
        status='in progress').count()) + ',' + str(Issue.objects.filter(issue_type='bug').filter(status='done').count())

    all_features_chart = '' + str(Issue.objects.filter(issue_type='feature').filter(status='pending').count()) + ',' + str(Issue.objects.filter(issue_type='feature').filter(
        status='in progress').count()) + ',' + str(Issue.objects.filter(issue_type='feature').filter(status='done').count())

    return render(request, 'stats.html', {
        'all_bugs_chart': all_bugs_chart,
        'all_features_chart': all_features_chart
    })


def top_bugs(request):
    """ Returns JSON data for the 5 top voted bugs to be displayed on chart """

    open_bugs = Issue.objects.filter(issue_type='bug').exclude(status='done')
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
        issue_type='feature').exclude(status='done')
    top_voted_features = []
    for feature in open_features:
        temp_dict = {}
        temp_dict['title'] = feature.title
        temp_dict['count'] = IssueVote.objects.filter(issue=feature.pk).count()
        top_voted_features.append(temp_dict)

    top_voted_features = sorted(
        top_voted_features, key=itemgetter('count'), reverse=True)[:5]

    return JsonResponse(top_voted_features, safe=False)
