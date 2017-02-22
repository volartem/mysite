# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Note
from .forms import CommentModelForm
from django.contrib import messages


def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    return render(request, 'note/note.html', {'note': note})


def add_comment(request, pk):
    if request.method == 'POST':
        form = CommentModelForm(request.POST or None, user=request.user, pk=pk)
        if form.is_valid():
            form.save()
            messages.success(request, "Your comment has been successfully added.", extra_tags='success')
            return redirect('note', pk)
        else:
            messages.success(request, "Please try again.", extra_tags='info')
            return redirect('note', pk)
