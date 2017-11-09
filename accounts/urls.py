from django.conf.urls import url
from . import views

# Add Django site authentication urls (for login, logout, password management)
url(r'^$', views.home, name='index'),
url(r'^register/$', views.register, name='register'),
url(r'^login/$', views.login, name='login'),
url(r'^logout/$', views.logout, name='logout'),
url(r'^profile/$', views.profile, name='profile'),

# contact url
url(r'^contact/$', views.contact, name='contact'),
