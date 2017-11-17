from django import forms
from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Booking
        fields = ('booking_id', 'start_date', 'end_date', 'notes',)
