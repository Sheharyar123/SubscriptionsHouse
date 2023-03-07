from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, ListView
from accounts.utils import send_email
from .forms import ContactForm
from .models import Plan


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        plan_list = Plan.objects.filter(active=True)[:6]
        context = {"plan_list": plan_list, "form": ContactForm}
        return render(request, "plans/index.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            context = {
                "subject": form.cleaned_data["subject"],
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "phone_no": form.cleaned_data["phone_no"],
            }
            mail_subject = f"You have received a new email from {context['name']}"
            mail_template = "plans/emails/contact_form_message.html"
            send_email(mail_subject, mail_template, context)
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "failed"})


class PlanListView(ListView):
    model = Plan
    template_name = "plans/plan_list.html"
    context_object_name = "plan_list"
    paginate_by = 6

    def get_queryset(self):
        plan_list = Plan.objects.filter(active=True)
        return plan_list
