from django import forms

class SendDABForm(forms.Form):
    message = forms.CharField(label='DAB message', max_length=256)
    ship_id = forms.CharField(label='Schip identifier', max_length=256)
    messagetype = forms.IntegerField(label='Message Type')