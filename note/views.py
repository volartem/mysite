from django.shortcuts import render
from .models import Note, Comment
from django.http import JsonResponse
from django.core import serializers
from .serializers import CommentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route


def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    return render(request, 'note/note.html', {'note': note})


def note_comments(request, pk):
    comments = Comment.objects.filter(note_id=pk).order_by('-date_create')
    dict_comments = serializers.serialize('json', comments)
    return JsonResponse(dict_comments, safe=False)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().filter(parent=None)
    serializer_class = CommentSerializer

    @list_route()
    def roots(self, request):
        queryset = Comment.objects.filter(parent=None)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        try:
            if self.request.user.is_authenticated():
                note = self.kwargs.get('pk')
                serializer.save(owner=self.request.user, note_id=int(note))
        except TypeError:
            pass
