from django.test import TestCase, Client
from .models import Cart
from django.contrib.auth.models import User


class TestCartModel(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
        item = Cart(title='new suggested feature', description='will make the app better', user=self.user, request_type='new feature', amount=50)
        item.save()

    def test_item_in_db(self):
        obj = Cart.objects.get(title='new suggested feature')
        self.assertEqual(str(obj), 'new suggested feature')

    def test_str(self):
        obj = Cart.objects.get(title='new suggested feature')
        self.assertEqual(str(obj), 'new suggested feature')