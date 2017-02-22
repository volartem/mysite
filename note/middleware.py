# -*- coding: utf-8 -*-
from .models import Something


class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        response = self.process_response(request, response)

        return response

    def process_response(self, request, response):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        try:
            if not request.is_ajax():
                current_request = Something(
                    method=request.method,
                    path=request.path,
                    status_code=response.status_code,
                    ip=ip
                )
                current_request.save()
        except:
            pass
        return response
