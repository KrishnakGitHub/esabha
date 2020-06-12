from django import forms
from django.contrib.auth.models import User

from social.models import MyProfile


# User update form allows users to update user name and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = MyProfile
        fields = ("name", "age", "address", "status", "gender", "phone_no", "description", "pic")
