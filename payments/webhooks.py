import stripe
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.utils import send_confirmation_email
from subscriptions.models import Subscription
from .models import Payment


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event.type == "checkout.session.completed":
        session = event.data.object
        if session.mode == "payment" and session.payment_status == "paid":
            try:
                subscription = Subscription.objects.get(
                    id=session.client_reference_id, subscribed=False
                )
                subscription.subscribed = True
                subscription.valid_from = timezone.now()
                subscription.valid_till = timezone.now() + timedelta(
                    subscription.get_days
                )
                subscription.save()
                payment = Payment()
                payment.subscription = subscription
                payment.plan = subscription.plan
                payment.transaction_id = session.id
                payment.status = session.payment_status
                payment.amount = subscription.plan.price
                payment.save()
                del request.session["subscription_id"]
                context = {
                    "subscription": subscription,
                    "plan": subscription.plan,
                    "email": subscription.email,
                }
                mail_subject = "Thanks for subscribing"
                mail_template = "plans/emails/confirm_subscription.html"
                send_confirmation_email(mail_subject, mail_template, context)
            except Subscription.DoesNotExist:
                return HttpResponse(status=404)
    return HttpResponse(status=200)
