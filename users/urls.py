from django.conf.urls import url

from .views import update_profile

urlpatterns = [
    url(r'', update_profile, name="update"),
]