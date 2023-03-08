import uuid
from django_countries.fields import CountryField
from django.db import models
from plans.models import Plan


class Subscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plan = models.ForeignKey(
        Plan, on_delete=models.SET_NULL, null=True, related_name="subscriptions"
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    country = CountryField(blank_label="(Select country)")
    valid_from = models.DateTimeField(null=True, blank=True)
    valid_till = models.DateTimeField(null=True, blank=True)
    subscribed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.plan.title}'s Subscription"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
