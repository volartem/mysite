from note.tasks import background_logging


class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response = self.process_response(request, response)
        return response

    def process_response(self, request, response):
        obj = get_info(request, response)
        background_logging.delay(obj)
        return response


def get_info(request, response):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    try:
        refer = request.META.get('HTTP_REFERER')[:255]
    except TypeError:
        refer = 'not_refer'
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    obj = {
        'status_code': response.status_code,
        'method': request.method,
        'ip': ip,
        'refer': refer,
        'path': request.path
    }
    return obj
