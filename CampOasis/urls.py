from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from CampOasis import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
    url(r'^booking/', include('booking.urls', namespace='booking')),
    url(r'^shop/', include('shop.urls', namespace='shop')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    # url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^$', views.login_redirect, name='login_redirect'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
