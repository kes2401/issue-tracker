from django.test import TestCase, Client
from .views import view_cart, update_cart, add_to_cart, add_vote_to_cart, remove_from_cart
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import Cart_New_feature
from .models import Cart
from issues.models import Issue
from issues.views import create_feature


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_get_cart_page(self):
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
    
    def test_post_add_to_cart_valid_form(self):
        response = self.client.post(reverse('add_to_cart'), {'title': 'new feature 1', 'description': 'this will be great'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('view_cart'))

    # def test_post_add_to_cart_invalid_form(self):
    #     response = self.client.post(reverse('add_to_cart'), {})
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, reverse('create_feature'))

    def test_get_add_vote_to_cart(self):
        feature = Issue(issue_type='feature', title='new feature 1', description='this will be great', author=self.user,)
        feature.save()
        response = self.client.get(reverse('add_vote_to_cart', args=[feature.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('view_cart'))

    def test_post_to_update_cart(self):
        item = Cart(title='new feature 1', description='this will be great', user=self.user, request_type='new feature')
        item.save()
        response = self.client.post(reverse('update_cart'), {'amount_to_pay': 75, 'key': item.id})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('view_cart'))
        
    def test_get_remove_from_cart(self):
        item = Cart(title='new feature 1', description='this will be great', user=self.user, request_type='new feature')
        item.save()
        response = self.client.get(reverse('remove_from_cart', args=[item.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('view_cart'))