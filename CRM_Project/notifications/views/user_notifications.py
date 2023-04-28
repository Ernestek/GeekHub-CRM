from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from notifications.models import Notification
from notifications.serializers import NotificationSerializer, NotificationStatusUpdateSerializer

from common.permissions import TemporaryPasswordChanged, IsMyNotifications


@extend_schema(
    tags=('Notifications',),
    description='List all notifications. The user receives notifications '
                'when a task is assigned to him and its status changes, '
                'when added/removed from the project.'
)
class NotificationsListView(generics.ListAPIView):
    queryset = Notification.objects.select_related('user')
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated, TemporaryPasswordChanged]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['read']

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('created_at')


@extend_schema(
    tags=('Notifications',),
    description='Change status notifications'
)
class NotificationsUpdateStatusView(CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = NotificationStatusUpdateSerializer
    permission_classes = (IsAuthenticated, TemporaryPasswordChanged, IsMyNotifications)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.context['view'].object.read)
        return Response(request.data, status=status.HTTP_201_CREATED)


@extend_schema(
    tags=('Notifications',),
    description='Delete notification'
)
class NotificationDeleteView(DestroyAPIView):
    queryset = Notification.objects.select_related('user')
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated, TemporaryPasswordChanged, IsMyNotifications)
    serializer_class = NotificationSerializer
    lookup_field = 'id'
