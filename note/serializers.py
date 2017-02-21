from rest_framework import serializers
from .models import Note, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class CommentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('owner', 'text', 'title', 'date_create')


class NoteSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = ('id', 'title', 'text', 'date_create', 'rubric', 'comments')
