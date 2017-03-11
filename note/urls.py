from django.conf.urls import url
from note.views import CommentViewSet, note_detail


comment_list = CommentViewSet.as_view({'get': 'list',
                                       'post': 'create'})

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', note_detail, name='note'),
    url(r'(?P<pk>\d+)/comments/$', comment_list),
]
