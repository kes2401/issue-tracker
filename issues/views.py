from django.shortcuts import render


def tracker(request):
    """ Renders the Tracker page that tracks and manages all bug reports and feature requests """
    return render(request, 'tracker.html')
