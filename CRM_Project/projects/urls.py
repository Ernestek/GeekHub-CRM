from django.urls import path, include
from rest_framework import routers

from projects.views.partner_search import PartnerSearchByCodeView
from projects.views.project import ProjectViewSet
from projects.views.project_team import AddUserInTeam, DeleteUserFromTeam

app_name = 'projects'

projects_router = routers.DefaultRouter()
projects_router.register('', ProjectViewSet)


urlpatterns = [
    path('project-team-add-member', AddUserInTeam.as_view(), name='project-team-add-member'),
    path('project-team-remove-member', DeleteUserFromTeam.as_view(), name='project-team-remove-member'),
    path('search-partner-by-code', PartnerSearchByCodeView.as_view(), name='search-partner-by-code'),
    path('', include(projects_router.urls)),
]
