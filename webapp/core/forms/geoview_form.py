from django import forms

class GeoviewForm(forms.Form):
    AIS = forms.BooleanField(label="AIS", required=False)
    LoRaWAN = forms.BooleanField(label="LoRaWAN", required=False)
