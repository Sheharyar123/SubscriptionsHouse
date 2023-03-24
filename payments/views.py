import stripe
from decimal import Decimal
from datetime import timedelta
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import View
from accounts.utils import send_confirmation_email
from plans.models import Plan
from subscriptions.models import Subscription
from .models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


class PaymentView(View):
    def post(self, request, *args, **kwargs):
        # if request.headers.get("x-requested-with") == "XMLHttpRequest":
        try:
            success_url = request.build_absolute_uri(
                reverse("payments:payment_completed")
            )
            cancel_url = request.build_absolute_uri(
                reverse("payments:payment_canceled")
            )
            subscription_id = request.session.get("subscription_id")
            # plan_id = request.POST.get("plan_id")
            # plan = Plan.objects.get(id=plan_id, active=True)
            subscription = Subscription.objects.get(
                id=subscription_id, subscribed=False
            )
            # transaction_id = request.POST.get("transaction_id")
            # status = request.POST.get("status")
            # payment = Payment()
            # payment.plan = plan
            # payment.subscription = subscription
            # payment.transaction_id = transaction_id
            # payment.status = status
            # payment.amount = plan.price
            # payment.save()
            # subscription.subscribed = True
            # subscription.valid_from = timezone.now()
            # subscription.valid_till = timezone.now() + timedelta(subscription.get_days)
            # subscription.save()
            # del request.session["subscription_id"]
            # context = {
            #     "subscription": subscription,
            #     "plan": plan,
            #     "email": subscription.email,
            # }
            # mail_subject = "Thanks for subscribing"
            # mail_template = "plans/emails/confirm_subscription.html"
            # send_confirmation_email(mail_subject, mail_template, context)
            # return JsonResponse({"status": "success"})
            session_data = {
                "mode": "payment",
                "client_reference_id": subscription_id,
                "success_url": success_url,
                "cancel_url": cancel_url,
                "line_items": [],
            }

            session_data["line_items"].append(
                {
                    "price_data": {
                        "unit_amount": int(subscription.plan.price * Decimal("100")),
                        "currency": "usd",
                        "product_data": {"name": subscription.plan.title},
                    },
                    "quantity": 1,
                }
            )

            session = stripe.checkout.Session.create(**session_data)
            return redirect(session.url, code=303)

        except:
            return redirect("plans:plan_list")

    # else:
    #     return redirect("plans:index")


class PaymentCompletedView(View):
    def get(self, request, *args, **kwargs):
        pass


class PaymentCanceledView(View):
    def get(self, request, *args, **kwargs):
        pass
