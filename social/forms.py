from django import forms
from django.contrib.auth.models import User

from social.models import MyProfile, Feedback


# User update form allows users to update user name and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = MyProfile
        fields = (
            "name", "age", "address", "status", "gender", "phone_no", "description", "pic", "YOE", "YOP", "YOJ",
            "ptype",
            "course", "branch", "grduper", "interper", "highper", "myresume")


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ("feed_name", "feed_email", "feed_phone_no", "feedback", "suggetion")


class EmailForm(forms.Form):
    name = forms.CharField(required=True)
    to_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
