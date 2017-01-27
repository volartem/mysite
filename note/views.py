from django.shortcuts import render, redirect
from .models import Note, Comment
from .forms import CommentModelForm
from django.views.generic.edit import FormView
# Create your views here.

def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    return render(request, 'note/note.html', {'note': note})


def add_comment(request, pk):
    if request.method == 'POST':
        form = CommentModelForm(request.POST or None, user=request.user, pk=pk)
        if form.is_valid():
            form.save()
            # messages.success(request, "Course {0} has been successfully added.".format(model_form.cleaned_data['name']))
            return redirect('note', pk)
        else:
            return redirect('note', pk)
    # else:
    #     model_form = CommentModelForm()
    # return render(request, 'courses/add.html', {'model': model_form})


