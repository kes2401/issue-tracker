# Generated by Django 2.2.2 on 2019-07-04 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_auto_20190704_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuecomment',
            old_name='issue_id',
            new_name='issue',
        ),
        migrations.RenameField(
            model_name='issuecomment',
            old_name='user_id',
            new_name='user',
        ),
    ]
