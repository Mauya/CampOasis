# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .forms import BookingForm
# from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'creation_date', 'booking_id', 'email', 'start_date', 'date_until',
    ]
    form = BookingForm
