from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

from mFarm.models import Farmer, Sacco


class FarmerCreationForm(UserCreationForm):
    email = forms.EmailField()
    phone = PhoneNumberField()
    name = forms.CharField()
    address = forms.CharField()
    sacco = forms.ModelChoiceField(queryset=Sacco.objects.all(), required=True)

    class Meta:
        model = Farmer
        fields = ("email", "phone", "name", "address", "password1", "password2", "sacco")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone = self.cleaned_data["phone"]
        user.name = self.cleaned_data["name"]
        user.address = self.cleaned_data["address"]
        user.sacco = self.cleaned_data.get("sacco")
        if commit:
            user.save()
        return user
