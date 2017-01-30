
def save_user_data(backend, user, response, is_new=False, *args, **kwargs):

    if not is_new:
        print('error')
    try:
        user.uid = response['id']
        user.provider = backend.name
        user.access_token = response['access_token']
        if user.provider == 'facebook':
            user.image_url = 'https://graph.facebook.com/{}/picture?type=large&w‌​idth=480&height=480'.format(user.uid)
        elif user.provider == 'github':
            user.image_url = response['avatar_url']
        else:
            user.image_url = response['image']['url']
        user.save()
    except:
        print('error_save')
