from rest_framework import serializers
from .models import Note, Comment


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        exclude = []


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('owner', 'text', 'title', 'date_create')
