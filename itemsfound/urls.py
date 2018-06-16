from django.conf.urls import url

from .views import search_page, result_page

urlpatterns = [
    url('^$', search_page, name="search_page"),
    url('^result_page/$', result_page, name="result_page"),
]