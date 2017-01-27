from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import JsonResponse
from note.models import Note
from django.contrib.auth import logout
import requests, re

# from note.serializers import NoteSerializer, CommentSerializer
# from django.contrib.auth.models import User, Group
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.reverse import reverse
# from rest_framework.response import Response


def index(request):
    notes = Note.objects.all().order_by('id')
    return render(request, 'index.html', {'notes': notes})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    # social = request.user.social_auth.get(provider='facebook')
    # usernames = request.user.username
    # try:
    #     # user_id = request.user.uid
    #     user_id = request.user.social_auth.get(provider='facebook').uid
    #     token = request.user.social_auth.get(provider="facebook").tokens
    # except:
    #     print('error')
    # res = requests.get('https://www.facebook.com/{}'.format(usernames))
    # if res.status_code == requests.codes.ok:
    #     id_re = re.compile(r'"entity_id":"([0-9]+)"')
    #     new_username = id_re.findall(res.content)[0]
    # access_token = social.extra_data['access_token']
    # to_api = requests.get('https://graph.facebook.com/{0}'.format(user_id), params={'access_token': access_token})
    # to_api_f = requests.get('https://graph.facebook.com/me/photos', params={'access_token': access_token})
    # print(to_api)
    return render(request, 'profile.html')

def loginn(request):
    print('login')
    # social = request.user.social_auth.get(provider='facebook')
    # usernames = request.user.username
    # try:
    #     # user_id = request.user.uid
    #     user_id = request.user.social_auth.get(provider='facebook').uid
    #     token = request.user.social_auth.get(provider="facebook").tokens
    # except:
    #     print('error')
    # res = requests.get('https://www.facebook.com/{}'.format(usernames))
    # if res.status_code == requests.codes.ok:
    #     id_re = re.compile(r'"entity_id":"([0-9]+)"')
    #     new_username = id_re.findall(res.content)[0]
    # access_token = social.extra_data['access_token']
    # to_api = requests.get('https://graph.facebook.com/{0}'.format(user_id), params={'access_token': access_token})
    # to_api_f = requests.get('https://graph.facebook.com/me/photos', params={'access_token': access_token})
    # print(to_api)
    return render(request, 'profile.html')

def auth_logout(request):
    logout(request)
    return redirect('index')

# def save_comment(request):
#     print(request)
#     notes = Note.objects.all().order_by('id')
#     return render(request, 'index.html', {'notes': notes})