# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from django.contrib import messages

def booking_form(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # success message
        messages.success(request, "successfully created")
        return redirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not Successfully Created")
    context = {
        "form": form,
    }
    return render(request, 'booking_form.html', context)

def booking_detail(request, id=None):
    instance = get_object_or_404(booking_form)
    context ={
        "title": instance.title,
        "instance": instance,
    }
    return render(request, booking_detail, context)

def booking_list(request):
    queryset = get_object_or_404(BookingForm)
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "booking_list.html", context)

def booking_update(request, id=None):
    instance = get_object_or_404(BookingForm)
    form = BookingForm(request.POST or None, Instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "< a href='#'>Item</a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "", context)

def post_delete(request, id=None):
    instance = get_object_or_404(BookingForm)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("booking_list")