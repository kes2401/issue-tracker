from django import forms
from .models import Issue


class CreateIssue(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description']
