from django.urls import path
from .views import PaymentView, PaymentAcceptedView, PaymentCancelledView

app_name = "payments"

urlpatterns = [
    path("payment/", PaymentView.as_view(), name="check_payment"),
    path("payment_accepted/", PaymentAcceptedView.as_view(), name="payment_accepted"),
    path(
        "payment_cancelled/", PaymentCancelledView.as_view(), name="payment_cancelled"
    ),
]
