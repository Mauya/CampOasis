# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    gender = models.CharField(max_length=10, verbose_name='Gender', default='Male')
    organisation = models.CharField(max_length=20, verbose_name='Organisation', default="")
    phone = models.IntegerField(default=0)

    def create_profile(sender, **kwargs):
        user = kwargs['instance']
        if kwargs['created']:
            profile = user.models.UserProfile()
            profile.setUser(sender)
            profile.save()

    post_save.connect(create_profile, sender=User)