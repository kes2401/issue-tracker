from django.db import models
from django.contrib.auth.models import User
from issues.models import Issue
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

class Cart(models.Model):

    def validate_gt_fifty(value):
        if value < 50:
            raise ValidationError(
                _('%(value)s is not greater than 50'),
                params={'value': value},
            )

    def validate_lt_fifteenhundred(value):
        if value > 1500:
            raise ValidationError(
                _('%(value)s cannot be greater than 1500'),
                params={'value': value},
            )
    
    TYPE_CHOICES = [
        ('new feature', 'New Feature'),
        ('feature vote', 'Feature Vote')
    ]

    title = models.CharField(max_length=40)
    description = HTMLField('Description')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=12, choices=TYPE_CHOICES)
    amount = models.IntegerField(default=50, validators=[validate_gt_fifty, validate_lt_fifteenhundred])
    

    def __str__(self):
        return self.title

    