
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
from django.conf import settings
from itemsfound.views import Homepage
from  django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homepage.as_view(), name='index'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
=======
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('itemsfound.urls')),
    path('auth', include('users.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> d8a67fb0ae64310a4c827db3683439734ee72375
