from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User


class TestUserLoginForm(TestCase):
    def test_form_is_valid_when_username_and_password_entered(self):
        login_form = UserLoginForm({'username':'test', 'password':'test2019'})
        self.assertTrue(login_form.is_valid())

    def test_form_not_valid_when_only_username_or_password_entered(self):
        login_form1 = UserLoginForm({'username': 'testname'})
        login_form2 = UserLoginForm({'password': 'testpassword'})
        
        self.assertFalse(login_form1.is_valid())
        self.assertFalse(login_form2.is_valid())

class TestUserRegistrationForm(TestCase):
    def test_form_valid_when_all_fields_entered(self):
        reg_form1 = UserRegistrationForm({'email': 'testemail@gmail.com', 'username': 'testname', 'password1': 'test2019', 'password2': 'test2019'})
        
        self.assertTrue(reg_form1.is_valid())
    
    def test_form_invalid_when_any_field_except_email_is_omitted(self):
        reg_form1 = UserRegistrationForm({'email': 'testemail@gmail.com', 'password1': 'test2019', 'password2': 'test2019'})
        reg_form2 = UserRegistrationForm({'email': 'testemail@gmail.com', 'username': 'testname', 'password2': 'test2019'})
        reg_form3 = UserRegistrationForm({'email': 'testemail@gmail.com', 'username': 'testname', 'password1': 'test2019'})

        self.assertFalse(reg_form1.is_valid())
        self.assertFalse(reg_form2.is_valid())
        self.assertFalse(reg_form3.is_valid())

    def test_confirm_email_is_unique(self):
        User.objects.create(username='testuser', email='testemail@gmail.com', password='test2019')
        reg_form = UserRegistrationForm({'username': 'testuser','email': 'testemail@gmail.com', 'password1': 'test2019', 'password2': 'test2019'})

        self.assertEqual(reg_form.errors['email'], [u'Email address must be unique'])

    def test_passwords_must_match(self):
        reg_form = UserRegistrationForm({'username': 'testuser','email': 'testemail@gmail.com', 'password1': 'test2019', 'password2': 'test2020'})

        self.assertEqual(reg_form.errors['password2'], [u'The two password fields didn\'t match.'])

    def test_password2_field_must_not_be_blank(self):
        reg_form = UserRegistrationForm({'username': 'testuser','email': 'testemail@gmail.com', 'password1': 'test2019', 'password2': ''})

        self.assertEqual(reg_form.errors['password2'], [u'This field is required.'])
        