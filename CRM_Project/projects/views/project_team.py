from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.permissions import TemporaryPasswordChanged, IsStaff, IsOwner
from projects.models import Project
from projects.serializers.project_team import AddUserInProjectSerializer

User = get_user_model()


@extend_schema(
    tags=('Project',),
    description='Add user in project team',
    responses={
        204: OpenApiResponse(description='User added.'),
    }
)
class AddUserInTeam(CreateAPIView):
    serializer_class = AddUserInProjectSerializer
    permission_classes = [IsAuthenticated, TemporaryPasswordChanged, IsStaff, IsOwner]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(
    tags=('Project',),
    description='Remove a user from project team',
    responses={
        204: OpenApiResponse(description='User removed.'),
    }
)
class DeleteUserFromTeam(APIView):
    permission_classes = [IsAuthenticated, TemporaryPasswordChanged, IsStaff, IsOwner]

    def destroy(self, request, project_id, user_id):
        project = get_object_or_404(Project.objects.select_related('owner'), pk=project_id)
        user = get_object_or_404(User, pk=user_id)
        project.users.remove(user)
        return Response(status=status.HTTP_204_NO_CONTENT)
# class DeleteUserFromTeam(CreateAPIView):
#     serializer_class = AddUserInProjectSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated, TemporaryPasswordChanged, IsStaff, IsOwner]
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         print(serializer.data.get['user_id'])
#         # user_id = serializer.data['user_id']
#         # project = serializer.data['project']
#         # project.users.remove(user_id)
#         return Response(status=status.HTTP_204_NO_CONTENT)
