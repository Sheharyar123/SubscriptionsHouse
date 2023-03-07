from django.shortcuts import render
from django.views.generic import View, ListView

from .models import Plan


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        plan_list = Plan.objects.filter(active=True)[:6]
        context = {"plan_list": plan_list}
        return render(request, "plans/index.html", context)

    # def post(self, request, *args, **kwargs):
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         subject = form.cleaned_data["subject"]
    #         name = form.cleaned_data["name"]
    #         email_from = form.cleaned_data["email"]
    #         phone_no = form.cleaned_data["phone_no"]
    #         message = f'{form.cleaned_data["comment"]}.\n\nSent by {name}.\nPhone No is {phone_no}.\nEmail is {email_from}'
    #         receipient_list = [
    #             settings.EMAIL_HOST_USER,
    #         ]
    #         send_mail(
    #             subject,
    #             message,
    #             email_from,
    #             receipient_list,
    #             fail_silently=False,
    #         )
    #         messages.success(request, "Your message was sent successfully")
    #         return redirect("products:index")


class PlanListView(ListView):
    model = Plan
    template_name = "plans/plan_list.html"
    context_object_name = "plan_list"
    paginate_by = 6

    def get_queryset(self):
        plan_list = Plan.objects.filter(active=True)
        return plan_list
