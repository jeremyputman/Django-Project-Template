# Application Imports
from apps.core.functions import get_client_ip

# Third Party Imports
from loguru import logger

class LoguruContextMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        username = request.user.username if request.user.is_authenticated else None
        ip = get_client_ip(request)
        # attach a request-scoped
        request.logger = logger.bind(
            user=username,
            ip=ip,
            method=request.method,
            path=request.environ["REQUEST_URI"],
            http_version=request.environ["SERVER_PROTOCOL"],
        )

        return self.get_response(request)
