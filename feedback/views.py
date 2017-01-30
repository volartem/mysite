from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Feedback
from .forms import FeedbackForm
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


class AboutView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,
                         'Ваш отзыв отправлен!', extra_tags='success')
        # send_mail(self.object.theme, self.object.message, self.object.from_email, settings.ADMINS)
        return response