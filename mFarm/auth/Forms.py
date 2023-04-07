from django.forms import ModelForm

from mFarm.models import Farmer


class LoginForm(ModelForm):
    class Meta:
        model = Farmer
        fields = '__all__'
