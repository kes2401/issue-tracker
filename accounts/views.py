from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages


def login(request):
    """ Return login page containing login form so that user can log into the application """
    return render(request, 'login.html')


def logout(request):
    """ Log the user out and redirect to index page """
    auth.logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect(reverse('index'))
