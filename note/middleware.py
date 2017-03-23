import logging

logger = logging.getLogger('ip_logger')


class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        response = self.process_response(request, response)

        return response

    def process_response(self, request, response):
        try:
            logger.warning("%s ;; %s" % (request.path, request.META))
        except:
            pass
        return response
