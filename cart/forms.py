from django import forms
from tinymce.widgets import TinyMCE
from .models import Cart

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class Cart_New_feature(forms.ModelForm):

    description = forms.CharField(widget=TinyMCEWidget(attrs={'required': False, 'cols': 36, 'rows': 10}))

    class Meta:
        model = Cart
        fields = ['title', 'description']