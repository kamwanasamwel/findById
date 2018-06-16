from django.conf.urls import url

from .views import register_user

urlpatterns = [
    url(r'', register_user, name="register"),
]