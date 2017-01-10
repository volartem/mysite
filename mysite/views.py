from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from note.models import Note

def index(request):
    notes = Note.objects.all()
    return render(request, 'index.html', {'notes': notes})


def about(request):
    if request.method == 'POST':
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)