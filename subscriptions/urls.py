from django.urls import path
from .views import SubscriptionFormView

app_name = "subscriptions"

urlpatterns = [
    path(
        "<uuid:pk>/subscribe/", SubscriptionFormView.as_view(), name="subscription_form"
    ),
]
