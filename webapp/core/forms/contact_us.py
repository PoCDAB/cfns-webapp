from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    email = forms.EmailField(label="E-mail", required=True)
    intrested = forms.ChoiceField(label="Interested to get involved?", required=True)
    message = forms.CharField(label="Message", required=True)
    attachments   = forms.ImageField(label="Attachments")
    newsletter = forms.BooleanField(label="Subscribe to newsletter")
