from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import JsonResponse
from note.models import Note

# from note.serializers import NoteSerializer, CommentSerializer
# from django.contrib.auth.models import User, Group
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.reverse import reverse
# from rest_framework.response import Response


def index(request):
    notes = Note.objects.all().order_by('id')
    return render(request, 'index.html', {'notes': notes})

def contact(request):
    return JsonResponse({'contact': 'response_contact'})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
