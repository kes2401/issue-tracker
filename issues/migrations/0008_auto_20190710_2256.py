# Generated by Django 2.2.2 on 2019-07-10 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0007_auto_20190710_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in progress', 'In Progress'), ('closed', 'Closed')], default='pending', max_length=11),
        ),
    ]