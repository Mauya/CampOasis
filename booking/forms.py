from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booking_id', 'date_created', 'firstname', 'surname', 'gender', 'organisation', 'phone',
                  'email', 'start_date', 'date_until', 'notes',
                  )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            message = "Please enter valid email address"
            raise forms.ValidationError(message)
        return email