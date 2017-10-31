from models import User
from django.contrib.auth.backends import ModelBackend
from .models import booking

class EmailAuth(object):

    def authenticate(self, email=None, password=None):
        """
       Get an instance of User using the supplied email and check its password
       """
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
       Used by the django authentication system to retrieve an instance of User
       """
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None

"""Custom authentication backends for the booking app."""
class BookingIDBackend(ModelBackend):
    """
    Custom authentication backend that allows login via email and booking ID.
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            booking = Booking.objects.get(
                booking_id=password, user__email=username)
        except Booking.DoesNotExist:
            return None
        return booking.user