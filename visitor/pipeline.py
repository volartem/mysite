# django_project/visitor/pipeline.py
import requests
from slugify import slugify
from django.core.files.base import ContentFile

# Процедура для pipiline, сохраняющая изображение.
def save_user_data(backend, user, response, is_new=False, *args, **kwargs):

    if not is_new:
        print('error')
    try:
        user.uid = int(response['id'])
        user.provider = backend.name
        user.access_token = response['access_token']
        if user.provider == 'facebook':
            user.image_url = 'https://graph.facebook.com/{}/picture'.format(user.uid)
        else:
            user.image_url = response['avatar_url']
        user.save()
    except:
        print('error_save')