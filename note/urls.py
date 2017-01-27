from django.conf.urls import url
from note import views


urlpatterns = [
    url(r'^(?P<pk>[\d]+)/$', views.note_detail, name='note'),
    url(r'^add/comment/(?P<pk>\d+)$', views.add_comment, name='add_comment')
]