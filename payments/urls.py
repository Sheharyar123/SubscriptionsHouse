from django.urls import path
from .views import PaymentView

app_name = "payments"

urlpatterns = [
    path("", PaymentView.as_view(), name="check_payment"),
    # path("completed", PaymentCompletedView.as_view(), name="payment_completed"),
    # path("canceled", PaymentCanceledView.as_view(), name="payment_canceled"),
    # path("webhook/", stripe_webhook, name="stripe-webhook"),
]
