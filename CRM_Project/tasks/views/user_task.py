from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import mixins, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from django.utils.translation import gettext_lazy as _

from common.permissions import TemporaryPasswordChanged, IsStaffOrAssigned, IsStaff
from tasks.serializers.user_task import UserTaskCreateSerializer, UserTasksListSerializer, \
    UserTasksRetrieveSerializer, UserTasksUpdateSerializer, MyTaskCreateSerializer
from tasks.models import UserTask


@extend_schema(
    tags=('UserTasks',),
    parameters=[
        OpenApiParameter(
            name='user_id',
            location='query',
            required=False,
            type=int,
            description='If the user_id field is empty, we will get information on the authorized user,'
                        'else get information about the user whose ID was entered.'
        ),
        OpenApiParameter(
            name='ordering',
            location='query',
            required=False,
            type=str,
            # description=''
            enum=['created_at', '-created_at']
        ),
    ],
    description='Get a list of user tasks.'
)
class UserTaskListViewSet(mixins.ListModelMixin,
                          GenericViewSet):
    queryset = UserTask.objects.select_related('user')
    permission_classes = (IsAuthenticated, TemporaryPasswordChanged,)
    serializer_class = UserTasksListSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend,)
    ordering_fields = ['created_at']
    ordering_description = 'Ordering by field updated_at'
    filterset_fields = ['status']

    # TODO: empty task list or not found user
    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is None:
            user_id = self.request.user.id
        return queryset.filter(user_id=user_id)


@extend_schema(
    tags=('UserTasks',),
    description='',
)
class UserTaskUpdateDestroyRetrieveViewSet(mixins.RetrieveModelMixin,
                                           mixins.UpdateModelMixin,
                                           mixins.DestroyModelMixin,
                                           GenericViewSet):
    queryset = UserTask.objects.select_related('user', 'user_assigned')
    permission_classes = [IsAuthenticated, TemporaryPasswordChanged, IsStaffOrAssigned]
    serializer_class = UserTasksUpdateSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserTasksRetrieveSerializer
        return UserTasksUpdateSerializer

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permission() for permission in (IsAuthenticated, TemporaryPasswordChanged)]
        return [permission() for permission in self.permission_classes]


@extend_schema(
    tags=('UserTasks',),
    description='Add task to logged in user',
)
class UserTaskCreateViewSet(mixins.CreateModelMixin,
                            GenericViewSet):
    queryset = UserTask.objects.select_related('user', 'user_assigned')
    permission_classes = (IsAuthenticated, TemporaryPasswordChanged, IsStaff)
    serializer_class = UserTaskCreateSerializer


@extend_schema(
    tags=('UserTasks',),
    description='Assign new tasks to other users',
)
class MyTaskCreateViewSet(mixins.CreateModelMixin,
                          GenericViewSet):
    queryset = UserTask.objects.select_related('user', 'user_assigned')
    permission_classes = (IsAuthenticated, TemporaryPasswordChanged,)
    serializer_class = MyTaskCreateSerializer


# @extend_schema(
#     tags=('MyTasks',),
#     description='Get a list of user tasks.'
# )
# class MyTaskViewSet(ModelViewSet):
#     queryset = UserTask.objects.select_related('user')
#     permission_classes = (IsAuthenticated, TemporaryPasswordChanged,)
#     serializer_class = UserTasksListSerializer
#     filter_backends = (filters.OrderingFilter,)
#     ordering_fields = ('updated_at', 'status',)
#     ordering_description = _('Ordering by field updated_at')
#
#     def get_serializer_class(self):
#         if self.action == 'retrieve':
#             return MyTasksRetrieveSerializer
#         if self.action == 'update':
#             return MyTasksUpdateSerializer
#         if self.action == 'create':
#             return MyTaskCreateSerializer
#         return MyTasksListSerializer
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         user_id = self.request.user.id
#         return queryset.filter(user_id=user_id)

#
# @extend_schema(
#     tags=('UserTasks',),
#     parameters=[
#         OpenApiParameter(
#             name='user_id',
#             location='query',
#             required=False,
#             type=int,
#             description='If the user_id field is empty, we will get information on the authorized user,'
#                         'else get information about the user whose ID was entered.'
#         ),
#     ],
#     description='Get a list of user tasks.'
# )
# class UserTaskListRetrieveViewSet(ReadOnlyModelViewSet):
#     queryset = UserTask.objects.select_related('user')
#     permission_classes = (IsAuthenticated, TemporaryPasswordChanged,)
#     serializer_class = UserTasksListSerializer
#     filter_backends = (filters.OrderingFilter,)
#     ordering_fields = ['created_at']
#     ordering_description = _('Ordering by field created_at')
#     # search_fields = ['user__id', 'user__email']
#
#     def get_serializer_class(self):
#         if self.action == 'retrieve':
#             return UserTasksRetrieveSerializer
#         return UserTasksListSerializer
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#
#         # try:
#         #     user = self.kwargs['user_id']
#         # except KeyError:
#         #     user = self.request.user
#         user_id = self.request.query_params.get('user_id', None)
#         if user_id is None:
#             user_id = self.request.user.id
#
#         return queryset.filter(user_id=user_id)
