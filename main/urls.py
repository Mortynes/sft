from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, contact


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
]

if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
