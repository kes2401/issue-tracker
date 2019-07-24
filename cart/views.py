from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Cart
from .forms import Cart_New_feature
from django.http import HttpResponse

def view_cart(request):
    """ Renders the cart with all products selected by the logged in user """
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

def add_to_cart(request):
    """ Adds an item to the logged in user's cart """
    if request.method == 'POST':
        form = Cart_New_feature(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.title = request.POST['title']
            instance.description = request.POST['description']
            instance.request_type = 'new feature'
            instance.save()
            messages.success(request, 'You have added a new item to your cart.')
        else:
            messages.error(request, 'Something went wrong. Please try again.')
            return redirect('create_feature.html')
    
    return redirect(reverse('view_cart'))

def update_cart(request):
    """ Updates contents of the user's cart """
    if request.method == 'POST':
        updated_amount = request.POST['amount_to_pay']
        item_pk = request.POST['key']
        Cart.objects.filter(pk=item_pk).update(amount=updated_amount)     
    return redirect(reverse('view_cart'))

def remove_from_cart(request, id):
    """ Remove an item from the user's cart """
    cart_items = Cart.objects.filter(pk=id).delete()
    return redirect(reverse('view_cart'))