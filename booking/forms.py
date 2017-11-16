from django import forms
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BookingForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('booking_id', 'start_date', 'end_date', 'notes',)

    def save(self, commit=True):
        user = super(BookingForm, self).save(commit=False)

        if commit:
            user.save()
        return user