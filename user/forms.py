from django import forms
from user.models import User, Listing
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'bio', 'email', 'role']


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"


class JobForm(forms.ModelForm):
    listing = forms.CharField(widget=forms.Textarea, max_length=140) #max length dictated by rubric

    class Meta:
        model = Listing
        fields = "__all__"
        # exclude = ['time', 'user']