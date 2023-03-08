from django_countries.widgets import CountrySelectWidget
from django import forms
from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ["first_name", "last_name", "email", "phone_no", "country"]
        widgets = {"country": CountrySelectWidget()}

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget = forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control mb-4",
                "placeholder": "Enter your first name...",
            }
        )
        self.fields["last_name"].widget = forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control mb-4",
                "placeholder": "Enter your last name...",
            }
        )
        self.fields["email"].widget = forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control mb-4",
                "placeholder": "Enter your email...",
            }
        )
        self.fields["phone_no"].widget = forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control mb-4",
                "placeholder": "Enter your phone no...",
            }
        )

        self.fields["country"].widget.attrs.update({"class": "form-control mb-4"})
