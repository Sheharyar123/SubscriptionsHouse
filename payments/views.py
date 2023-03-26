import stripe
from decimal import Decimal
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View
from subscriptions.models import Subscription

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


class PaymentView(View):
    def post(self, request, *args, **kwargs):
        try:
            success_url = request.build_absolute_uri(
                reverse("payments:payment_completed")
            )
            cancel_url = request.build_absolute_uri(
                reverse("payments:payment_canceled")
            )
            subscription_id = request.session.get("subscription_id")
            subscription = Subscription.objects.get(
                id=subscription_id, subscribed=False
            )
            del request.session["subscription_id"]
            session_data = {
                "mode": "payment",
                "client_reference_id": subscription_id,
                "success_url": success_url,
                "cancel_url": cancel_url,
                "line_items": [],
                "customer_email_collection": False,
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


class PaymentCompletedView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "payments/payment_completed.html")


class PaymentCanceledView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "payments/payment_canceled.html")
