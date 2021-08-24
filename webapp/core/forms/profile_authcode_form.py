from django import forms

class viewBase64AuthcodeForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
