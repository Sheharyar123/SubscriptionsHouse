from django.contrib import admin
from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [
        "plan",
        "first_name",
        "last_name",
        "phone_no",
        "valid_from",
        "valid_till",
        "subscribed",
    ]
    list_display_links = ["plan"]


admin.site.register(Subscription, SubscriptionAdmin)
