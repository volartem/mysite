from django.urls import reverse_lazy
from .models import Feedback
from .forms import FeedbackForm
from django.views.generic.edit import CreateView
from django.contrib import messages
from .tasks import send_admin_feedback


class AboutView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        response = super().form_valid(form)
        try:
            send_admin_feedback.delay(self.object.theme, self.object.message, self.object.from_email)
            messages.success(self.request, 'Ваш отзыв отправлен!', extra_tags='success')
        except Exception:
            messages.success(self.request, 'Система отправки не пропускает Ваш отзыв', extra_tags='error')
        return response
