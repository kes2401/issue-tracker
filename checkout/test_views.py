from django.test import TestCase, Client
from .views import checkout
from django.urls import reverse
from django.contrib.auth.models import User
from cart.models import Cart
from .models import Order, OrderLineItem
from issues.models import Issue, IssueVote
from django.conf import settings
import stripe


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
        cart_item1 = Cart(title='new item', description='this is a new item', user=self.user, request_type='new feature')
        cart_item1.save()

        stripe.api_key = settings.STRIPE_SECRET

    def test_get_checkout_page(self): 
        response = self.client.get(reverse('checkout'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')

    def test_post_checkout_page(self): 
        response = self.client.post(reverse('checkout'), {'full_name': 'John Doe', 'street_address1': '1 test address', 'street_address2': 'test address', 'phone_number': '123456789', 'town_or_city': 'test town', 'postcode': '00000', 'country': 'ireland', 'credit_card_no': '4242424242424242', 'cvv': '123', 'expiry_month': '01', 'expiry_year': '2021', 'stripe_id': 'card_1F4uRuFI3R6rxPhVqkTq60CR'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')