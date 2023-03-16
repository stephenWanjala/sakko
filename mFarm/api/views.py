from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(http_method_names=['GET'])
def apiRoutes(request):
    routes = [
        "api/token",
        "api/token/refresh",
        "api/signup",
        "api/login",
        "api/farmers",
        "api/farmer<pk:str>"
    ]
    return Response(data=routes)
