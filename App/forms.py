from django import forms
from App.models import Prime,Article

class PrimeForm(forms.ModelForm):

    class meta():
        model = Prime
        fields = ('employer','article') 
