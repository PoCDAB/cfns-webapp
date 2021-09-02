from django import forms

# Form at the profilepage to retrieve the Base64 code for external authentication for the API
class viewBase64AuthcodeForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
