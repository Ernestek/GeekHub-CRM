from django.urls import path

from notifications.views.count_unread_notifications import UnreadNotificationCountAPIView
from notifications.views.user_notifications import NotificationsListView, NotificationsUpdateStatusView, \
    NotificationDeleteView

app_name = 'notifications'


urlpatterns = [
    path('user-notidications-change-status', NotificationsUpdateStatusView.as_view(), name='status'),
    path('user-notifications-count-unread', UnreadNotificationCountAPIView.as_view(), name='count-unread-notifications'),
    path('user-notifications/', NotificationsListView.as_view(), name='user-notifications'),
    path('user-notifications/<int:id>/', NotificationDeleteView.as_view(), name='delete-notification'),
]

