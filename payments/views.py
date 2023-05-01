from datetime import timedelta
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import View
from plans.models import Plan
from subscriptions.models import Subscription
from accounts.utils import send_confirmation_email
from .models import Payment

# import stripe
# from decimal import Decimal
# from django.conf import settings
# from django.shortcuts import redirect, render
# from django.urls import reverse

# stripe.api_key = settings.STRIPE_SECRET_KEY
# stripe.api_version = settings.STRIPE_API_VERSION


# class PaymentView(View):
#     def post(self, request, *args, **kwargs):
#         try:
#             success_url = request.build_absolute_uri(
#                 reverse("payments:payment_completed")
#             )
#             cancel_url = request.build_absolute_uri(
#                 reverse("payments:payment_canceled")
#             )
#             subscription_id = request.session.get("subscription_id")
#             subscription = Subscription.objects.get(
#                 id=subscription_id, subscribed=False
#             )
#             session_data = {
#                 "mode": "payment",
#                 "client_reference_id": subscription_id,
#                 "success_url": success_url,
#                 "cancel_url": cancel_url,
#                 "line_items": [],
#                 "customer_email": subscription.email,
#             }

#             session_data["line_items"].append(
#                 {
#                     "price_data": {
#                         "unit_amount": int(subscription.plan.price * Decimal("100")),
#                         "currency": "usd",
#                         "product_data": {"name": subscription.plan.title},
#                     },
#                     "quantity": 1,
#                 }
#             )

#             session = stripe.checkout.Session.create(**session_data)
#             return redirect(session.url, code=303)

#         except:
#             return redirect("plans:plan_list")


# class PaymentCompletedView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "payments/payment_completed.html")


# class PaymentCanceledView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, "payments/payment_canceled.html")


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
                subscription.subscribed = True
                subscription.valid_from = timezone.now()
                subscription.valid_till = timezone.now() + timedelta(
                    subscription.get_days
                )
                subscription.save()
                transaction_id = request.POST.get("transaction_id")
                status = request.POST.get("status")
                payment = Payment()
                payment.plan = plan
                payment.subscription = subscription
                payment.transaction_id = transaction_id
                payment.status = status
                payment.amount = plan.price
                payment.save()
                print(subscription)
                del request.session["subscription_id"]
                context = {
                    "subscription": subscription,
                    "plan": plan,
                    "email": subscription.email,
                }
                mail_subject = "Thanks for subscribing"
                mail_template = "plans/emails/confirm_subscription.html"
                send_confirmation_email(mail_subject, mail_template, context)
                return JsonResponse({"status": "success"})
            except:
                return JsonResponse({"status": "failed"})
        else:
            return redirect("plans:index")
