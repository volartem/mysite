from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from note.models import Note
from django.contrib.auth import logout
from django.contrib import messages
# import requests, re

# from note.serializers import NoteSerializer, CommentSerializer
# from django.contrib.auth.models import User, Group
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.reverse import reverse
# from rest_framework.response import Response


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

# def save_comment(request):
#     print(request)
#     notes = Note.objects.all().order_by('id')
#     return render(request, 'index.html', {'notes': notes})