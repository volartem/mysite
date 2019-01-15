from celery import shared_task
from django.core.mail import send_mail
from mysite.settings import ADMINS


@shared_task
def send_admin_feedback(theme, message, from_who):
    send_mail(theme, message, from_who, ADMINS)
