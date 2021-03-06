from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Issue(models.Model):
    ISSUE_CHOICES = [
        ('bug', 'Bug'),
        ('feature', 'Feature')
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in progress', 'In Progress'),
        ('closed', 'Closed')
    ]
    issue_type = models.CharField(max_length=7, choices=ISSUE_CHOICES)
    title = models.CharField(max_length=40)
    description = HTMLField('Description')
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=11, choices=STATUS_CHOICES, default='pending')
    total_paid = models.IntegerField(default=0)
    date_complete = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class IssueComment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=624)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class IssueVote(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.issue.title
