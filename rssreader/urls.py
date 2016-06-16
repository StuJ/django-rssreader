
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('reader_app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
]
