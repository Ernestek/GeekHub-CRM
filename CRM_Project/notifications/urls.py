from django.urls import path, include
from rest_framework import routers

from notifications.views.base_notifications import UnreadNotificationCountAPIView
from notifications.views.tasks_notifications import NotificationsListView

app_name = 'notifications'

tasks_router = routers.SimpleRouter()


urlpatterns = [
    path('user-count-unread-notifications', UnreadNotificationCountAPIView.as_view(), name='count-unread-notifications'),
    path('user-notifications/', NotificationsListView.as_view(), name='user-notifications'),
    path('', include(tasks_router.urls)),
]
