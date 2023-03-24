from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("subscriptions-house-admin/", admin.site.urls),
    path("", include("plans.urls")),
    path("subscribe/", include("subscriptions.urls")),
    path("payment/", include("payments.urls")),
]
