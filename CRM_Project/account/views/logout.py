from django.core.exceptions import ObjectDoesNotExist
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


@extend_schema(
    tags=('Account',),
    description='Destroy token authentication',
    responses={
        205: OpenApiResponse(description='Reset content.'),
    }
)
class LogoutView(APIView):
    """
    Use this endpoint to logout user (remove user authentication token).
    """
    serializer_class = None
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        return Response(status=status.HTTP_205_RESET_CONTENT)

