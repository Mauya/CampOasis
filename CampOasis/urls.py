"""we_are_social URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from accounts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='index'),

    #Add Django site authentication urls (for login, logout, password management)

    url(r'^pages/', include('django.contrib.auth.urls')),
    url(r'^register/', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^profile/$', views.profile, name='profile'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls)))