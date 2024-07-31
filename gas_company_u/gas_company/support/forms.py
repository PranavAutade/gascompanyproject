from django import forms
from .models import SupportRequest

class RequestForm(forms.ModelForm):
    class Meta:
        model = SupportRequest
        fields = ['subject', 'message']

class AssignRepForm(forms.ModelForm):
    class Meta:
        model = SupportRequest
        fields = ['assigned_rep']
        widgets = {
            'assigned_rep': forms.Select(attrs={'class': 'form-control'}),
        }
