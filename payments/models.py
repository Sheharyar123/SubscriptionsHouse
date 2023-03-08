import uuid
from django.db import models
from plans.models import Plan
from subscriptions.models import Subscription


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plan = models.ForeignKey(
        Plan, on_delete=models.SET_NULL, null=True, related_name="payments"
    )
    subscription = models.OneToOneField(
        Subscription, on_delete=models.SET_NULL, null=True
    )
    transaction_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Payment from {self.subscription.name}"
