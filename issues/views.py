from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CreateIssue
from .models import Issue, IssueComment
from django.http import HttpResponse


def tracker(request):
    """ Renders the Tracker page that tracks and manages all bug reports and feature requests """
    bugs = Issue.objects.filter(issue_type='bug')
    features = Issue.objects.filter(issue_type='feature')
    return render(request, 'tracker.html', {'bugs': bugs, 'features': features})


# @login_required
def create_bug(request):
    """ Render page providing form to user to report a new bug """
    if request.method == 'POST':
        form = CreateIssue(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.issue_type = 'bug'
            instance.author = request.user
            instance.save()
            messages.success(
                request, 'You have successfully reported a new bug.')
        else:
            messages.error(
                request, 'Something went wrong. Please try again.')
        return redirect('tracker')
    else:
        form = CreateIssue()
    return render(request, 'create_bug.html', {'form': form})


# @login_required
def create_feature(request):
    """ Render page providing form to user to create a new feature request """
    if request.method == 'POST':
        form = CreateIssue(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.issue_type = 'feature'
            instance.author = request.user
            instance.save()
            messages.success(
                request, 'You have successfully submitted a new feature request.')
        else:
            messages.error(
                request, 'Something went wrong. Please try again.')
        return redirect('tracker')
    else:
        form = CreateIssue()
    return render(request, 'create_feature.html', {'form': form})


def bug_detail(request, id):
    bug = Issue.objects.get(pk=id)
    return render(request, 'issue_detail.html', {'issue': bug})


@ensure_csrf_cookie
def feature_detail(request, id):
    feature = Issue.objects.get(pk=id)
    comments = IssueComment.objects.all().filter(issue=id)
    return render(request, 'issue_detail.html', {'issue': feature, 'comments': comments})


def add_comment(request, id):
    if request.method == 'POST':
        new_comment = IssueComment(comment=request.POST.get('comment'))
        currrent_user = User.objects.get(username=request.user)
        current_issue = Issue.objects.get(pk=id)
        new_comment.user = currrent_user
        new_comment.issue = current_issue
        new_comment.save()
        savetime = IssueComment.objects.get(
            user=request.user, comment=request.POST.get('comment'), issue=current_issue.pk)
        return HttpResponse(savetime.date_published)
