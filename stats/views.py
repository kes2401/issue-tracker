from django.shortcuts import render


def stats(request):
    """ Renders the Stats page to display statistics for bug reports and feature requests """
    return render(request, 'stats.html')
