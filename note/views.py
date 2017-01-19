from django.shortcuts import render

# Create your views here.

def note_detail(request, pk):
    return render(request, 'note/note.html')