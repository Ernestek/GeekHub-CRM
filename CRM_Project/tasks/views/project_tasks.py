from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from common.permissions import TemporaryPasswordChanged, IsOwnerOrInProject
from tasks.models import UserTask
from tasks.serializers.project_tasks import UserTasksInProjectSerializer


@extend_schema(
    tags=('UserTasks',),
    description='Get a list of user tasks filtered by project.'
)
class UserTasksInProjectListView(ListAPIView):
    queryset = UserTask.objects.select_related('user')
    serializer_class = UserTasksInProjectSerializer
    permission_classes = (IsAuthenticated, TemporaryPasswordChanged, IsOwnerOrInProject)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(project_id=self.kwargs.get('project_id'))
