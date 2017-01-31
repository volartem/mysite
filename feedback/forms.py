from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ('create_date',)

        widgets = {
            'theme': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Theme'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
            'from_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
