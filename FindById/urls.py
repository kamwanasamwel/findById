
from django.contrib import admin
from django.urls import path
from django.conf import settings
from itemsfound.views import Homepage
from  django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homepage.as_view(), name='index'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
