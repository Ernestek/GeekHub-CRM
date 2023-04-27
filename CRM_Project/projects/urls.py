from django.urls import path, include
from rest_framework import routers

from projects.views.partner_search import PartnerSearchByCodeView
from projects.views.project import ProjectViewSet
from projects.views.project_team import AddUserInTeam, DeleteUserFromTeam

app_name = 'projects'

projects_router = routers.DefaultRouter()
projects_router.register('', ProjectViewSet)


urlpatterns = [
    path('user-in-project-team-add', AddUserInTeam.as_view(), name='user-in-project-team-add'),
    path('<int:project_id>/remove-user-from-team/<int:user_id>/', DeleteUserFromTeam.as_view(), name='user-in-project-team-delete'),
    path('search-project-by-code', PartnerSearchByCodeView.as_view(), name='search-project-by-code'),
    path('', include(projects_router.urls)),
]
