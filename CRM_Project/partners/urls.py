from django.urls import path, include
from rest_framework import routers

from partners.veiws.partner import PartnerViewSet

app_name = 'partners'

projects_router = routers.DefaultRouter()
projects_router.register('', PartnerViewSet)


urlpatterns = [
    path('', include(projects_router.urls)),
]
