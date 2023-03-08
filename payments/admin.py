from django.contrib import admin
from .models import Payment

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ["transaction_id", "plan", "subscription", "amount", "status"]
    list_filter = ["status"]


admin.site.register(Payment, PaymentAdmin)
