from django import forms
from tinymce.widgets import TinyMCE
from .models import Issue

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class CreateIssue(forms.ModelForm):

    description = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 36, 'rows': 10}))

    class Meta:
        model = Issue
        fields = ['title', 'description']
