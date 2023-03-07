from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def send_email(mail_subject, mail_template, context):
    to_email = settings.EMAIL_HOST_USER
    from_email = context.get("email")
    message = render_to_string(mail_template, context)
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.send()
