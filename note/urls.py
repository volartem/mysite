from django.conf.urls import url
from note import views


urlpatterns = [
    url(r'(?P<pk>\d+)/comments/$', views.CommentList.as_view(), name='note_comments'),
    url(r'^$', views.ReadNoteViewSet.as_view({'get': 'list'}), name='note_list'),
    url(r'(?P<pk>\d+)/', views.ReadNoteViewSet.as_view({'get': 'retrieve'}), name='note_detail'),
]
