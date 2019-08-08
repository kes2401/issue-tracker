from django.test import TestCase, Client
from .views import tracker, create_bug, create_feature, bug_detail, feature_detail, add_comment, add_vote, remove_vote
from django.urls import reverse
from .models import Issue, IssueComment, IssueVote
from django.utils import timezone
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.test_bug = Issue(issue_type='bug', title='testbug1', description='testdescription1', author=self.user)
        self.test_bug.save()
        self.test_bug_comment = IssueComment(issue=self.test_bug, user=self.user, comment='test comment')
        self.test_bug_comment.save()
        self.test_bug_vote = IssueVote(issue=self.test_bug, user=self.user)
        self.test_bug_vote.save()
        self.test_feature = Issue(issue_type='feature', title='testfeature1', description='testdescription1', author=self.user)
        self.test_feature.save()
        self.test_feature_comment = IssueComment(issue=self.test_feature, user=self.user, comment='test comment')
        self.test_feature_comment.save()
        self.test_feature_vote = IssueVote(issue=self.test_feature, user=self.user)
        self.test_feature_vote.save()
        self.test_feature2 = Issue(issue_type='feature', title='testfeature2', description='testdescription2', author=self.user)
        self.test_feature2.save()

    def test_get_tracker_page(self):
        response = self.client.get(reverse('tracker'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracker.html')
    
    def test_post_tracker_page(self):
        response = self.client.post(reverse('tracker'), {'bug-search': 'test', 'bugStatus': 'pending', 'featureStatus': 'pending', 'bugSort': 'name-down', 'featureSort': 'name-down'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracker.html')

    def test_get_create_bug(self):
        response = self.client.get(reverse('create_bug'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_bug.html')

    def test_post_create_bug(self):
        response = self.client.post(reverse('create_bug'), {'title': 'test bug 2', 'description': 'test description'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tracker'))
        
    def test_get_create_feature(self):
        response = self.client.get(reverse('create_feature'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_feature.html')

    def test_get_bug_detail(self):
        response = self.client.get(reverse('bug_detail', kwargs={'id': self.test_bug.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'issue_detail.html')
    
    def test_get_feature_detail(self):
        response = self.client.get(reverse('feature_detail', kwargs={'id': self.test_feature.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'issue_detail.html')

    def test_post_add_comment(self):
        response = self.client.post(reverse(add_comment, kwargs={'id': self.test_feature2.id}), {'comment': 'test comment'})
        self.assertEqual(response.status_code, 200)

    def test_post_add_vote(self):
        response = self.client.post(reverse(add_vote, kwargs={'id': self.test_feature.id}))
        self.assertEqual(response.status_code, 200)

    def test_post_remove_vote(self):
        response = self.client.post(reverse(remove_vote, kwargs={'id': self.test_feature.id}))
        self.assertEqual(response.status_code, 200)
