from datetime import timedelta
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import View
from accounts.utils import send_email
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
                subscription.subscribed = True
                subscription.valid_from = timezone.now()
                subscription.valid_till = timezone.now() + timedelta(
                    subscription.get_days
                )
                subscription.save()
                del request.session["subscription_id"]
                context = {
                    "subscription": subscription,
                    "plan": plan,
                    "email": subscription.email,
                }
                mail_subject = "Thanks for subscribing"
                mail_template = "plans/emails/confirm_subscription.html"
                send_email(mail_subject, mail_template, context)
                return JsonResponse({"status": "success"})
            except:
                return JsonResponse({"status": "failed"})
        else:
            return redirect("plans:index")
