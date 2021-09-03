from django import forms
from .models import Visitor

class MainForm(forms.ModelForm):
  class Meta:
    model = Visitor
    fields = ['visitor_name', 'role', 'email', 'planned_checkout', 'nightstay']

    widgets = {
      'visitor_name': forms.TextInput(attrs={'class':'form-control'}),
      'role': forms.TextInput(attrs={'class':'form-control'}),
      'email': forms.EmailInput(attrs={'class':'form-control'}),
      'nightstay': forms.CheckboxInput(attrs={'class':'form-check-input'}),
      'planned_checkout': forms.DateTimeInput(attrs={'class':'form-control'})
    }