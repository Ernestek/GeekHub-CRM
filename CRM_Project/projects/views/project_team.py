from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.permissions import TemporaryPasswordChanged, IsStaff
from projects.serializers.project_team import AddUserInProjectSerializer, RemoveUserInProjectSerializer


@extend_schema(
    tags=('Project',),
    description='Add user in project team',
    responses={
        200: OpenApiResponse(description='User added.'),
    }
)
class AddUserInTeam(CreateAPIView):
    serializer_class = AddUserInProjectSerializer
    permission_classes = [IsAuthenticated, TemporaryPasswordChanged, IsStaff]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(
    tags=('Project',),
    description='Remove a user from project team',
    responses={
        204: OpenApiResponse(description='User removed.'),
    }
)
class DeleteUserFromTeam(GenericAPIView):
    serializer_class = RemoveUserInProjectSerializer
    permission_classes = [IsAuthenticated, TemporaryPasswordChanged, IsStaff]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
