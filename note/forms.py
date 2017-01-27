from .models import Comment, Note
from django import forms


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'text')

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('user')
        self.note = Note.objects.get(id=kwargs.pop('pk'))
        super(CommentModelForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(CommentModelForm, self).save(commit=False)
        instance.owner = self.owner
        instance.note = self.note
        if commit:
            instance.save()
        return instance