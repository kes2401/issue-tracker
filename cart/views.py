from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import CartContent
from django.http import HttpResponse

def view_cart(request):
    """ Renders the cart with all products selected by the logged in user """
    return render(request, 'cart.html')

def add_to_cart(request, id):
    """ Adds an item to the logged in user's cart """
    return render(request, 'cart.html')

def update_cart(request, id):
    """ Updates contents of the user's cart """
    return render(request, 'cart.html')

