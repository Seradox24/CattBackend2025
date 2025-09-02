from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=Profile.Roles.choices)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "role")
