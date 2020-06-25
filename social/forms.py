from django import forms
from django.contrib.auth.models import User
from django.forms import SelectDateWidget

from social.models import MyProfile, Feedback, JobPost


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
            "name", "gender","ptype", "pic","age","phone_no","address","course", "branch","YOP", "YOJ","highper","interper","grduper",
            "status","YOE", "description","myresume")


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ("feed_name", "feed_email", "feed_phone_no", "feedback", "suggetion")


class EmailForm(forms.Form):
    name = forms.CharField(required=True)
    to_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class JobForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ('company_name', 'eligibility', 'job_role', 'experience', 'job_requirements',
                  'job_description', 'job_specification', 'work_location',
                  'salary', 'how_to_apply', 'last_date')
        widgets = {
            'last_date': SelectDateWidget(attrs={'style': 'display: inline-block; width: 33%;'})
        }