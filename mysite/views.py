from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from note.models import Note
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from django.contrib.syndication.views import Feed


def index(request):
    notes = Note.objects.all().order_by('id').reverse()
    paginator = Paginator(notes, 5)

    page = request.GET.get('page')
    try:
        pagin_notes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pagin_notes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pagin_notes = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'notes': pagin_notes})


def rubric(request, pk):
    notes = Note.objects.filter(rubric=pk)
    paginator = Paginator(notes, 5)

    page = request.GET.get('page')
    try:
        pagin_notes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pagin_notes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pagin_notes = paginator.page(paginator.num_pages)
    return render(request, 'rubric.html', {'notes': pagin_notes})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')


def auth_logout(request):
    logout(request)
    messages.success(request, 'You are logout.', extra_tags='info')
    return redirect('index')


def site_map(request):
    posts = {
        'queryset': Note.objects.all(),
        'date_field': 'date_create',
    }
    site = {
        'notes': GenericSitemap(posts),
    }
    return sitemap(request, sitemaps=site)


class SiteFeed(Feed):
    title = u"myblognotes.ru: Краткие записи при работе с Python, Django, Linux, базами данных " \
            u"и прочие полезности в мире web(а)..."
    link = "/"
    description = u"Заходите, читайте и находите полезное для себя на данном ресурсе"

    def items(self):
        return Note.objects.order_by('-date_create')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text[0:200] + ""
