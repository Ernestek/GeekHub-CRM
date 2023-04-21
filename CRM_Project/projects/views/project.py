from django.db.models import Q
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from projects.models import Project
from common.permissions import TemporaryPasswordChanged, IsStaffOrAssigned, IsStaff, IsOwner
from projects.serializers.project import ProjectListSerializer, ProjectRetrieveSerializer, ProjectCreateSerializer, \
    ProjectUpdateSerializer


@extend_schema(
    tags=('Project',),
    description='',
)
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.select_related('partner', 'owner')
    permission_classes = (IsAuthenticated, TemporaryPasswordChanged)
    serializer_class = ProjectListSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, TemporaryPasswordChanged, IsStaff, IsOwner]
        else:
            permission_classes = [IsAuthenticated, TemporaryPasswordChanged]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = self.queryset
        if self.action == 'retrieve':
            queryset = queryset.prefetch_related('users')
            queryset = queryset.filter(
                Q(owner=self.request.user) | Q(users=self.request.user)
            )
        elif self.action == 'list':
            queryset = queryset.filter(
                Q(owner=self.request.user) | Q(users=self.request.user)
            ).distinct().order_by('id')
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        if self.action == 'retrieve':
            return ProjectRetrieveSerializer
        if self.action == 'create':
            return ProjectCreateSerializer
        return ProjectUpdateSerializer


