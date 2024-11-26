from .models import personalinfo
from django import forms

class personalinfoForm(forms.ModelForm):
    class Meta:
        model=personalinfo
        fields='__all__'