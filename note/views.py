from .models import Note, Comment
from .serializers import CommentSerializer, NoteSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets


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


class NoteList(generics.GenericAPIView):
    serializer_class = NoteSerializer

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        notes = [note for note in Note.objects.all()]
        return Response(notes)


class ReadNoteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
