from django.db import models
from django.contrib.auth.models import User


class Issue(models.Model):
    ISSUE_CHOICES = [
        ('bug', 'Bug'),
        ('feature', 'Feature')
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in progress', 'In Progress'),
        ('done', 'Done')
    ]
    issue_type = models.CharField(max_length=7, choices=ISSUE_CHOICES)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=1248)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, default='Anonymous', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=11, choices=STATUS_CHOICES, default='pending')
    amount_paid = models.DecimalField(
        max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title


class IssueComment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=624)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class IssueVotes(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.issue
