from django import forms
from django.forms import ModelForm
from .models import Visitor


class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'fp', 'components']
        widgets = {'fp': forms.HiddenInput(), 'components': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(VisitorForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your nick'})
        self.fields['fp'].widget.attrs.update({'class': 'form-control', 'id': 'fp', 'placeholder': 'Your fingerprint'})
        self.fields['components'].widget.attrs.update({'class': 'form-control', 'id': 'components'})
        self.fields['name'].label = 'Your nickname:'
        self.fields['fp'].label = 'Fingerprint:'