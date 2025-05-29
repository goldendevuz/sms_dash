# forms.py
from django import forms

class SendMessageForm(forms.Form):
    api_token = forms.CharField(max_length=255, label="API Token")
    phone_number = forms.CharField(max_length=20, label="Phone Number")
    message = forms.CharField(widget=forms.Textarea, label="Message")
