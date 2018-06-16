from django import forms
from django.contrib.auth.models import User
from getall.models import Profile
from django.utils.translation import ugettext_lazy as _


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['surname', 'idno', 'phoneNo']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['FirstName','LastName','surname', 'email', 'phoneNo', 'idno']