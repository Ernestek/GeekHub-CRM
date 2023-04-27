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
        204: OpenApiResponse(description='User added.'),
    }
)
class AddUserInTeam(CreateAPIView):
    serializer_class = AddUserInProjectSerializer
    permission_classes = [IsAuthenticated, TemporaryPasswordChanged, IsStaff]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


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
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)




# class DeleteUserFromTeam(APIView):
#     permission_classes = [IsAuthenticated, TemporaryPasswordChanged, IsStaff, IsOwner]
#
#     def delete(self, request, project_id, contact_id):
#         project = get_object_or_404(Project.objects.select_related('owner'), pk=project_id)
#
#         if request.user != project.owner:
#             return Response({'detail': _('You do not have permission to perform this action.')},
#                             status=status.HTTP_403_FORBIDDEN)
#         print(project.users.values_list('id', flat=True))
#         if contact_id in project.users.values_list('id', flat=True):
#             project.users.remove(contact_id)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         # user = get_object_or_404(User, pk=contact_id)
#         return Response(status=status.HTTP_204_NO_CONTENT)