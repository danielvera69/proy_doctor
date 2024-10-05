from django import forms

from aplication.core.models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        #        inputtext               select
        fields=['first_name','last_name','profession','clinic','sex','birth_date','address','is_active']
             