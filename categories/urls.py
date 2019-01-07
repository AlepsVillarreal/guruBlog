from django.conf.urls import url
from . import views

app_name = 'categories'

urlpatterns = [
    url(r'^(?P<hierarchy>.+)/$', views.show_category, name="category"),
#	url(r'^(?P<hierarchy>.+)/$', views.show_category, name='category'),
]