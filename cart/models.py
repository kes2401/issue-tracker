from django.db import models
from django.contrib.auth.models import User
from issues.models import Issue
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CartContent(models.Model):

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

    user = models.ForeignKey(User, default='Anonymous', on_delete=models.CASCADE)
    product = models.ForeignKey(Issue, on_delete=models.CASCADE)
    amount = models.IntegerField(default=50, validators=[validate_gt_fifty, validate_lt_fifteenhundred])

    def __str__(self):
        return self.user