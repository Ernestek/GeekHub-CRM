from django.urls import path, include
from rest_framework import routers

from projects.views import ProjectViewSet

app_name = 'projects'

# projects_router = routers.DefaultRouter()
# projects_router.register('', ProjectViewSet)


urlpatterns = [
    # path('', include(projects_router.urls)),
]