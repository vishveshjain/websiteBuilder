from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    phone = forms.CharField(max_length=12, required=False)
    sender = forms.EmailField()