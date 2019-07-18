# Generated by Django 2.2.2 on 2019-07-17 20:00

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0008_auto_20190710_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='date_complete',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
