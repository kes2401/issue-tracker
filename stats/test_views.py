from django.test import TestCase, Client
from .views import stats, top_bugs, top_features, bug_closure, feature_closure
from django.urls import reverse
from cart.models import Cart
from django.contrib.auth.models import User
from issues.models import Issue
from django.utils import timezone


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.open_bug = Issue(issue_type='bug', title='testbug1', description='testdescription1', author=self.user)
        self.open_bug.save()
        self.open_feature = Issue(issue_type='feature', title='testfeature1', description='testdescription1', author=self.user)
        self.open_feature.save()
        self.closed_bug = Issue(issue_type='bug', title='testbug2', description='testdescription2', author=self.user, status='closed')
        self.closed_bug.save()
        self.closed_bug.date_complete = timezone.now()
        self.closed_bug.save()
        self.closed_feature = Issue(issue_type='feature', title='testfeature2', description='testdescription2', author=self.user, status='closed')
        self.closed_feature.save()
        self.closed_feature.date_complete = timezone.now()
        self.closed_feature.save()

    def test_get_stats_page(self):
        cart_item = Cart(title='new suggested feature', description='will make the app better', user=self.user, request_type='new feature', amount=50)
        cart_item.save()
        response = self.client.get(reverse(stats))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stats.html')

    def test_top_bugs(self):
        response = self.client.get(reverse(top_bugs))
        self.assertEqual(response.status_code, 200)
    
    def test_top_features(self):
        response = self.client.get(reverse(top_features))
        self.assertEqual(response.status_code, 200)

    def test_bug_closure(self):
        response = self.client.get(reverse(bug_closure))
        self.assertEqual(response.status_code, 200)
    
    def test_feature_closure(self):
        response = self.client.get(reverse(feature_closure))
        self.assertEqual(response.status_code, 200)
