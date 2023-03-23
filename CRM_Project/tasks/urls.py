from django.urls import path, include
from rest_framework import routers

from tasks.views import TasksViewSet

app_name = 'tasks'

tasks_router = routers.DefaultRouter()
tasks_router.register('', TasksViewSet)


urlpatterns = [
    path('', include(tasks_router.urls)),
]