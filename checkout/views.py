from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import MakePaymentForm, OrderForm
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from cart.models import Cart
from .models import Order, OrderLineItem
from issues.models import Issue
import stripe


stripe.api_key = settings.STRIPE_SECRET

@login_required
def checkout(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            cart_items = Cart.objects.filter(user=request.user)
            payment_total = 0
            for item in cart_items:
                payment_total += item.amount

            try: 
                customer = stripe.Charge.create(
                    amount = int(payment_total * 100),
                    currency = 'EUR',
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, 'Your card was declined.')
            
            if customer.paid:
                messages.success(request, 'You have successfully paid.')

                order_instance = order_form.save(commit=False)
                order_instance.date = timezone.now()
                order_instance.user = request.user
                order_instance.save()
                
                for item in cart_items:
                    if item.request_type == 'new feature':
                        new_feature = Issue(
                            issue_type = 'feature',
                            title = item.title,
                            description = item.description,
                            date_created = timezone.now(),
                            author = request.user,
                            total_paid = item.amount
                        )
                        new_feature.save()

                        order_line_item = OrderLineItem(
                            order = order_instance,
                            issue = new_feature,
                            request_type = item.request_type,
                            amount_paid = item.amount
                        )
                        order_line_item.save()

                    elif item.request_type == 'feature vote':
                        # --- UPDATE THE ITEM ALREADY IN THE ISSUE TABLE ----
                        # this_item = 
                        print('This is a feature upvote.')

                Cart.objects.filter(user=request.user).delete()

                return redirect(reverse('tracker'))
            else:
                message.error(request, 'Unable to take payment.')
        
        else:
            messages.error(request, 'We were unable to take a payment with that card.')
            cart = Cart.objects.all().filter(user=request.user)

    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        cart = Cart.objects.filter(user=request.user)
        cart_total = 0
        for item in cart:
            cart_total += item.amount
    
    return render(request, 'checkout.html', {
        'payment_form': payment_form,
        'order_form': order_form,
        'publishable': settings.STRIPE_PUBLISHABLE,
        'cart': cart,
        'cart_total': cart_total
        })