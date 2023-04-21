from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from common.permissions import TemporaryPasswordChanged
from notifications.models import Notification
from notifications.serializers import UnreadNotificationCountSerializer


@extend_schema(
    tags=('Notifications',),
    description='Response count unread notifications logged in user',
)
class UnreadNotificationCountAPIView(RetrieveAPIView):
    serializer_class = UnreadNotificationCountSerializer
    permission_classes = (IsAuthenticated, TemporaryPasswordChanged)

    def get_object(self):
        return {'count': Notification.objects.prefetch_related('user').filter(user=self.request.user, status=False).count()}
