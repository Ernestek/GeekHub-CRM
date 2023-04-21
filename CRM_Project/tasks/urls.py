from django.urls import path, include
from rest_framework import routers

from tasks.views.user_search import UserSearchView
from tasks.views.user_task import UserTaskCreateViewSet, MyTaskCreateViewSet, UserTaskUpdateDestroyRetrieveViewSet, \
    UserTaskListViewSet

app_name = 'tasks'

tasks_router = routers.SimpleRouter()
tasks_router.register(r'user-task', UserTaskUpdateDestroyRetrieveViewSet)
tasks_router.register(r'user-task', UserTaskListViewSet)
tasks_router.register(r'add-task', MyTaskCreateViewSet)
tasks_router.register(r'assign-user-task', UserTaskCreateViewSet)



urlpatterns = [
    # re_path('^user-tasks/(?P<user_id>.+)/$', UserTaskListRetrieveViewSet.as_view({'get': 'list'})),
    # re_path('^user-tasks/(?P<user_id>.+)/(?P<id>.+)/$', UserTaskListRetrieveViewSet.as_view({'get': 'retrieve'})),
    # path('users/<int:user_id>/tasks/', UserTaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-tasks'),
    # path('user-tasks/<int:user_id>/', UserTaskListRetrieveViewSet.as_view({'get': 'list'})),
    # path('user-tasks/<int:user_id>/<int:id>/', UserTaskListRetrieveViewSet.as_view({'get': 'retrieve'})),

    path('user-search/', UserSearchView.as_view(), name='user-search'),
    path('', include(tasks_router.urls)),
]
