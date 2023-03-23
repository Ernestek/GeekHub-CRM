from django.urls import path, include
from rest_framework import routers

from partners.views import PartnerViewSet, PartnerContactPersonViewSet

app_name = 'partners'

partners_router = routers.DefaultRouter()
partners_router.register('', PartnerViewSet, 'partners')

contacts_router = routers.DefaultRouter()
contacts_router.register('', PartnerContactPersonViewSet, 'contacts')

urlpatterns = [
    path('contacts/', include(contacts_router.urls)),
    path('', include(partners_router.urls)),

]
