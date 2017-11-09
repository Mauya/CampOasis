
from django.conf.urls import url
import booking.views

# Booking form urls
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', booking.views.booking_detail, name='booking_detail'),
    url(r'^booking/$', booking.views.booking_form, name='booking_form'),
    url(r'^$', booking.views.booking_list, name='booking_list'),
    ]
