from django.urls import path
from .views import HomePageView, PlanListView, PlanDetailView

app_name = "plans"

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("plans/", PlanListView.as_view(), name="plan_list"),
    path("plan/<uuid:pk>/", PlanDetailView.as_view(), name="plan_detail"),
]
