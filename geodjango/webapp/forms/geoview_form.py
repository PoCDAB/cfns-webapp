from django import forms

class GeoviewForm(forms.Form):
    AIS = forms.BooleanField(required=False)
    LoRa = forms.BooleanField(required=False)
