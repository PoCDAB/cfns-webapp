from django import forms
from datetime import datetime    

class GeoviewForm(forms.Form):
    DAB = forms.BooleanField(label="DAB+ (done, but connection with hardware missing)", required=False)
    AIS = forms.BooleanField(label="AIS", required=False, initial=True)
    LoRaWAN = forms.BooleanField(label="LoRaWAN (work-in-progress)", required=False, initial=True)
    LTE = forms.BooleanField(label="2G+ (coming soon)", required=False)

    date_from = forms.DateTimeField(
        label='date_from',
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker_from'
        }),
        required = False
    )
    date_till = forms.DateTimeField(
        label='date_till',
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker_till'
        }),
        required = False,
        initial = datetime.now,
    )
