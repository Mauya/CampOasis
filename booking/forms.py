from django import forms
from .models import Booking

class BookingForm(forms.modelForm):

    class Meta:
        model = Booking
        fields = ['title', 'forename', 'surname', 'organisation', 'street1', 'street2', 'city', 'zip_code', 'phone',
                  'email', 'date_from', 'date_until']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email