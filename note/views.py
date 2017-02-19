from django.shortcuts import render, redirect
from .models import Note, Comment
from .forms import CommentModelForm
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from .serializers import CommentSerializer
from rest_framework import generics


def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    return render(request, 'note/note.html', {'note': note})


def note_comments(request, pk):
    comments = Comment.objects.filter(note_id=pk).order_by('-date_create')
    # dict_comments = [obj.as_dict() for obj in comments]
    dict_comments = serializers.serialize('json', comments)
    return JsonResponse(dict_comments, safe=False)


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


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        This view should return a list of all the comments
        for the current note.
        """
        pk = self.kwargs['pk']
        return Comment.objects.filter(note_id=pk).order_by('-date_create')

    def perform_create(self, serializer):
        try:
            if self.request.user.is_authenticated():
                note = self.kwargs.get('pk')
                serializer.save(owner=self.request.user, note_id=int(note))
        except TypeError:
            raise
