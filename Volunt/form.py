from django import forms
from .models import Volunteers
class Vols(forms.ModelForm):
    class Meta:
        model = Volunteers
        fields=['name','age','birthdate','email','city','study']
        labels={
            'name':'الاسم',
             'age':'العمر',
           'birthdate':'تاريخ الميلاد',
             'email':'البريد الالكتروني',
            'city':'المدينة',
            'study':'يدرس',
        }