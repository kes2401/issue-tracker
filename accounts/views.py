from django.shortcuts import render


def login(request):
    """ Return login page containing login form so that user can log into the application """
    return render(request, 'login.html')
