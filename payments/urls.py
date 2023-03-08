from django.urls import path
from .views import PaymentView

app_name = "payments"

urlpatterns = [
    path("payment/", PaymentView.as_view(), name="check_payment"),
]
