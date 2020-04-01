from django import forms
from .models import *


class institute_photo_form(forms.ModelForm):
    class Meta:
        model=Images
        fields=['institute_photos']

class institute_result_form(forms.ModelForm):
    class Meta:
        model=institute_result
        fields=['institute_result']


class faculty_detail_form(forms.ModelForm):
    class Meta:
        model=faculty_detail
        fields=['faculty_image']

class institute_information_form(forms.ModelForm):
    class Meta:
        model=institute_information
        fields=['institute_logo']
