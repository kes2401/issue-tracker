from django.contrib import admin
from .models import Issue, IssueComment, IssueVotes

# Register your models here.

admin.site.register(Issue)
admin.site.register(IssueComment)
admin.site.register(IssueVotes)
