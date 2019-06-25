from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm


def login(request):
    """ Return login page containing the login form """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            print(messages)
            if user:
                auth.login(user=user, request=request)
                messages.success(
                    request, 'You have been succesfully logged in!')
                return redirect(reverse('index'))
            else:
                messages.error(
                    request, 'Your username or password is incorrect')
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


@login_required
def logout(request):
    """ Log the user out and redirect to index page """
    auth.logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect(reverse('index'))
