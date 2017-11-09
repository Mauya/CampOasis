# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .forms import BookingForm
from . import models

class BookingAdmin(admin.ModelAdmin):
    list_display = [
        'date_created', 'booking_id', 'user', 'start_date', 'end_date', 'notes',
    ]
    form = BookingForm

admin.site.register(models.Booking, BookingAdmin)