from django import forms
from django.forms import ModelForm
from .models import Booking

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget=forms.PasswordInput())

class DateInput(forms.DateInput):
    input_type ='date'

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['name','description','Booking_ref','booking_date']
        widgets = {
            'booking_date' : DateInput(),
        }


