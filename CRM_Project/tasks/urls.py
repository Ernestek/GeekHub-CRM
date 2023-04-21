from django.urls import path, include
from rest_framework import routers

from tasks.views.user_search import UserSearchView
from tasks.views.user_task import UserTaskCreateViewSet, MyTaskCreateViewSet, UserTaskUpdateDestroyRetrieveViewSet, \
    UserTaskListViewSet

app_name = 'tasks'

tasks_router = routers.SimpleRouter()
tasks_router.register(r'user-task', UserTaskUpdateDestroyRetrieveViewSet)
tasks_router.register(r'user-task', UserTaskListViewSet)
tasks_router.register(r'add-task-to-self', MyTaskCreateViewSet)
tasks_router.register(r'staff-assign-user-task', UserTaskCreateViewSet)


urlpatterns = [
    path('user-search/', UserSearchView.as_view(), name='user-search'),
    path('', include(tasks_router.urls)),
]
