from rest_framework import serializers
from .models import Note, Comment
from django.contrib.auth.models import User


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class CommentSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    child_set = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('owner', 'text', 'title', 'date_create', 'id', 'child_set')

    def create(self, validated_data):
        """Create a new object"""
        try:
            validated_data['parent_id'] = self.initial_data['parent']
        except KeyError:
            validated_data['parent_id'] = None
        return Comment.objects.create(**validated_data)


class NoteSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = ('id', 'title', 'text', 'date_create', 'rubric', 'comments')
