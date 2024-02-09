from .models import Chatbot, Inputoutput
from django import forms
from django.forms import ValidationError
from django.forms.widgets import ClearableFileInput

class ChatbotForm(forms.Form):
    msg = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}), required=False)

class InputOutputForm(forms.Form):
    msg1 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    msg2 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    msg3 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    msg4 = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)