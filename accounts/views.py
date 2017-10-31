# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm, ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.core.urlresolvers import reverse
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

from .forms import BookingForm
from .models import Booking

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                messages.success(request, "You have successfully registered")
                return redirect(reverse('profile'))

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        form = UserRegistrationForm()

    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))

def contact(request):
    form_class = ContactForm

    return render(request, 'contact.html', {
        'form': form_class,
    })

"""Views for the booking form."""
# ------ MIXINS ------ #

class BookingViewMixin(object):
    model = Booking
    form_class = BookingForm


# ------ MODEL VIEWS ------ #

class BookingCreateView(BookingViewMixin, CreateView):
    """View to create a new ``Booking`` instance."""
    def get_success_url(self):
        return reverse('booking_detail', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(BookingCreateView, self).get_form_kwargs(
            *args, **kwargs)
        if self.request.user.is_authenticated():
            kwargs.update({'user': self.request.user})
        else:
            # If the user is not authenticated, get the current session
            if not self.request.session.exists(
                    self.request.session.session_key):
                self.request.session.create()
            kwargs.update({'session': Session.objects.get(
                session_key=self.request.session.session_key)})
        return kwargs


class BookingDetailView(BookingViewMixin, DetailView):
    """View to display a ``Booking`` instance."""
    def dispatch(self, request, *args, **kwargs):
        self.kwargs = kwargs
        self.object = self.get_object()
        if request.user.is_authenticated():
            # If user doesn't own the booking forbid access
            if not self.object.user == request.user:
                raise Http404
        else:
            # If anonymous doesn't own the booking forbid access
            session = self.object.session
            if (not session or not request.session.session_key or
                    session.session_key != request.session.session_key):
                raise Http404
        return super(BookingViewMixin, self).dispatch(request, *args, **kwargs)


class BookingListView(BookingViewMixin, ListView):
    """View to display all ``Booking`` instances of one user."""
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BookingViewMixin, self).dispatch(self, request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.bookings.all()
