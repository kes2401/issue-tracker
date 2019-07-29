from django.db import models
from cart.models import Cart
from issues.models import Issue
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0} - {1} - {2}".format(self.id, self.user, self.date)

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete=models.DO_NOTHING)
    issue = models.ForeignKey(Issue, null=False, on_delete=models.DO_NOTHING)
    request_type = models.CharField(max_length=12, default='new request')
    amount_paid = models.IntegerField(default=0)
    
    def __str__(self):
        return "{0} - {1} - {2} - € {3}".format(self.request_type, self.order.user, self.issue.title, self.amount_paid)
