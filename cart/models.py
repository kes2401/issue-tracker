from django.db import models
from django.contrib.auth.models import User
from issues.models import Issue
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class CartContent(models.Model):

    def validate_gt_fifty(value):
        if value < 50:
            raise ValidationError(
                _('%(value)s is not greater than 50.00'),
                params={'value': value},
            )

    user = models.ForeignKey(User, default='Anonymous', on_delete=models.CASCADE)
    product = models.ForeignKey(Issue, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2, default=50.00, validators=[validate_gt_fifty])

    def __str__(self):
        return self.user