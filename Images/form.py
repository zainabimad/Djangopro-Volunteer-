from .models import Uploaded
from django import forms
class Fileform(forms.ModelForm):
    class Meta:
        model=Uploaded
        fields='__all__'

