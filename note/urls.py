from django.conf.urls import url
from note import views


urlpatterns = [
    url(r'^(?P<pk>[\d]+)/$', views.note_detail, name='note'),
]