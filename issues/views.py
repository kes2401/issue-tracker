from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CreateIssue
from .models import Issue


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
                request, 'You have successfully report a new bug.')
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
