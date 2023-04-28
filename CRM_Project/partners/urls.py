from django.urls import path, include
from rest_framework import routers

from partners.veiws.partner import PartnerViewSet
from partners.veiws.partners_contact import AddUserInPartnerContacts, DeleteUserFromPartnerContacts

app_name = 'partners'

projects_router = routers.DefaultRouter()
projects_router.register('', PartnerViewSet)


urlpatterns = [
    path('partner-contacts-add', AddUserInPartnerContacts.as_view(), name='partner-contacts-add'),
    path('partner-contacts-remove', DeleteUserFromPartnerContacts.as_view(), name='partner-contacts-remove'),
    path('', include(projects_router.urls)),
]
