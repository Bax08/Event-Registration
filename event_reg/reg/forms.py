from django import forms
from. models import Information

class InformationForm(forms.ModelForm):
    class meta:
        model = Information
        field = ['text']
        label={'text': ' '}

