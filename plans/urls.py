from django.urls import path
from .views import HomePageView, PlanListView

app_name = "plans"

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("plans/", PlanListView.as_view(), name="plan_list"),
]
