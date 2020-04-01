from django import forms
from .models import *


class user_profile_form(forms.ModelForm):
    class Meta:
        model=user_profile_details
        fields=['user_profile']
