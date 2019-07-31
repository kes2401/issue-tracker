from django.shortcuts import render
from cart.models import Cart


def index(request):
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0     
    return render(request, 'index.html', {'cart_count': cart_count})
