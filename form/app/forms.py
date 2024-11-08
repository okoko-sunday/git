from django import forms
from django.forms import formset_factory


class FamilyForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    
myform = formset_factory(FamilyForm, extra=5)