from django import forms
from django.forms import ModelForm
from .models import MyModelName

class NameForm(ModelForm):
    class Meta:
        model= MyModelName
        fields = ["name","user_choice"]
