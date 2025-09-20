class ContentSecurityPolicyMiddleware:
def __init__(self, get_response):
self.get_response = get_response


def __call__(self, request):
response = self.get_response(request)
# Adjust policy to your needs
response.setdefault('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:;")
return response