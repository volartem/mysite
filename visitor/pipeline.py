from .models import Visitor


def save_user_data(backend, user, response, is_new=False, *args, **kwargs):
    '''
        Save in special table but important get correct url avatar 
    '''

    id = response.get('id') or response['uid']
    if not is_new:
        auth_user = Visitor.objects.get(uid=id)
        old_url = get_url(backend.name, response, id)
        if old_url != auth_user.image_url:
            auth_user.image_url = get_url(backend.name, response, id)
            auth_user.save()
    else:
        try:
            user.uid = id
            user.provider = backend.name
            user.access_token = response['access_token']
            user.image_url = get_url(user.provider, response, id)
            user.username = '%s %s' % (response['first_name'], response['last_name']) or user.username
            user.save()
        except:
            print('error_save')
            pass


def get_url(provider, response, id):
    if provider == 'facebook':
        image_url = 'https://graph.facebook.com/{}/picture?type=large&w‌​idth=480&height=480'.\
            format(id)
    elif provider == 'github':
        image_url = response['avatar_url']
    elif provider == 'yandex-oauth2':
        if response['is_avatar_empty']:
            image_url = '/static/images/logo.png'
        else:
            image_url = 'https://avatars.mds.yandex.net/get-yapic/{}/big'. \
                format(response['default_avatar_id'])
    elif provider == 'twitter':
        image_url = response['profile_image_url_https'] or '/static/images/logo.png'
    elif provider == 'mailru-oauth2':
        if response['has_pic']:
            image_url = response['pic_190']
        else:
            image_url = '/static/images/logo.png'
    elif provider == 'vk-oauth2':
        image_url = response['user_photo'] if response['user_photo'] != 'http://vk.com/images/camera_50.png' \
            else '/static/images/logo.png'
    elif provider == 'google-oauth2':
        image_url = response['image']['url']
    else:
        image_url = '/static/images/logo.png'
    return image_url
