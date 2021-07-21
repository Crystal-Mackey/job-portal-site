from django import forms
from .models import User, CHOICES
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.CharField(max_length=100)
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    employee = forms.ChoiceField(label='Account Type', widget=forms.RadioSelect(), choices=CHOICES)


class EditProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = "name",  "bio", "experience", "skills", "contact_num"
