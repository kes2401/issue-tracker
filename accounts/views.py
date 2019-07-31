from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from issues.models import Issue
from checkout.models import Order, OrderLineItem
from cart.models import Cart


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
                return redirect(reverse('profile'))
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


def register(request):
    """ Render user registration page """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(
                username=request.POST['username'], password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(
                    request, 'You have been successfully registered!')
                return redirect(reverse('index'))
            else:
                messages.error(request, 'Unable to register your account.')
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'register.html', {'registration_form': registration_form})


@login_required
def profile(request):
    """ Renders profile dashboard for logged in user """
    current_user = User.objects.get(username=request.user)
    user_bugs = Issue.objects.all().filter(issue_type='bug').filter(author=current_user)
    user_orders = Order.objects.filter(user=current_user)
    feature_orders = OrderLineItem.objects.filter(order__in=user_orders).filter(request_type='new feature')
    vote_orders = OrderLineItem.objects.filter(order__in=user_orders).filter(request_type='feature vote')
    cart_count = Cart.objects.filter(user=request.user).count()

    total_paid_features = 0
    total_paid_votes = 0
    for item in feature_orders:
        total_paid_features += item.amount_paid
    for item in vote_orders:
        total_paid_votes += item.amount_paid

    return render(request, 'profile.html', {
        'user_bugs': user_bugs,
        'feature_orders': feature_orders,
        'vote_orders': vote_orders,
        'total_paid_features': total_paid_features,
        'total_paid_votes': total_paid_votes,
        'cart_count': cart_count
    })
