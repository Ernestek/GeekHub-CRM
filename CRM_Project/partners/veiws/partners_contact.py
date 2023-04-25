from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from partners.models import PartnerContactPerson
from partners.serializers.partners_contact import ContactPersonListSerializer


class PartnerContactPersonViewSet(ModelViewSet):
    queryset = PartnerContactPerson.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = ContactPersonListSerializer
