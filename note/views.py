from django.shortcuts import render
from .models import Note, Comment
from django.http import JsonResponse
from django.core import serializers
from .serializers import CommentSerializer
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist


def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    return render(request, 'note/note.html', {'note': note})


def note_comments(request, pk):
    comments = Comment.objects.filter(note_id=pk).order_by('-date_create')
    dict_comments = serializers.serialize('json', comments)
    return JsonResponse(dict_comments, safe=False)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = Comment.objects.\
            raw(
            'SELECT * FROM note_comment '
            'WHERE note_id = %s AND path && ARRAY[0] '
            'ORDER BY path[:];' % pk)
        return queryset

    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            note = self.kwargs.get('pk')
            try:
                obj = self.request.data.get('parent')
                parent_path = Comment.objects.get(id=obj).path
                path = []
                path.extend(parent_path)
            except (KeyError, ObjectDoesNotExist):
                path = [0]

            obj = serializer.save(
                owner=self.request.user,
                note_id=int(note),
                path=path
            )
            obj.path.append(obj.id)
            obj.save()
