from .models import Comment
from django import forms


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text'}),
        }