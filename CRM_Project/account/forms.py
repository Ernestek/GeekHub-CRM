from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserCreateForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=False,
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = User
        fields = ('email',)
