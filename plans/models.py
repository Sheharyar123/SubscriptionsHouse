import uuid
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse


class Plan(models.Model):
    PLAN_TYPE = (
        ("BASIC", "BASIC"),
        ("POPULAR", "POPULAR"),
        ("ENTERPRISE", "ENTERPRISE"),
    )
    BACKGROUND_TYPE = (
        ("primary", "primary"),
        ("secondry", "secondry"),
        ("danger", "danger"),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    background_type = models.CharField(choices=BACKGROUND_TYPE, max_length=30)
    plan_type = models.CharField(
        choices=PLAN_TYPE, max_length=30, null=True, blank=True
    )
    price = models.DecimalField(max_digits=8, decimal_places=0)
    title = models.CharField(max_length=255)
    valid_for = models.CharField(max_length=50)
    description = RichTextField()
    active = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_on", "added_on"]

    def __str__(self):
        if self.plan_type:
            return f"{self.plan_type} - {self.title}"
        else:
            return self.title

    def get_absolute_url(self):
        return reverse("plans:plan_detail", kwargs={"pk": self.pk})
