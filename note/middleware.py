# -*- coding: utf-8 -*-
from .models import Something
from ipware.ip import get_ip
import logging


logger = logging.getLogger('bad_ip_log')


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
        logger.info("Before db %s :: %s :: %s :: %s" % (request.method,
                                                        request.path,
                                                        response.status_code,
                                                        ip_address))
        if ip_address is not None:
            if not request.is_ajax():
                current_request = Something(
                    method=request.method,
                    path=request.path,
                    status_code=response.status_code,
                    ip=ip_address
                )
                current_request.save()
        else:
            logger.warning("%s ;; %s" % (request.path, request.META))

        return response
