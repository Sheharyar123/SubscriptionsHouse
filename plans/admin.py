from django.contrib import admin
from .models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "plan_type",
        "background_type",
        "price",
        "valid_for",
        "active",
    ]
    list_editable = [
        "active",
        "valid_for",
    ]
    list_filter = ["plan_type", "price"]
    search_fields = ["plan_type", "title", "price"]
