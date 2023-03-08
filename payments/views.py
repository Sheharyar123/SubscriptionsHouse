from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from plans.models import Plan
from subscriptions.models import Subscription
from .models import Payment


class PaymentView(View):
    def post(self, request, *args, **kwargs):
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            try:
                subscription_id = request.session.get("subscription_id")
                plan_id = request.POST.get("plan_id")
                plan = Plan.objects.get(id=plan_id, active=True)
                subscription = Subscription.objects.get(
                    id=subscription_id, subscribed=False
                )
                transaction_id = request.POST.get("transaction_id")
                status = request.POST.get("status")
                payment = Payment()
                payment.plan = plan
                payment.subscription = subscription
                payment.transaction_id = transaction_id
                payment.status = status
                payment.amount = plan.price
                payment.save()
                del request.session["subscription_id"]
                return JsonResponse(
                    {
                        "status": "success",
                        "subscription_id": subscription_id,
                        "plan_id": plan_id,
                    }
                )
            except:
                return redirect("subscriptions:subscription_form", id=plan_id)
