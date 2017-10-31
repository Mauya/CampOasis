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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
import accounts.views
import cart.views
import shop.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', accounts.views.home, name='index'),

    # URLs for the booking form.

    url(r'^(?P<pk>\d+)/$',accounts.views.BookingDetailView.as_view(), name='booking_detail'),
    url(r'^create/$',accounts.views.BookingCreateView.as_view(), name='booking_create'),
    url(r'^$', accounts.views.BookingListView.as_view(), name='booking_list'),


    # Add Django site authentication urls (for login, logout, password management)

    url(r'^pages/', include('django.contrib.auth.urls')),
    url(r'^register/$', accounts.views.register, name='register'),
    url(r'^login/$', accounts.views.login, name='login'),
    url(r'^logout/$', accounts.views.logout, name='logout'),
    url(r'^profile/$', accounts.views.profile, name='profile'),

    # Shop urls
    url(r'^shop/$', shop.views.shop, name='shop'),
    url(r'^list/$', shop.views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', shop.views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', shop.views.product_detail, name='product_detail'),

    # cart urls
    url(r'^$', cart.views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', cart.views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', cart.views.cart_remove, name='cart_remove'),

    # contact url
    url(r'^contact/$', accounts.views.contact, name='contact'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
