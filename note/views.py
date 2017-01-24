from django.shortcuts import render
from .models import Note
# Create your views here.

def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    return render(request, 'note/note.html', {'note': note})