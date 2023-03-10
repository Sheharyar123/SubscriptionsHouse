from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from plans.models import Plan
from .forms import SubscriptionForm
from .models import Subscription


class SubscriptionFormView(View):
    def get(self, request, *args, **kwargs):
        plan = get_object_or_404(Plan, id=kwargs.get("pk"))
        subscription_id = request.session.get("subscription_id")
        if subscription_id is not None:
            subscription = get_object_or_404(
                Subscription, id=subscription_id, plan=plan
            )
            return redirect(subscription.plan.get_absolute_url())
        else:
            form = SubscriptionForm
            context = {"form": form, "plan": plan}
            return render(request, "subscriptions/subscription_form.html", context)

    def post(self, request, *args, **kwargs):
        plan = get_object_or_404(Plan, id=kwargs.get("pk"))
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.plan = plan
            subscription.save()
            request.session["subscription_id"] = str(subscription.id)
            return redirect(plan.get_absolute_url())
        else:
            context = {"form": form}
            return render(request, "subscriptions/subscription_form.html", context)
