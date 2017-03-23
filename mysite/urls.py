"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mysite import views
from django.conf.urls.static import static
from mysite import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/', include('feedback.urls')),
    url(r'rubric/(?P<pk>\w+)/$', views.rubric, name='rubric'),
    url(r'^note/', include('note.urls')),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.auth_logout, name='logout'),
    url(r'^social/', include('social_django.urls', namespace='social')),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

