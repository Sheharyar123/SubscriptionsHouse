from django.urls import path
from .views import HomePageView

app_name = "plans"

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
]
