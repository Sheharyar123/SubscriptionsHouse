from django.contrib import admin
from .models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "background_type",
        "price",
        "valid_for",
        "active",
    ]
    list_editable = [
        "active",
        "valid_for",
    ]
    list_filter = [
        "price",
    ]
    search_fields = ["title", "price"]
