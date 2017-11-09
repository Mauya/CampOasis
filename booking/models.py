from django.db import models
# from django.conf import settings
from accounts.models import User

class Booking(models.Model):
    """" this contain data about the booking itself and will include
    :booking-id, date_created, firstname, lastname, organisation,
    email, phone, start_date, end_date, total, notes (office only)
    """
    booking_id = models.CharField(max_length=100, verbose_name='Booking ID')
    user = models.ForeignKey(User, related_name='bookings')
    date_created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(verbose_name='Start Date')
    end_date = models.DateTimeField(verbose_name='End Date')
    notes = models.TextField(
        max_length=800,
    )

    def __str__(self):
        return self.booking_id
