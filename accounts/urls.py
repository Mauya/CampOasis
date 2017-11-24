from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

# Add Django site authentication urls (for login, logout, password management)
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^$', views.home, name='home'),
    # contact url
    url(r'^contact/$', views.contact, name='contact'),
]