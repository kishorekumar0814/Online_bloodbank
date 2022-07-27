from django import forms
from .models import *


class blooddataform(forms.ModelForm):
    blood_group = forms.CharField(required=True)
    name = forms.CharField(required=True)
    age = forms.CharField(required=True)
    ph_no = forms.CharField(required=True)
    place = forms.CharField(required=True)

    class Meta:
        model = blooddata
        fields = ('blood_group', 'name', 'age', 'ph_no', 'place')