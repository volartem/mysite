from rest_framework import serializers
from .models import Note, Comment


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        exclude = []


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = []
