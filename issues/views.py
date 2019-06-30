from django.shortcuts import render, redirect
from .forms import CreateIssue
from django.contrib.auth.decorators import login_required


def tracker(request):
    """ Renders the Tracker page that tracks and manages all bug reports and feature requests """
    return render(request, 'tracker.html')


# @login_required
def create_bug(request):
    """ Render page providing form to user to create a new bug """
    if request.method == 'POST':
        form = CreateIssue(request.POST)
        # set issue type to 'bug'
        # save to db
        return redirect('tracker')
    else:
        form = CreateIssue()
    return render(request, 'create_bug.html', {'form': form})


# @login_required
def create_feature(request):
    """ Render page providing form to user to create a new feature request """
    if request.method == 'POST':
        form = CreateIssue(request.POST)
        # set issue type to 'feature'
        # save to db
        return redirect('tracker')
    else:
        form = CreateIssue()
    return render(request, 'create_feature.html', {'form': form})
