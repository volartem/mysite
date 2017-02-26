# -*- coding: utf-8 -*-
from .models import Something
from ipware.ip import get_ip


class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        response = self.process_response(request, response)

        return response

    def process_response(self, request, response):
        ip_address = get_ip(request)

        if not request.is_ajax():
            current_request = Something(
                method=request.method,
                path=request.path,
                status_code=response.status_code,
                ip=ip_address
            )
            current_request.save()

        return response
