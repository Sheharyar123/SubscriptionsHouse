from django.urls import path
from .views import PaymentView, PaymentCompletedView, PaymentCanceledView

app_name = "payments"

urlpatterns = [
    path("payment/", PaymentView.as_view(), name="check_payment"),
    path("payment/completed", PaymentCompletedView.as_view(), name="payment_completed"),
    path("payment/canceled", PaymentCanceledView.as_view(), name="payment_canceled"),
]
