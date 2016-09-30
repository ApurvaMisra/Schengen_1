from django import forms

class DateForm(forms.Form):
    start_date = forms.DateField(label='Start date',input_formats= ['%m/%d/%Y'],help_text='%m/%d/%Y')
    stop_date = forms.DateField(label='Stop date',input_formats= ['%m/%d/%Y'],help_text='%m/%d/%Y')
    country=forms.CharField(label='Country code')