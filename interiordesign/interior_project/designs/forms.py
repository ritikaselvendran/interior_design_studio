from django import forms
from .models import Design

class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = ['title', 'description', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }