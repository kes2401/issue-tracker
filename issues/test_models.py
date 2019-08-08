from django.test import TestCase, Client
from .models import Issue, IssueComment, IssueVote
from django.contrib.auth.models import User

class TestModels(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'testuser@gmail.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.test_bug = Issue(title='new bug', description='test bug description', author=self.user, issue_type='bug')
        self.test_bug.save()
        self.test_comment = IssueComment(issue=self.test_bug, user=self.user, comment='test comment')
        self.test_comment.save()
        self.test_vote = IssueVote(issue=self.test_bug, user=self.user)
        self.test_vote.save()
    
    def test_issue_str(self):
        issue = Issue.objects.get(title='new bug')
        self.assertEqual(str(issue), 'new bug')

    def test_issuecomment_str(self):
        comment = IssueComment.objects.get(comment='test comment')
        self.assertEqual(str(comment), 'test comment')
    
    def test_issuevote_str(self):
        vote = IssueVote.objects.get(pk=self.test_vote.id)
        self.assertEqual(str(vote), 'new bug')