from django import forms

# iterable for intrest of this project
list_interested =(
    ("1", "Yes"),
    ("2", "No"),
    ("3", "Maybe"),
)

# Define Contact form at the Contact page
class contactForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    email = forms.EmailField(label="E-mail", required=True)
    interested = forms.ChoiceField(label="Interested to get involved?", required=True, choices = list_interested)
    message = forms.CharField(label="Message", required=True)
    attachments   = forms.ImageField(label="Attachments", required=False)
    newsletter = forms.BooleanField(label="I want to receive the CFNS newsletter when available", required=False)
