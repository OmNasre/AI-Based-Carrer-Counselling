# forms.py
from django import forms
from .models import UserResponse

class AptitudeTestForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ['question', 'selected_option']
