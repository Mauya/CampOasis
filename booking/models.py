from django.db import models
# from django.conf import settings
# from django.utils import timezone

class Booking(models.Model):
    """" this contain data about the booking itself and will include
    :booking-id, date_created, firstname, lastname, organisation,
    email, phone, start_date, date_until, total, notes (office only)
    """
    booking_id = models.CharField(max_length=100, verbose_name='Booking ID')
    date_created = models.DateTimeField(verbose_name='Date Created')
    firstname = models.CharField(max_length=20, verbose_name='First Name')
    surname = models.CharField(max_length=50, verbose_name='Surname')
    gender = models.CharField(max_length=10, verbose_name='Gender')
    organisation = models.CharField(max_length=20, verbose_name='Organisation')
    email = models.CharField(max_length=255, verbose_name='Email')
    phone = models.IntegerField(max_length=255, verbose_name='Phone')
    start_date = models.DateTimeField(verbose_name='Start Date')
    date_until = models.DateTimeField(verbose_name='End Date', auto_now_add=True)
    notes = models.TextField(
        max_length=800,
    )

    def __str__(self):
        return self.firstname
