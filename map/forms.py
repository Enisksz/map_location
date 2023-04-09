from django import forms
from .models import SearchModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SearchModelForm(forms.ModelForm):
    address = forms.CharField(label='')
    class Meta:
        model = SearchModel
        fields = ('address',)
