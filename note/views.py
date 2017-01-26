from django.shortcuts import render, redirect
from .models import Note
from .forms import CommentModelForm
# Create your views here.

def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    return render(request, 'note/note.html', {'note': note})


def add_comment(request, pk):
    if request.method == 'POST':
        model_form = CommentModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            # messages.success(request, "Course {0} has been successfully added.".format(model_form.cleaned_data['name']))
            return redirect('index')
        else:
            return redirect('note', pk)
    # else:
    #     model_form = CommentModelForm()
    # return render(request, 'courses/add.html', {'model': model_form})