from django.conf.urls import url, include
from .views import AboutView

urlpatterns = [
    url(r'^$', AboutView.as_view(), name='contact')
]