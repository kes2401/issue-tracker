# Generated by Django 2.2.2 on 2019-07-06 12:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues', '0004_auto_20190704_2111'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IssueVotes',
            new_name='IssueVote',
        ),
    ]