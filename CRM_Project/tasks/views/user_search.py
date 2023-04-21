from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from common.permissions import TemporaryPasswordChanged
from tasks.serializers.user_search import UserSearchSerializer

User = get_user_model()


@extend_schema(
    tags=('Common',),
    parameters=[
        OpenApiParameter(
            name='full_name',
            location='query',
            required=False,
            type=str,
        ),
    ],
    description='Search user by full name.'
)
class UserSearchView(APIView):
    serializer_class = UserSearchSerializer
    permission_classes = (IsAuthenticated, TemporaryPasswordChanged)

    def get(self, request, format=None):
        query_full_name = self.request.query_params.get('full_name', None)
        if query_full_name:
            q_obj = Q(first_name__icontains=query_full_name) | Q(last_name__icontains=query_full_name)
            users = User.objects.filter(q_obj)
            serializer = self.serializer_class(users, many=True)
            return Response(serializer.data)
        else:
            return Response([])
