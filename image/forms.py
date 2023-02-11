from django import forms
from .models import Image

class Formss(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'Images':''}
