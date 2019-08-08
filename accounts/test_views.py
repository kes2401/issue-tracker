from django.test import TestCase, Client
from .views import login, logout, register, profile
from issue_tracker.views import index
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_get_login_page(self):
        page = self.client.get(reverse('login'))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'login.html')

    def test_get_login_page_redirecct_when_user_logged_in(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.client.logout()
    
    def test_post_login_page_with_correct_credentials(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpassword')
        response = self.client.post(reverse('login'), {'username':'testuser', 'password':'testpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('profile'))
        self.client.logout()
    
    def test_post_login_page_with_incorrect_credentials(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpassword')
        response = self.client.post(reverse('login'), {'username':'testusers', 'password':'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_get_register_page(self):
        page = self.client.get(reverse('register'))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register.html')

    def test_get_register_page_redirect_when_user_already_logged_in(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.client.logout()

    def test_post_register_page_with_valid_details(self):
        self.client = Client()
        response = self.client.post(reverse('register'), {'username':'testuser', 'email':'testuser@gmail.com', 'password1':'testpassword', 'password2':'testpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.client.logout()

    def test_post_register_page_with_invalid_details(self):
        self.client = Client()
        response = self.client.post(reverse('register'), {'username':'testuser', 'email':'testuser@gmail.com', 'password1':'testpassword', 'password2':'testpassword123'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_get_profile_page_no_user_logged_in_redirect(self):
        page = self.client.get(reverse('profile'))
        self.assertEqual(page.status_code, 302)
        self.assertRedirects(page, '/accounts/login/?next=/accounts/profile/')

    def test_get_profile_page_when_user_logged_in(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.client.logout()

    def test_get_logout_page(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.client.logout()